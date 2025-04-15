from sklearn.datasets import load_iris
import pandas as pd # type: ignore

def load_iris_data():
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    return data
