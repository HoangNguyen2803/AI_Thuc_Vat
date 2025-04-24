# dayAI.py
import numpy as np

def predict_from_database(features):
    try:
        with open("database.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            return "❌ Không có dữ liệu trong database."

        min_distance = float('inf')
        predicted_name = "❌ Không xác định"

        for line in lines:
            parts = line.strip().split(',')
            if len(parts) != 5:
                continue

            name = parts[0]
            try:
                data_features = list(map(float, parts[1:]))
                distance = np.linalg.norm(np.array(features) - np.array(data_features))
                if distance < min_distance:
                    min_distance = distance
                    predicted_name = name
            except:
                continue

        return f"🌸 Dự đoán gần đúng nhất: {predicted_name}"
    except Exception as e:
        return f"❌ Lỗi khi đoán từ cơ sở dữ liệu: {str(e)}"