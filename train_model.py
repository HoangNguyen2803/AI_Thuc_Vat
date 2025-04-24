from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import os

# Load dữ liệu Iris
X, y = load_iris(return_X_y=True)

# Chia dữ liệu train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Khởi tạo và huấn luyện mô hình
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Tạo thư mục models nếu chưa có
os.makedirs("models", exist_ok=True)

# Lưu mô hình vào file
with open('models/iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Mô hình đã được huấn luyện và lưu tại 'models/iris_model.pkl'")