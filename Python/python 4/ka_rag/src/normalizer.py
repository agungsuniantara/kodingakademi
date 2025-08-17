# src/normalizer.py
import re

def soft_lower(text: str) -> str:
    # biarkan URL & kode tetap, tapi turunkan huruf lain
    def repl(m):
        s = m.group(0)
        if s.startswith(("http://","https://","taplink.","bit.ly")): return s
        return s.lower()
    return re.sub(r'(https?://\S+|taplink\.\S+|bit\.ly/\S+)', repl, text, flags=re.IGNORECASE)

def strip_formatting(text: str) -> str:
    # buang markdown ringan & emoji umum untuk keperluan embedding
    t = re.sub(r'[*_`~>#+-]', ' ', text)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def build_search_text(q: str, a: str) -> str:
    qn = strip_formatting(soft_lower(q))
    an = strip_formatting(soft_lower(a))
    return f"{qn} {an}"
