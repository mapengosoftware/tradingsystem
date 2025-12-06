import os
import httpx

class FXBlueClient:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.getenv('FXBLUE_BASE_URL', 'http://localhost:8000/fxblue')
        self.client = httpx.AsyncClient(timeout=10)

    async def place_order(self, symbol: str, side: str, volume: float, sl: float = None, tp: float | None = None, client_ref: str | None = None):
        payload = {
            'symbol': symbol,
            'side': side,
            'volume': volume,
            'sl': sl,
            'tp': tp,
            'client_ref': client_ref
        }
        resp = await self.client.post(f'{self.base_url}/place', json=payload)
        resp.raise_for_status()
        return resp.json()
