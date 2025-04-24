# UI.py
from flask import Blueprint, render_template, jsonify
import os, json

ui_bp = Blueprint('ui', __name__, template_folder='templates', static_folder='static')

# trả tiến độ "nở sen" (số dòng database.txt / mốc 100)
@ui_bp.route('/mandala/progress')
def mandala_progress():
    total = 0
    if os.path.exists('database.txt'):
        with open('database.txt', 'r', encoding='utf-8') as f:
            total = len(f.readlines())
    percent = min(total, 100)          # tối đa 100 cánh
    return jsonify({'percent': percent})

@ui_bp.route('/mandala')
def mandala():
    return render_template('UI.html')
