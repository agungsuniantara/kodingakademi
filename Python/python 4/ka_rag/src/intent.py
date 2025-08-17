# src/intent.py
import re
from typing import Optional, Tuple
from .metadata import parse_city

def extract_greeting(q: str) -> Optional[str]:
    s = q.lower()
    if "selamat pagi" in s: return "Selamat pagi"
    if "selamat siang" in s: return "Selamat siang"
    if "selamat sore" in s: return "Selamat sore"
    if "selamat malam" in s: return "Selamat malam"
    if s.strip() in ["halo","hai","hi","hello"]: return "Halo"
    return None

def extract_age(q: str) -> Tuple[Optional[int], Optional[int]]:
    q = q.lower()
    m = re.search(r'(\d+)\s*[-–]\s*(\d+)', q)
    if m: 
        a,b = int(m.group(1)), int(m.group(2))
        return (min(a,b), max(a,b))
    m = re.search(r'(\d+)\s*\+', q)
    if m: 
        a = int(m.group(1)); return (a, 100)
    m = re.search(r'\b(\d{1,2})\b', q)
    if m: 
        a = int(m.group(1)); return (a,a)
    return (None,None)

def extract_topic(q: str) -> str:
    s = q.lower()
    if "alamat" in s or "dimana" in s or "di mana" in s: return "address"
    if "program" in s or "kelas" in s: return "program"
    if "harga" in s or "biaya" in s: return "price"
    return "general"

def parse_filters(q: str):
    age_min, age_max = extract_age(q)
    city = parse_city(q)
    return {"age_min": age_min, "age_max": age_max, "city": city}
