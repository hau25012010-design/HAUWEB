from flask import Flask, request, render_template_string

app = Flask(__name__)

VIDEOS = [
    {
        "title": "Video nhạc hot",
        "id": "I_3jF658WEY",
        "channel": "My Channel"
    },
    {
        "title": "Video giải trí",
        "id": "xf1F5Frzzbg",
        "channel": "Entertainment"
    },
    {
        "title": "Video chill",
        "id": "5qap5aO4i9A",
        "channel": "Chill Music"
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Mini</title>
    <style>
        body {
            margin: 0;
            font-family: Arial;
            background: #0f0f0f;
            color: white;
        }
        header {
            background: #202020;
            padding: 15px;
            display: flex;
            align-items: center;
        }
        header h2 {
            margin: 0 20px 0 0;
            color: red;
        }
        input {
            flex: 1;
            padding: 10px;
            border-radius: 20px;
            border: none;
            font-size: 16px;
        }
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .video {
            background: #181818;
            padding: 10px;
            border-radius: 12px;
        }
        iframe {
            width: 100%;
            height: 180px;
            border-radius: 10px;
        }
        .title {
            font-weight: bold;
            margin: 8px 0 4px;
        }
        .channel {
            color: #aaa;
            font-size: 14px;
        }
    </style>
</head>
<body>

<header>
    <h2>▶ YouTube Mini</h2>
    <form method="get" style="flex:1;">
        <input type="text" name="q" placeholder="Tìm kiếm" value="{{query}}">
    </form>
</header>

<div class="container">
{% for v in videos %}
    <div class="video">
        <iframe src="https://www.youtube.com/embed/{{v.id}}" allowfullscreen></iframe>
        <div class="title">{{v.title}}</div>
        <div class="channel">{{v.channel}}</div>
    </div>
{% endfor %}
</div>

</body>
</html>
"""

@app.route("/")
def home():
    q = request.args.get("q", "").lower()
    if q:
        filtered = [v for v in VIDEOS if q in v["title"].lower()]
    else:
        filtered = VIDEOS
    return render_template_string(HTML, videos=filtered, query=q)

if __name__ == "__main__":
    app.run()
