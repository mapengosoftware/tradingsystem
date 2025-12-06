from sqlalchemy import Table, Column, Integer, String, JSON, DateTime, Float, MetaData, ForeignKey
from sqlalchemy.sql import func
from .db import metadata

signals = Table(
    'signals', metadata,
    Column('id', Integer, primary_key=True),
    Column('chat_id', String, nullable=True),
    Column('raw', String, nullable=False),
    Column('parsed', JSON),
    Column('status', String, default='new'),
    Column('created_at', DateTime, server_default=func.now()),
)

orders = Table(
    'orders', metadata,
    Column('id', Integer, primary_key=True),
    Column('signal_id', Integer, ForeignKey('signals.id')),
    Column('symbol', String),
    Column('side', String),
    Column('volume', Float),
    Column('tp', Float),
    Column('sl', Float),
    Column('status', String, default='pending'),
    Column('fx_id', String, nullable=True),
    Column('created_at', DateTime, server_default=func.now()),
)
