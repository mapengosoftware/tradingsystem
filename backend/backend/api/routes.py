from fastapi import APIRouter
from ..crud import list_signals, list_orders
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get('/signals')
async def signals():
    s = await list_signals()
    return JSONResponse({'signals': [dict(x) for x in s]})

@router.get('/orders')
async def orders():
    o = await list_orders()
    return JSONResponse({'orders': [dict(x) for x in o]})
