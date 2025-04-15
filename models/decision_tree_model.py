import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from data.iris_data import load_iris_data
from utils.preprocessing import preprocess_data
from utils.logger import log

def train_model():
    data = load_iris_data()
    X, y = preprocess_data(data)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    joblib.dump(model, 'models/iris_model.pkl')
    
    log(f"Model trained with accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    train_model()
