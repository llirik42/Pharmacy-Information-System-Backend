from fastapi import FastAPI
from sqlalchemy import select

from db import new_session
from models import DoctorOrm
from schemas import Doctor

app = FastAPI()


@app.get('/doctors')
async def get_doctors() -> list[Doctor]:
    async with new_session() as session:
        query = select(DoctorOrm)
        result = await session.execute(query)
        return [Doctor.model_validate(obj) for obj in result.scalars().all()]
