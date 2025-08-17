# admin/app.py
from flask import Flask, jsonify, request, render_template, redirect, url_for
import json, os, requests, tempfile, shutil

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
FAQ_FILE = os.path.join(DATA_DIR, "knowledge_faq.json")
DATA_FILE = os.path.join(DATA_DIR, "knowledge_data.json")

def write_json_atomic(path, data_obj):
    # tulis aman: ke file tmp lalu atomically replace
    fd, tmp_path = tempfile.mkstemp(dir=DATA_DIR, prefix=".tmp_", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data_obj, f, ensure_ascii=False, indent=2)
        shutil.move(tmp_path, path)
    finally:
        try:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        except Exception:
            pass

# ===== Views landing =====
@app.route("/")
def home():
    return render_template("landing.html")

# ===== API JSON =====
@app.route("/api/knowledge_faq")
def api_faq():
    with open(FAQ_FILE, encoding="utf-8") as f:
        return jsonify(json.load(f))

@app.route("/api/knowledge_data")
def api_data():
    with open(DATA_FILE, encoding="utf-8") as f:
        return jsonify(json.load(f))

# ===== Admin FAQ =====
@app.route("/admin/faq", methods=["GET","POST"])
def admin_faq():
    with open(FAQ_FILE, encoding="utf-8") as f:
        data = json.load(f)

    if request.method == "POST":
        if 'delete' in request.form:
            idx = int(request.form['delete'])
            if 0 <= idx < len(data):
                data.pop(idx)
        else:
            qs = request.form.getlist("question")
            ans = request.form.getlist("answer")
            data = [{"question": q.strip(), "answer": a.strip()} for q,a in zip(qs, ans) if q.strip() and a.strip()]

        write_json_atomic(FAQ_FILE, data)
        try:
            requests.post("http://127.0.0.1:8001/admin/rebuild", timeout=2)
        except Exception:
            pass
        return redirect(url_for("admin_faq"))

    return render_template("admin_faq.html", data=data)

# ===== Admin Program/Jadwal =====
@app.route("/admin/program", methods=["GET", "POST"])
def admin_program():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    if request.method == "POST":
        if 'delete' in request.form:
            idx = int(request.form['delete'])
            if 0 <= idx < len(data):
                data.pop(idx)
        else:
            types    = request.form.getlist("type")
            titles   = request.form.getlist("title")
            ages     = request.form.getlist("age_range")
            cities   = request.form.getlist("city")
            links_ts = request.form.getlist("links")
            sums     = request.form.getlist("summary")

            new_data = []
            for i in range(len(titles)):
                title = (titles[i] or "").strip()
                summary = (sums[i] or "").strip()
                if not title and not summary:
                    continue
                links = [ln.strip() for ln in (links_ts[i] or "").splitlines() if ln.strip()]
                new_data.append({
                    "type": (types[i] or "program").strip() or "program",
                    "title": title,
                    "age_range": (ages[i] or "").strip(),
                    "city": (cities[i] or "").strip(),
                    "links": links,
                    "summary": summary,
                })
            data = new_data

        write_json_atomic(DATA_FILE, data)
        try:
            requests.post("http://127.0.0.1:8001/admin/rebuild", timeout=2)
        except Exception:
            pass
        return redirect(url_for("admin_program"))

    return render_template("admin_program.html", data=data)

if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    for fpath in [FAQ_FILE, DATA_FILE]:
        if not os.path.exists(fpath):
            with open(fpath, "w", encoding="utf-8") as w:
                json.dump([], w)
    app.run(host="0.0.0.0", port=5001, debug=True)
