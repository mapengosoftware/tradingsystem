from .db import database
from .db_models import signals, orders
import datetime
import json

async def save_raw_signal(raw_payload: dict):
    query = signals.insert().values(chat_id=raw_payload.get('chat_id'), raw=raw_payload.get('raw_text'), parsed=None, status='raw')
    row_id = await database.execute(query)
    return row_id

async def save_parsed_signal(signal_id:int, parsed: dict):
    query = signals.update().where(signals.c.id==signal_id).values(parsed=parsed, status='parsed')
    await database.execute(query)

async def create_order(signal_id:int, symbol:str, side:str, volume:float, tp:float, sl:float):
    query = orders.insert().values(signal_id=signal_id, symbol=symbol, side=side, volume=volume, tp=tp, sl=sl, status='pending')
    order_id = await database.execute(query)
    return order_id

async def set_order_fxid(order_id:int, fx_id:str):
    query = orders.update().where(orders.c.id==order_id).values(fx_id=fx_id, status='open')
    await database.execute(query)

async def list_signals(limit=100):
    query = signals.select().order_by(signals.c.created_at.desc()).limit(limit)
    return await database.fetch_all(query)

async def list_orders(limit=100):
    query = orders.select().order_by(orders.c.created_at.desc()).limit(limit)
    return await database.fetch_all(query)
