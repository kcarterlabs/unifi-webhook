from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "need a new webhook url you dummy"

@app.route("/unifi-webhook", methods=["POST"])
def unifi_webhook():
    data = request.json
    if data and "camera" in data and "event_type" in data:
        camera_name = data["camera"]["name"]
        event_type = data["event_type"]

        if event_type == "smart_detect":
            payload = {
                "username": "UniFi Alert",
                "content": f"🚨 **Person detected** on **{camera_name}**!"
            }
            requests.post(DISCORD_WEBHOOK_URL, json=payload)

    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

