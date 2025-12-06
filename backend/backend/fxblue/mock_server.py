from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
import uuid
router = APIRouter()

class PlaceOrder(BaseModel):
    symbol: str
    side: str
    volume: float
    sl: float | None = None
    tp: float | None = None
    client_ref: str | None = None

@router.post('/place')
async def place(order: PlaceOrder):
    # Simulate acceptance and return an order id
    return {'status':'ok', 'order_id': str(uuid.uuid4()), 'received': order.dict()}

def create_mock_app():
    app = FastAPI(title='FXBlue Mock')
    app.include_router(router, prefix='/fxblue')
    return app
