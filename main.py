from datetime import date
from typing import Optional

from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import (
    DrugOrm,
    DrugTypeOrm,
    PatientOrm,
    DoctorOrm,
    CustomerOrm,
    OrderOrm
)
from schemas import (
    FrequentCustomer,
    CustomerOrder,
    Customer,
    UsedDrug,
    Drug,
    DrugType,
    Doctor,
    Patient,
    Order,
    StoredDrug,
    TechnologyComponent,
    Technology,
    Prescription,
)
from schemas.responses import (
    CreateOrderResponse,
    BaseResponse
)

app = FastAPI()


@app.get("/orders")
async def get_orders(session: AsyncSession = Depends(get_session)) -> list[Order]:
    query = select(OrderOrm)
    result = await session.execute(query)
    return [Order.model_validate(i) for i in result.unique().scalars().all()]


@app.post("/orders")
async def create_order(prescription: Prescription) -> CreateOrderResponse:
    return CreateOrderResponse(is_customer_required=True, order_id=0)


@app.post("/orders/{order_id}/customers")
async def add_order_customer(order_id: int, customer: Customer) -> BaseResponse:
    return BaseResponse()


@app.post("/orders/{order_id}/pay")
async def add_order_customer() -> BaseResponse:
    return BaseResponse()


@app.post("/orders/{order_id}/obtain")
async def add_order_customer() -> BaseResponse:
    return BaseResponse()


@app.get("/drugs")
async def get_drugs(session: AsyncSession = Depends(get_session)) -> list[Drug]:
    query = select(DrugOrm)
    result = await session.execute(query)
    return [Drug.model_validate(i) for i in result.scalars().all()]


@app.get("/drug-types")
async def get_drug_types(session: AsyncSession = Depends(get_session)) -> list[DrugType]:
    query = select(DrugTypeOrm)
    result = await session.execute(query)
    return [DrugType.model_validate(i) for i in result.scalars().all()]


@app.get("/doctors")
async def get_doctors(session: AsyncSession = Depends(get_session)) -> list[Doctor]:
    query = select(DoctorOrm)
    result = await session.execute(query)
    return [Doctor.model_validate(i) for i in result.scalars().all()]


@app.get("/patients")
async def get_patients(session: AsyncSession = Depends(get_session)) -> list[Patient]:
    query = select(PatientOrm)
    result = await session.execute(query)
    return [Patient.model_validate(i) for i in result.scalars().all()]


@app.get("/customers")
async def get_customers(session: AsyncSession = Depends(get_session)) -> list[Customer]:
    query = select(CustomerOrm)
    result = await session.execute(query)
    return [Customer.model_validate(i) for i in result.scalars().all()]


@app.get("/forgotten-orders")
async def get_forgotten_orders() -> list[CustomerOrder]:
    return []


@app.get("/waiting-supplies-customers")
async def get_waiting_supplies_customers(drug_type_id: Optional[int] = None) -> list[Customer]:
    return []


@app.get("/popular-drugs")
async def get_popular_drugs(limit: int = 10, drug_type_id: Optional[int] = None) -> list[UsedDrug]:
    return []


@app.get("/used-drugs")
async def get_used_drugs(period_start: date, period_end: date) -> list[UsedDrug]:
    return []


@app.get("/ordered-something-customers")
async def get_ordered_something_customers(
        period_start: date, period_end: date, drug_id: Optional[int] = None, drug_type_id: Optional[int] = None
) -> list[Customer]:
    return []


@app.get("/critical-amount-drugs")
async def get_critical_amount_drugs() -> list[Drug]:
    return []


@app.get("/critical-amount-drug-types")
async def get_critical_amount_drug_types() -> list[DrugType]:
    return []


@app.get("/minimal-amount-drugs")
async def get_minimal_amount_drugs(drug_type_id: Optional[int] = None) -> list[StoredDrug]:
    return []


@app.get("/orders-in-production")
async def get_orders_in_production() -> list[Order]:
    return []


@app.get("/production-components")
async def get_production_components() -> list[TechnologyComponent]:
    return []


@app.get("/technologies")
async def get_technologies(
        drug_id: Optional[int] = None, drug_type_id: Optional[int] = None, in_production: bool = False
) -> list[Technology]:
    return []


@app.get("/frequent-customers")
async def get_frequent_customers(
        drug_id: Optional[int] = None, drug_type_id: Optional[int] = None
) -> list[FrequentCustomer]:
    return []
