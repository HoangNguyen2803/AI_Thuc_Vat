def preprocess_data(data):
    X = data.drop('target', axis=1)
    y = data['target']
    return X, y
