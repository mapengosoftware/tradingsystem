import asyncio
import os
from .parser.parser import parse_message
from .crud import save_raw_signal, save_parsed_signal, create_order, set_order_fxid
from .fxblue.client import FXBlueClient

SAMPLES_FILE = os.path.join(os.path.dirname(__file__), 'samples', 'messages.txt')

async def process_raw_message(raw_text:str):
    raw_payload = {'chat_id': 'demo_channel', 'raw_text': raw_text}
    signal_id = await save_raw_signal(raw_payload)
    parsed = parse_message(raw_text)
    await save_parsed_signal(signal_id, parsed)
    # simple: for each TP create an order and send to FXBlue mock
    fx = FXBlueClient()
    for tp in parsed.get('tps', []):
        order_id = await create_order(signal_id, parsed.get('symbol'), parsed.get('side'), parsed.get('volume'), tp, parsed.get('sl'))
        # place order
        resp = await fx.place_order(parsed.get('symbol') or 'EURUSD', parsed.get('side') or 'buy', parsed.get('volume'), parsed.get('sl'), tp, client_ref=str(order_id))
        # update with fx id
        await set_order_fxid(order_id, resp.get('order_id'))

async def start_sample_reader():
    # Reads the samples file periodically and processes each new line
    if not os.path.exists(SAMPLES_FILE):
        print('No samples file found at', SAMPLES_FILE)
        return
    seen = set()
    while True:
        with open(SAMPLES_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line in seen:
                    continue
                seen.add(line)
                try:
                    await process_raw_message(line)
                    print('Processed sample:', line)
                except Exception as e:
                    print('Error processing sample:', e)
        await asyncio.sleep(5)
