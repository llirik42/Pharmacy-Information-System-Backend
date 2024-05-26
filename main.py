import logging.config
from contextlib import asynccontextmanager
from typing import Optional

import starlette
import starlette.datastructures
from fastapi import FastAPI
from sqladmin import Admin
from starlette.requests import Request

import routing.customers
import routing.doctors
import routing.drug_types
import routing.drugs
import routing.orders
import routing.patients
import routing.production
import routing.technologies
import routing.prescriptions
from admin import (
    AdministrationRouteView,
    DrugTypeView,
    MixtureTypeView,
    CustomerView,
    DoctorView,
    LabWorkerView,
    PatientView,
    DrugView,
    MixtureView,
    TinctureView,
    PillView,
    PowderView,
    SalveView,
    SolutionView,
    DrugTypeAdministrationRouteView,
    PrescriptionView,
    OrderView,
    StorageItemView,
    SupplierView,
    SupplyView,
    TechnologyView,
    PrescriptionItemView,
    ProductionView,
    OrderWaitingDrugSupplyView,
    ReservedDrugView,
    ProductionLabWorkerView,
    TechnologyComponentView,
)
from db import engine


@asynccontextmanager
async def lifespan(app_: FastAPI):
    root_logger.info("Application is launched")

    yield

    root_logger.info("Application is shutting down")
    await engine.dispose()


logging.config.fileConfig(fname="logging.ini")

root_logger = logging.getLogger("root")
controller_logger = logging.getLogger("controller")

app = FastAPI(separate_input_output_schemas=False, lifespan=lifespan)
app.include_router(routing.orders.router)
app.include_router(routing.customers.router)
app.include_router(routing.drugs.router)
app.include_router(routing.drug_types.router)
app.include_router(routing.doctors.router)
app.include_router(routing.patients.router)
app.include_router(routing.technologies.router)
app.include_router(routing.production.router)
app.include_router(routing.prescriptions.router)

admin = Admin(app=app, engine=engine)
admin.add_model_view(AdministrationRouteView)
admin.add_model_view(DrugTypeView)
admin.add_model_view(MixtureTypeView)
admin.add_model_view(CustomerView)
admin.add_model_view(DoctorView)
admin.add_model_view(LabWorkerView)
admin.add_model_view(PatientView)
admin.add_model_view(SupplierView)
admin.add_model_view(DrugView)
admin.add_model_view(MixtureView)
admin.add_model_view(TinctureView)
admin.add_model_view(PillView)
admin.add_model_view(PowderView)
admin.add_model_view(SalveView)
admin.add_model_view(SolutionView)
admin.add_model_view(DrugTypeAdministrationRouteView)
admin.add_model_view(PrescriptionView)
admin.add_model_view(OrderView)
admin.add_model_view(StorageItemView)
admin.add_model_view(SupplyView)
admin.add_model_view(TechnologyView)
admin.add_model_view(PrescriptionItemView)
admin.add_model_view(ProductionView)
admin.add_model_view(OrderWaitingDrugSupplyView)
admin.add_model_view(ReservedDrugView)
admin.add_model_view(ProductionLabWorkerView)
admin.add_model_view(TechnologyComponentView)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    client: Optional[starlette.datastructures.Address] = request.client

    controller_logger.info(
        f"Received %s %s from %s:%s",
        request.method,
        request.url,
        None if client is None else client.host,
        None if client is None else client.port,
    )

    result = await call_next(request)
    controller_logger.info("Returning %s for %s", result.status_code, request.url)

    return result
