from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import CustomerOrm
from schemas import Customer, FrequentCustomer

router = APIRouter(prefix="/customers")


@router.get("/")
async def get_customers(session: AsyncSession = Depends(get_session)) -> list[Customer]:
    query = select(CustomerOrm)
    result = await session.execute(query)
    return [Customer.model_validate(i) for i in result.scalars().all()]


@router.get("/waiting-supplies")
async def get_waiting_supplies_customers(drug_type_id: Optional[int] = None, session: AsyncSession = Depends(get_session)) -> list[Customer]:
    tmp = "" if drug_type_id is None else f"drugs.type_id = {drug_type_id} and"

    query_string = f"""
        select distinct
            customer_id
        from orders
            join orders_waiting_drug_supplies on orders.id = orders_waiting_drug_supplies.order_id
            join drugs on orders_waiting_drug_supplies.drug_id = drugs.id
        where {tmp} customer_id is not null
    """

    query = text(query_string)
    result = await session.execute(query)

    customers: list[Customer] = []

    for i in result:
        c = await session.get(CustomerOrm, ident=i[0])
        customers.append(Customer.model_validate(c))

    return customers


@router.get("/ordered-something")
async def get_ordered_something_customers(
    period_start: date, period_end: date, drug_id: Optional[int] = None, drug_type_id: Optional[int] = None, session: AsyncSession = Depends(get_session)
) -> list[Customer]:
    query = text(_get_ordered_something_customers_query_string(
        period_start=period_start,
        period_end=period_end,
        drug_id=drug_id,
        drug_type_id=drug_type_id
    ))
    result = await session.execute(query)

    customers: list[Customer] = []

    for row in result:
        q = await session.get(CustomerOrm, ident=row[0])
        customers.append(Customer.model_validate(q))

    return customers


@router.get("/frequent")
async def get_frequent_customers(
    drug_id: Optional[int] = None,
    drug_type_id: Optional[int] = None,
    session: AsyncSession = Depends(get_session)
) -> list[FrequentCustomer]:
    query = text(_get_frequent_customers_query_string(drug_id=drug_id, drug_type_id=drug_type_id))
    result = await session.execute(query)

    customers: list[FrequentCustomer] = []

    for row in result:
        q = await session.get(CustomerOrm, ident=row[0])
        c = Customer.model_validate(q)

        customers.append(FrequentCustomer(
            customer=c,
            orders_count=row[1],
        ))

    return customers


def _get_ordered_something_customers_query_string(period_start: date, period_end: date, drug_id: Optional[int] = None, drug_type_id: Optional[int] = None) -> str:
    s1 = f"'{str(period_start).replace('-', '/')}'"
    s2 = f"'{str(period_end).replace('-', '/')}'"

    if drug_id is not None:
        return f"""
            select distinct
                customer_id
            from prescriptions_content
                join orders using (prescription_id)
            where
                (registration_datetime between {s1} and {s2})
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
                (registration_datetime between {s1} and {s2})
                and (drugs.type_id = {drug_type_id})
                and customer_id is not null
        """

    return f"""
        select distinct
            customer_id
        from prescriptions_content
            join orders using (prescription_id)
        where
            (registration_datetime between {s1} and {s2})
            and customer_id is not null
    """


def _get_frequent_customers_query_string(drug_id: Optional[int] = None,
                                         drug_type_id: Optional[int] = None) -> str:
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
