from flask import render_template, request
from backend.predictor import predict_crop


def init_routes(app):

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/predict")
    def predict_page():
        return render_template("predict.html")

    @app.route("/predict", methods=["POST"])
    def predict():

        # Get user input from the form
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Predict crop
        crop = predict_crop(
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        )

        return render_template(
            "result.html",
            prediction_text=f"🌱 Recommended Crop: {crop}"
        )