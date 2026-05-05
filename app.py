from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy database
bookings = []

@app.route("/book", methods=["POST"])
def book_car():
    data = request.json

    name = data.get("name")
    car = data.get("car")
    days = data.get("days")
    amount = data.get("amount")

    if not name or not car:
        return jsonify({"message": "Invalid Data"}), 400

    booking = {
        "name": name,
        "car": car,
        "days": days,
        "amount": amount
    }

    bookings.append(booking)

    return jsonify({
        "message": "Booking Saved Successfully",
        "data": booking
    })

@app.route("/pay", methods=["POST"])
def payment():
    data = request.json

    aadhaar = data.get("aadhaar")
    license = data.get("license")

    if len(aadhaar) != 12:
        return jsonify({"message": "Invalid Aadhaar"}), 400

    return jsonify({
        "message": "Payment Successful"
    })

if __name__ == "__main__":
    app.run(debug=True)