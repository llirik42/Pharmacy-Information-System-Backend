from fastapi import FastAPI

import routing.customers
import routing.doctors
import routing.drug_types
import routing.drugs
import routing.orders
import routing.patients
import routing.production
import routing.technologies

app = FastAPI()
app.include_router(routing.orders.router)
app.include_router(routing.customers.router)
app.include_router(routing.drugs.router)
app.include_router(routing.drug_types.router)
app.include_router(routing.doctors.router)
app.include_router(routing.patients.router)
app.include_router(routing.technologies.router)
app.include_router(routing.production.router)
