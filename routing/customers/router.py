import logging
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Customer
from schemas import CustomerSchema, FrequentCustomerSchema, InputCustomerSchema
from .customer_creation_response import CustomerCreationResponseSchema
from .customer_creation_status import CustomerCreationStatus
from .customer_search_response import CustomerSearchResponseSchema
from ..utils import date_to_mysql_string, create_object

router = APIRouter(prefix="/customers")
logger = logging.getLogger("customers")


@router.get("/")
async def get_customers(session: AsyncSession = Depends(get_session)) -> list[CustomerSchema]:
    query = select(Customer)
    query_result = await session.execute(query)
    return [CustomerSchema.model_validate(customer_orm) for customer_orm in query_result.scalars().all()]


@router.get("/search")
async def find_customer(customer_id: int, session: AsyncSession = Depends(get_session)) -> CustomerSearchResponseSchema:
    optional_customer: Optional[Customer] = await session.get(Customer, ident=customer_id)
    return CustomerSearchResponseSchema(customer=CustomerSchema.model_validate(optional_customer))


@router.post("/")
async def create_customer(
    input_customer: InputCustomerSchema, session: AsyncSession = Depends(get_session)
) -> CustomerCreationResponseSchema:
    try:
        customer = Customer(
            full_name=input_customer.full_name, phone_number=input_customer.phone_number, address=input_customer.address
        )
        await create_object(session, customer)
        await session.commit()
        return CustomerCreationResponseSchema(status=CustomerCreationStatus.SUCCESS)
    except Exception as e:
        logger.error(f"Creation of ({input_customer}) failed", exc_info=e)
        return CustomerCreationResponseSchema(status=CustomerCreationStatus.ALREADY_EXISTS_OR_INVALID)


@router.get("/waiting-supplies")
async def get_waiting_supplies_customers(
    drug_type_id: Optional[int] = None, session: AsyncSession = Depends(get_session)
) -> list[CustomerSchema]:
    query = text(_get_waiting_supplies_customers_query_string(drug_type_id))
    query_result = await session.execute(query)

    waiting_supplies_customers: list[CustomerSchema] = []

    for row in query_result:
        customer_id: int = row[0]
        customer_orm = await session.get(Customer, ident=customer_id)
        waiting_supplies_customers.append(CustomerSchema.model_validate(customer_orm))

    return waiting_supplies_customers


@router.get("/ordered-something")
async def get_ordered_something_customers(
    period_start: date,
    period_end: date,
    drug_id: Optional[int] = None,
    drug_type_id: Optional[int] = None,
    session: AsyncSession = Depends(get_session),
) -> list[CustomerSchema]:
    query = text(
        _get_ordered_something_customers_query_string(
            period_start=period_start, period_end=period_end, drug_id=drug_id, drug_type_id=drug_type_id
        )
    )
    result = await session.execute(query)

    ordered_something_customers: list[CustomerSchema] = []

    for row in result:
        customer_id: int = row[0]
        customer_orm = await session.get(Customer, ident=customer_id)
        ordered_something_customers.append(CustomerSchema.model_validate(customer_orm))

    return ordered_something_customers


@router.get("/frequent")
async def get_frequent_customers(
    drug_id: Optional[int] = None, drug_type_id: Optional[int] = None, session: AsyncSession = Depends(get_session)
) -> list[FrequentCustomerSchema]:
    query = text(_get_frequent_customers_query_string(drug_id=drug_id, drug_type_id=drug_type_id))
    result = await session.execute(query)

    frequent_customers: list[FrequentCustomerSchema] = []

    for row in result:
        customer_id: int = row[0]
        customer_orm = await session.get(Customer, ident=customer_id)

        frequent_customers.append(
            FrequentCustomerSchema(
                customer=CustomerSchema.model_validate(customer_orm),
                order_count=row[1],
            )
        )

    return frequent_customers


def _get_ordered_something_customers_query_string(
    period_start: date, period_end: date, drug_id: Optional[int] = None, drug_type_id: Optional[int] = None
) -> str:
    period_start_string: str = date_to_mysql_string(period_start)
    period_end_string: str = date_to_mysql_string(period_end)
    period_condition: str = f"(registration_datetime between {period_start_string} and {period_end_string})"

    if drug_id is not None:
        return f"""
            select distinct
                customer_id
            from prescriptions_content
                join orders using (prescription_id)
            where
                {period_condition}
                and (prescriptions_content.drug_id = {drug_id})
                and customer_id is not null
        """

    if drug_type_id is not None:
        return f"""
            select distinct
                customer_id
            from prescriptions_content
                join drugs on prescriptions_content.drug_id = drugs.id
                join orders using (prescription_id)
            where
                {period_condition}
                and (drugs.type_id = {drug_type_id})
                and customer_id is not null
        """

    return f"""
        select distinct
            customer_id
        from prescriptions_content
            join orders using (prescription_id)
        where
            {period_condition}
            and customer_id is not null
    """


def _get_frequent_customers_query_string(drug_id: Optional[int] = None, drug_type_id: Optional[int] = None) -> str:
    if drug_id is not None:
        return f"""
            select
                id as customer_id,
                orders_count
            from (
                select
                    customers.id,
                    count(*) as orders_count,
                    dense_rank() over (order by count(*) desc) as dr
                from orders
                    join prescriptions_content using (prescription_id)
                    join customers on orders.customer_id = customers.id
                where drug_id = {drug_id}
                group by customer_id
                ) all_orders_count_data
            where dr = 1
        """

    if drug_type_id is not None:
        return f"""
            select
                id as customer_id,
                orders_count
            from (
                select
                    customers.id,
                    count(*) as orders_count,
                    dense_rank() over (order by count(*) desc) as dr
                from orders
                    join prescriptions_content using (prescription_id)
                    join drugs on prescriptions_content.drug_id = drugs.id
                    join customers on orders.customer_id = customers.id
                where type_id = {drug_type_id}
                group by customer_id
                ) all_orders_count_data
            where dr = 1
        """

    return """
            select
                id as customer_id,
                orders_count
            from (
                select
                    customers.id,
                    count(*) as orders_count,
                    dense_rank() over (order by count(*) desc) as dr
                from orders
                    join prescriptions_content using (prescription_id)
                    join customers on orders.customer_id = customers.id
                group by customer_id
                ) all_orders_count_data
            where dr = 1
        """


def _get_waiting_supplies_customers_query_string(drug_type_id: Optional[int]) -> str:
    condition: str = "" if drug_type_id is None else f"drugs.type_id = {drug_type_id} and"

    return f"""
        select distinct
            customer_id
        from orders
            join orders_waiting_drug_supplies on orders.id = orders_waiting_drug_supplies.order_id
            join drugs on orders_waiting_drug_supplies.drug_id = drugs.id
        where {condition} customer_id is not null
    """
