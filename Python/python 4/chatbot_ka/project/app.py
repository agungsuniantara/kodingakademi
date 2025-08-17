from flask import Flask, jsonify, request, render_template, redirect, url_for
import json, os

app = Flask(__name__)

PROGRAMS_FILE = 'knowledge_data.json'  # program berbasis usia/lokasi
FAQ_FILE      = 'knowledge_faq.json'   # Q/A

# ---------- Helpers ----------
def ensure_files():
    for file, default in [
        (PROGRAMS_FILE, []),
        (FAQ_FILE, [])
    ]:
        if not os.path.exists(file):
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(default, f, ensure_ascii=False, indent=2)

def parse_locations(text):
    """
    Ubah string 'Denpasar=https://...; Surabaya=https://...' menjadi dict.
    """
    result = {}
    if not text:
        return result
    entries = [x.strip() for x in text.split(';') if x.strip()]
    for e in entries:
        if '=' in e:
            k, v = e.split('=', 1)
            k = k.strip()
            v = v.strip()
            if k and v:
                result[k] = v
    return result

# ---------- Public ----------
@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/api/programs')
@app.route('/api/knowledge_data')  # kompatibel dengan kode lama
def api_programs():
    with open(PROGRAMS_FILE, encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/knowledge_faq')
def api_faq():
    with open(FAQ_FILE, encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

# ---------- Admin: Programs ----------
@app.route('/admin/programs', methods=['GET', 'POST'])
def admin_programs():
    with open(PROGRAMS_FILE, encoding='utf-8') as f:
        data = json.load(f)

    if request.method == 'POST':
        # Hapus baris
        if 'delete' in request.form:
            idx = int(request.form['delete'])
            if 0 <= idx < len(data):
                data.pop(idx)
                with open(PROGRAMS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            return redirect(url_for('admin_programs'))

        # Simpan semua dari form
        names        = request.form.getlist('name')
        categories   = request.form.getlist('category')
        min_ages     = request.form.getlist('min_age')
        max_ages     = request.form.getlist('max_age')
        descriptions = request.form.getlist('description')
        videos       = request.form.getlist('video')
        locations_s  = request.form.getlist('locations')

        newdata = []
        for i in range(len(names)):
            name = (names[i] or "").strip()
            category = (categories[i] or "").strip()
            if not name:
                continue

            # min/max age
            try:
                min_age = int(min_ages[i]) if min_ages[i] != "" else None
            except:
                min_age = None
            try:
                max_age = int(max_ages[i]) if max_ages[i] != "" else None
            except:
                max_age = None

            desc  = (descriptions[i] or "").strip() if i < len(descriptions) else ""
            video = (videos[i] or "").strip() if i < len(videos) else ""
            locs  = parse_locations(locations_s[i]) if i < len(locations_s) else {}

            newdata.append({
                "name": name,
                "category": category,
                "min_age": min_age,
                "max_age": max_age,
                "description": desc,
                "video": video if video else None,
                "locations": locs
            })

        with open(PROGRAMS_FILE, 'w', encoding='utf-8') as f:
            json.dump(newdata, f, ensure_ascii=False, indent=2)
        return redirect(url_for('admin_programs'))

    return render_template('admin.html', data=data, tipe='Program (Usia/Lokasi)', endpoint='admin_programs')

# ---------- Admin: FAQ ----------
@app.route('/admin/faq', methods=['GET', 'POST'])
def admin_faq():
    with open(FAQ_FILE, encoding='utf-8') as f:
        data = json.load(f)

    if request.method == 'POST':
        if 'delete' in request.form:
            idx = int(request.form['delete'])
            if 0 <= idx < len(data):
                data.pop(idx)
                with open(FAQ_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            return redirect(url_for('admin_faq'))

        questions = request.form.getlist('question')
        answers   = request.form.getlist('answer')
        newdata = [{"question": (q or "").strip(), "answer": (a or "").strip()}
                   for q, a in zip(questions, answers) if (q or "").strip() and (a or "").strip()]

        with open(FAQ_FILE, 'w', encoding='utf-8') as f:
            json.dump(newdata, f, ensure_ascii=False, indent=2)
        return redirect(url_for('admin_faq'))

    return render_template('admin.html', data=data, tipe='FAQ (Pertanyaan Umum)', endpoint='admin_faq')

# ---------- MAIN ----------
if __name__ == '__main__':
    ensure_files()
    app.run(debug=True, port=5000)
