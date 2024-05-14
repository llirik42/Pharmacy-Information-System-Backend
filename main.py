from datetime import date
from typing import Optional

from fastapi import FastAPI

from schemas import (FrequentCustomer, CustomerOrder, Customer, UsedDrug, Drug, DrugType, Doctor, Patient, Order,
                     StoredDrug, TechnologyComponent, Technology)

app = FastAPI()


@app.get('/drugs')
async def get_drugs() -> list[Drug]:
    return []


@app.get('/drug-types')
async def get_drug_types() -> list[DrugType]:
    return []


@app.get('/doctors')
async def get_doctors() -> list[Doctor]:
    return []


@app.get('/patients')
async def get_patients() -> list[Patient]:
    return []


@app.get('/customers')
async def get_customers() -> list[Customer]:
    return []


@app.get('/forgotten-orders')
async def get_forgotten_orders() -> list[CustomerOrder]:
    return []


@app.get('/waiting-supplies-customers')
async def get_waiting_supplies_customers(
        drug_type_id: Optional[int] = None) -> list[Customer]:
    return []


@app.get('/popular-drugs')
async def get_popular_drugs(
        limit: int = 10,
        drug_type_id: Optional[int] = None) -> list[UsedDrug]:
    return []


@app.get('/used-drugs')
async def get_used_drugs(
        period_start: date,
        period_end: date) -> list[UsedDrug]:
    return []


@app.get('/ordered-something-customers')
async def get_ordered_something_customers(
        period_start: date,
        period_end: date,
        drug_id: Optional[int] = None,
        drug_type_id: Optional[int] = None) -> list[Customer]:
    return []


@app.get('/critical-amount-drugs')
async def get_critical_amount_drugs() -> list[Drug]:
    return []


@app.get('/critical-amount-drug-types')
async def get_critical_amount_drug_types() -> list[DrugType]:
    return []


@app.get('/minimal-amount-drugs')
async def get_minimal_amount_drugs(
        drug_type_id: Optional[int] = None) -> list[StoredDrug]:
    return []


@app.get('/orders-in-production')
async def get_orders_in_production() -> list[Order]:
    return []


@app.get('/production-components')
async def get_production_components() -> list[TechnologyComponent]:
    return []


@app.get('/technologies')
async def get_technologies(
        drug_id: Optional[int] = None,
        drug_type_id: Optional[int] = None,
        in_production: bool = False) -> list[Technology]:
    return []


@app.get('/frequent-customers')
async def get_frequent_customers(
        drug_id: Optional[int] = None,
        drug_type_id: Optional[int] = None) -> list[FrequentCustomer]:
    return []
