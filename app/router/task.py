from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.amqp.producer import ProducerService
from app.cache.locker import LockerService
from app.model.request_model import TaskCreate

router = APIRouter()
locker = LockerService()
producer = ProducerService()


@router.post(
    "/create",
    status_code=status.HTTP_200_OK,
)
def create(payload: TaskCreate):
    locker_response = locker.lock(payload.key)
    if isinstance(locker_response, JSONResponse):
        return locker_response

    producer_response = producer.create_publish(payload)
    if isinstance(producer_response, JSONResponse):
        return producer_response

    return {"success": True}
