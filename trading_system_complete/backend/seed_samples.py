import os, shutil
from backend import __file__ as _init
from pathlib import Path
base = Path(__file__).parent / 'backend' / 'samples'
base.mkdir(parents=True, exist_ok=True)
sample = base / 'messages.txt'
if not sample.exists():
    sample.write_text('BUY EURUSD TP1:1.1050 TP2:1.1100 SL:1.0980\nSELL GBPUSD tp1 1.2550 sl 1.2610\n')
print('Samples written to', sample)
