from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import subprocess
import pickle
import sys

app = Flask(__name__)

# Load mô hình AI
with open('models/iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

# ====== TRANG CHỦ ======
@app.route('/')
def home():  # ✅ Đặt tên là 'home' để tương thích với url_for('home')
    return render_template('index.html')

# ====== DỰ ĐOÁN HOA ======
@app.route('/predict', methods=['POST'])
def predict():
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        data = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(data)[0]

        flower_name_vn = "Không tìm thấy"
        with open('database.txt', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0].strip().lower() == prediction.lower():
                    flower_name_vn = parts[1]
                    break

        return render_template('index.html',
                               prediction=prediction,
                               flower_name_vn=flower_name_vn,
                               sepal_length=sepal_length,
                               sepal_width=sepal_width,
                               petal_length=petal_length,
                               petal_width=petal_width)
    except Exception as e:
        return render_template('index.html', error=str(e))

# ====== DẠY AI ======
@app.route('/dayAI', methods=['GET', 'POST'])
def dayAI():
    if request.method == 'POST':
        tenhoa = request.form['tenhoa']
        tentiengviet = request.form['tentiengviet']
        sepal_length = request.form['sepal_length']
        sepal_width = request.form['sepal_width']
        petal_length = request.form['petal_length']
        petal_width = request.form['petal_width']
        new_data = f"{tenhoa},{tentiengviet},{sepal_length},{sepal_width},{petal_length},{petal_width}\n"
        with open('database.txt', 'a', encoding='utf-8') as file:
            file.write(new_data)
        return redirect(url_for('danhsachdadayAI'))
    return render_template('dayAI.html')

# ====== DANH SÁCH ĐÃ DẠY AI ======
@app.route('/danhsachdadayAI', methods=['GET', 'POST'])
def danhsachdadayAI():
    if request.method == 'POST':
        action = request.form['action']
        index = int(request.form['index'])
        with open('database.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if action == 'save':
            new_line = f"{request.form['tenhoa']},{request.form['tentiengviet']},{request.form['sepal_length']},{request.form['sepal_width']},{request.form['petal_length']},{request.form['petal_width']}\n"
            lines[index] = new_line
        elif action == 'delete':
            lines.pop(index)
        elif action == 'add':
            new_line = f"{request.form['tenhoa']},{request.form['tentiengviet']},{request.form['sepal_length']},{request.form['sepal_width']},{request.form['petal_length']},{request.form['petal_width']}\n"
            lines.append(new_line)
        with open('database.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)
    with open('database.txt', 'r', encoding='utf-8') as file:
        data = [line.strip().split(',') for line in file.readlines()]
    return render_template('danhsachdadayAI.html', data=data)

# ====== BÁCH KHOA VỀ HOA ======
@app.route('/bachkhoavehoa')
def bachkhoavehoa():
    with open('database.txt', 'r', encoding='utf-8') as file:
        data = [line.strip().split(',') for line in file.readlines()]
    return render_template('bachkhoavehoa.html', data=data)

# ====== GIỚI THIỆU VỀ AI HANA ======
@app.route('/gioithieu')
def gioithieu():
    return render_template('gioithieu.html')

# ====== GÓP Ý ======
@app.route('/gopy', methods=['GET', 'POST'])
def gopy():
    if request.method == 'POST':
        noidung = request.form['noidung']
        with open('gopy.txt', 'a', encoding='utf-8') as file:
            file.write(noidung + '\n')
        return render_template('camon.html')
    return render_template('gopy.html')

@app.route('/hienthigopy', methods=['GET', 'POST'])
def hienthigopy():
    if request.method == 'POST':
        action = request.form['action']
        index = int(request.form['index'])
        with open('gopy.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if action == 'edit':
            lines[index] = request.form['noidung'] + '\n'
        elif action == 'delete':
            with open('gopy_history.txt', 'a', encoding='utf-8') as hist:
                hist.write("XÓA: " + lines[index])
            lines.pop(index)
        with open('gopy.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)
    with open('gopy.txt', 'r', encoding='utf-8') as file:
        gopy_data = [line.strip() for line in file.readlines()]
    return render_template('hienthigopy.html', gopy_data=gopy_data)

# ====== BÁCH KHOA VỀ CÂY ======
@app.route('/bachkhoavecay')
def bachkhoavecay():
    with open('cay.txt', 'r', encoding='utf-8') as file:
        cay_data = [line.strip().split(',') for line in file]
    return render_template('bachkhoavecay.html', cay_data=cay_data)

@app.route('/api/cay', methods=['POST'])
def add_cay():
    data = request.json
    with open('cay.txt', 'a', encoding='utf-8') as file:
        file.write(f"{data['ten']},{data['mota']},{data['hinh']}\n")
    return jsonify({'message': 'Đã thêm cây'})

@app.route('/api/sua_cay', methods=['POST'])
def sua_cay():
    data = request.json
    index = int(data['index'])
    with open('cay.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines[index] = f"{data['ten']},{data['mota']},{data['hinh']}\n"
    with open('cay.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)
    return jsonify({'message': 'Đã sửa cây'})

@app.route('/api/xoa_cay', methods=['POST'])
def xoa_cay():
    data = request.json
    index = int(data['index'])
    with open('cay.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines.pop(index)
    with open('cay.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)
    return jsonify({'message': 'Đã xoá cây'})

# ====== CHẠY C++ ======
@app.route('/nangcapAI_cpp')
def nangcapAI_cpp():
    path = 'nangcapAI/nangcap.cpp'
    try:
        subprocess.check_output(['g++', path, '-o', 'nangcapAI/nangcap.out'], stderr=subprocess.STDOUT)
        result = subprocess.check_output(['nangcapAI/nangcap.out'], stderr=subprocess.STDOUT)
        try:
            result = result.decode('utf-8')
        except UnicodeDecodeError:
            result = result.decode('ISO-8859-1')
    except subprocess.CalledProcessError as e:
        try:
            error_message = e.output.decode('utf-8')
        except UnicodeDecodeError:
            error_message = e.output.decode('ISO-8859-1')
        result = f"❌ Lỗi biên dịch hoặc chạy C++: {error_message}"
    
    return render_template('run_output.html', result=result, language='C++')

# ====== CHẠY JAVA ======
@app.route('/nangcapAI_java')
def nangcapAI_java():
    path = 'nangcapAI/nangcap.java'
    try:
        subprocess.check_output(['javac', path], stderr=subprocess.STDOUT)
        result = subprocess.check_output(['java', '-cp', 'nangcapAI', 'nangcap'], stderr=subprocess.STDOUT)
        try:
            result = result.decode('utf-8')
        except UnicodeDecodeError:
            result = result.decode('ISO-8859-1')
    except subprocess.CalledProcessError as e:
        try:
            error_message = e.output.decode('utf-8')
        except UnicodeDecodeError:
            error_message = e.output.decode('ISO-8859-1')
        result = f"❌ Lỗi biên dịch hoặc chạy Java: {error_message}"
    
    return render_template('run_output.html', result=result, language='Java')

# ====== CHẠY APP ======
if __name__ == '__main__':
    app.run(debug=True)
