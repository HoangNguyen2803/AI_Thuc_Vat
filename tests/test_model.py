from models import decision_tree_model

def test_model_training():
    try:
        decision_tree_model.train_model()
        print("✅ Model training test passed.")
    except Exception as e:
        print(f"❌ Model training test failed: {e}")