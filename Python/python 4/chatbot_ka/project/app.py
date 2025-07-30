from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = 'knowledge_data.json'
FAQ_FILE = 'knowledge_faq.json'

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/api/knowledge_data')
def api_knowledge_dynamic():
    with open(DATA_FILE) as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/knowledge_faq')
def api_knowledge_static():
    with open(FAQ_FILE) as f:
        data = json.load(f)
    return jsonify(data)

# Admin panel untuk dynamic knowledge (program, jam buka, dsb)
@app.route('/admin/program', methods=['GET', 'POST'])
def admin_program():
    with open(DATA_FILE) as f:
        data = json.load(f)
    if request.method == 'POST':
        # Hapus
        if 'delete' in request.form:
            idx = int(request.form['delete'])
            if 0 <= idx < len(data):
                data.pop(idx)
                with open(DATA_FILE, 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            return redirect(url_for('admin_program'))
        # Update/tambah
        questions = request.form.getlist('question')
        answers = request.form.getlist('answer')
        data = [{"question": q, "answer": a} for q, a in zip(questions, answers) if q and a]
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return redirect(url_for('admin_program'))
    return render_template('admin.html', data=data, tipe='Program / Jadwal', endpoint='admin_program')

# Admin panel untuk FAQ/Static knowledge
@app.route('/admin/faq', methods=['GET', 'POST'])
def admin_faq():
    with open(FAQ_FILE) as f:
        data = json.load(f)
    if request.method == 'POST':
        if 'delete' in request.form:
            idx = int(request.form['delete'])
            if 0 <= idx < len(data):
                data.pop(idx)
                with open(FAQ_FILE, 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            return redirect(url_for('admin_faq'))
        questions = request.form.getlist('question')
        answers = request.form.getlist('answer')
        data = [{"question": q, "answer": a} for q, a in zip(questions, answers) if q and a]
        with open(FAQ_FILE, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return redirect(url_for('admin_faq'))
    return render_template('admin.html', data=data, tipe='FAQ (Pertanyaan Umum)', endpoint='admin_faq')

if __name__ == '__main__':
    # Create files if doesn't exist
    for file in [DATA_FILE, FAQ_FILE]:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                json.dump([], f)
    app.run(debug=True, port=5000)
