from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory data store
users = {
    "1": {"name": "Osman Abdi", "balance": 1000.0},
    "2": {"name": "Warsame Fraha", "balance": 500.0}
}

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    sender_id = data["sender_id"]
    receiver_id = data["receiver_id"]
    amount = data["amount"]

    if sender_id not in users or receiver_id not in users:
        return jsonify({"error": "Invalid user ID"}), 400

    sender_balance = users[sender_id]["balance"]
    if amount > sender_balance:
        return jsonify({"error": "Insufficient balance"}), 400

    users[sender_id]["balance"] -= amount
    users[receiver_id]["balance"] += amount

    return jsonify({"message": "Transfer successful"}), 200

@app.route("/balance", methods=["GET"])
def balance():
    user_id = request.args.get("user_id")
    if user_id not in users:
        return jsonify({"error": "Invalid user ID"}), 400

    return jsonify({"balance": users[user_id]["balance"]}), 200

if __name__ == "__main__":
    app.run(debug=True)

