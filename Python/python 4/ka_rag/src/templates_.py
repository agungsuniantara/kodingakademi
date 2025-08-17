# src/templates_.py
def greet_line(greet: str) -> str:
    return f"{greet}!"

def format_program_item(m):
    links = " ".join(m.get("links") or [])
    age = ""
    if m["age_min"] or m["age_max"]:
        lo = m["age_min"] if m["age_min"] else ""
        hi = m["age_max"] if m["age_max"] not in (None,100) else "+"
        if lo and hi == "+": age = f"(usia {lo}+)"
        elif lo and hi: age = f"(usia {lo}-{hi})"
    city = f" • {m['city'].title()}" if m.get("city") else ""
    return f"- {m['question']} {age}{city}\n  {m['answer']}\n  {links}".strip()

def format_program_list(items):
    return "\n".join([format_program_item(m) for m in items])

def address_answer(city_meta, city_name):
    # city_meta: list meta item yang memuat alamat
    if not city_meta:
        return f"Alamat cabang {city_name.title()} belum tersedia di data."
    # ambil jawaban paling masuk akal (pertama)
    m = city_meta[0]
    return m["answer"]
