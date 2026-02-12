import pickle

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model/intent_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_intent(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    print("DEBUG Intent:", prediction)
    return prediction
