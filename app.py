from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")  # Set this as a secret/env var

@app.route("/unifi-webhook", methods=["POST"])
def unifi_webhook():
    data = request.get_json()
    print("Incoming Webhook:", data)

    # Basic sanity check
    if not data or "event_type" not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Create a simple message based on the event
    camera_name = data.get("camera", {}).get("name", "Unknown Camera")
    event_type = data.get("event_type")

    message = f"📹 UniFi Event Detected: **{event_type}** from **{camera_name}**"

    # Post to Discord
    discord_payload = {
        "content": message
    }

    try:
        resp = requests.post(DISCORD_WEBHOOK_URL, json=discord_payload)
        resp.raise_for_status()
    except Exception as e:
        print("Discord webhook failed:", e)
        return jsonify({"error": "Failed to send to Discord"}), 500

    return jsonify({"status": "forwarded to Discord"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

if not DISCORD_WEBHOOK_URL:
    raise Exception("Missing DISCORD_WEBHOOK_URL environment variable")
