# src/metadata.py
import re
from typing import Optional, Tuple, List

CITIES = ["denpasar","gianyar","surabaya","jakarta","bandung","bali"]

def parse_age(text: str) -> Tuple[Optional[int], Optional[int]]:
    t = text.lower()
    # 7 - 10
    m = re.search(r'(\d+)\s*[-–]\s*(\d+)', t)
    if m:
        a,b = int(m.group(1)), int(m.group(2))
        return (min(a,b), max(a,b))
    # 7+ / usia 7+
    m = re.search(r'(\d+)\s*\+', t)
    if m:
        a = int(m.group(1))
        return (a, 100)
    # angka tunggal
    m = re.search(r'\b(\d{1,2})\b', t)
    if m:
        a = int(m.group(1))
        return (a, a)
    return (None, None)

def parse_city(text: str) -> Optional[str]:
    t = text.lower()
    for c in CITIES:
        if c in t: return c
    return None

def extract_links(text: str) -> List[str]:
    return re.findall(r'(https?://\S+|taplink\.\S+|bit\.ly/\S+)', text, flags=re.IGNORECASE)

def age_overlap(qmin,qmax, dmin,dmax) -> bool:
    if qmin is None and qmax is None: return True
    if dmin is None and dmax is None: return True
    if qmin is None: qmin = dmin
    if qmax is None: qmax = dmax
    return not (qmax < dmin or qmin > dmax)
