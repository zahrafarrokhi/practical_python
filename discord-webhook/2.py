from flask import Flask
from flask import request, jsonify
import requests
mUrl = "https://discordapp.com/api/webhooks/1097824674748055613/dmQYy7ZR1JHDiJ4I6HSYg9v-l9bGg_K8Dca-QOjtxKhZnjbEqGGpmZdEVTfHVX4Xrmb2"


app = Flask(__name__)


@app.route('/contact', methods=['POST',])
def contact():
    if request.method == 'POST':
        data = request.form
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        subject = data.get('subject')
        text = data.get('text')

        dis_data = {
            "username": "nelly",
            "avatar_url": "https://i.imgur.com/4M34hi2.png",
            "content": "New Message",
            "embeds": [
                {
                    "author": {
                        "name": f"{first_name} {last_name} ♫",
                        # "url": f"mail:{email}",

                    },
                    "fields": [
                        {
                            "name": "Email",
                            "value": email,
                            "inline": True
                        },],
                    "title": subject,
                    "description": text,
                    "color": 15258703,

                },]
        }
        response = requests.post(mUrl, json=dis_data)

        print(response.status_code)

        print(response.content)

        return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run()
