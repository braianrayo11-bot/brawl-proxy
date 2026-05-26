from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("BRAWL_TOKEN", "")

@app.route("/players/<tag>")
def get_player(tag):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"https://api.brawlstars.com/v1/players/{tag}"
    response = requests.get(url, headers=headers)
    return jsonify(response.json()), response.status_code

@app.route("/ip")
def get_ip():
    ip = requests.get("https://api.ipify.org").text
    return jsonify({"ip": ip})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
