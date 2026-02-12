from flask import Flask, render_template, request, jsonify
from nlp.preprocessing import preprocess
from intent.intent_detector_ml import predict_intent
from router.agent_router import route_agent

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    intent = predict_intent(user_input)
    agent = route_agent(intent)
    response = agent.respond()

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
