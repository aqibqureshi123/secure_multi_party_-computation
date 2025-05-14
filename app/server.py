from flask import Flask, request, render_template, jsonify
from logic import submit_share, compute_result
import ssl
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    party_id = data.get('party_id')
    share = int(data.get('share'))
    submit_share(party_id, share)
    return jsonify({"message": f"Share received from {party_id}."})

@app.route('/compute')
def compute():
    result = compute_result()
    if result is None:
        return jsonify({"error": "Not enough shares yet"})
    return jsonify({"result": result})

if __name__ == '__main__':
    # Path to SSL certificate and key (use real domain & Let's Encrypt in production)
    cert_path = os.path.join('certs', 'cert.pem')
    key_path = os.path.join('certs', 'key.pem')

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)

    app.run(host='0.0.0.0', port=5000, ssl_context=context)

