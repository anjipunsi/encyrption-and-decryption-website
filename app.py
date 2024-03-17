from flask import Flask, render_template, request, jsonify
from transposition_cipher import TranspositionCipher

app = Flask(__name__)
cipher = TranspositionCipher(4)  # Use your desired key here

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    message = data.get("message")
    encrypted_message = cipher.encrypt(message)
    return jsonify({"encrypted_message": encrypted_message})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    encrypted_message = data.get("encrypted_message")
    decrypted_message = cipher.decrypt(encrypted_message)
    return jsonify({"decrypted_message": decrypted_message})

if __name__ == "__main__":
    app.run(debug=True)
