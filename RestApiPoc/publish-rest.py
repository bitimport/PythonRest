from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', '')
    if not name:
        return jsonify({"error": "Name parameter is required"}), 400
    letters = len(name)
    unique_letters = len(set(name))
    response_message = f"your name has {unique_letters} number of unique letters"
    return jsonify({"name": name, "message": response_message, "letters": letters, "unique_letters": unique_letters}), 300

if __name__ == '__main__':
    app.run(debug=True)