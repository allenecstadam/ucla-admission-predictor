

from sklearn.neural_network import MLPClassifier
import joblib



def train_and_save_model(X_train, y_train, model_path="models/admission_nn_model.pkl"):
    
        model = MLPClassifier(hidden_layer_sizes=(20, 20), max_iter=1000, random_state=42)
        model.fit(X_train, y_train)
        joblib.dump(model, model_path)

        return model

