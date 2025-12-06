from langdetect import detect
import re

TP_REGEX = re.compile(r"(tp\d?|take[-\s]?profit)\s*[:\-]?\s*([0-9\.,]+)", re.I)
SL_REGEX = re.compile(r"(sl|stop[-\s]?loss)\s*[:\-]?\s*([0-9\.,]+)", re.I)
SIDE_REGEX = re.compile(r"\b(buy|long|sell|short|comprar|vender|kopen|verkopen)\b", re.I)
SYMBOL_REGEX = re.compile(r"\b([A-Z]{3,6}(?:USD|JPY|EUR|GBP)?|[A-Z]{6})\b")

def normalize_num(s: str) -> float:
    return float(s.replace(',', '.'))

def find_symbol(text: str) -> str | None:
    m = SYMBOL_REGEX.search(text)
    if m:
        return m.group(0)
    return None

def parse_message(raw: str) -> dict:
    try:
        lang = detect(raw)
    except Exception:
        lang = "unknown"
    side_m = SIDE_REGEX.search(raw)
    sl_m = SL_REGEX.search(raw)
    tps = TP_REGEX.findall(raw)

    parsed = {
        "language": lang,
        "symbol": find_symbol(raw),
        "side": side_m.group(0) if side_m else None,
        "sl": normalize_num(sl_m.group(2)) if sl_m else None,
        "tps": [normalize_num(m[1]) for m in tps],
        "raw": raw,
    }
    # simple default volume
    parsed['volume'] = 0.1
    return parsed
