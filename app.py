from flask import Flask, request, render_template_string

app = Flask(__name__)

VIDEOS = [
    {"title": "Nhạc chill buổi tối", "id": "5qap5aO4i9A", "channel": "Chillhop"},
    {"title": "Video giải trí hot", "id": "xf1F5Frzzbg", "channel": "Entertainment"},
    {"title": "Nhạc thư giãn học bài", "id": "I_3jF658WEY", "channel": "Study Music"},
    {"title": "Lo-fi chill", "id": "DWcJFNfaw9c", "channel": "Lofi Girl"},
]

HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>MyTube – Web Video</title>
<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}
header {
    display: flex;
    align-items: center;
    padding: 15px 25px;
    background: rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
}
.logo {
    font-size: 26px;
    font-weight: bold;
    color: #ff3c3c;
}
.search {
    margin-left: 30px;
    flex: 1;
}
.search input {
    width: 100%;
    padding: 12px 20px;
    border-radius: 30px;
    border: none;
    font-size: 16px;
}
.container {
    padding: 30px;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 25px;
}
.card {
    background: rgba(0,0,0,0.35);
    border-radius: 18px;
    padding: 12px;
    transition: transform 0.3s, box-shadow 0.3s;
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.4);
}
iframe {
    width: 100%;
    height: 180px;
    border-radius: 14px;
}
.title {
    margin: 10px 0 4px;
    font-weight: bold;
    font-size: 16px;
}
.channel {
    font-size: 14px;
    color: #ddd;
}
footer {
    text-align: center;
    padding: 20px;
    background: rgba(0,0,0,0.4);
    margin-top: 20px;
    font-size: 14px;
}
</style>
</head>

<body>
<header>
    <div class="logo">▶ MyTube</div>
    <form class="search" method="get">
        <input type="text" name="q" placeholder="🔍 Tìm kiếm video..." value="{{query}}">
    </form>
</header>

<div class="container">
{% for v in videos %}
    <div class="card">
        <iframe src="https://www.youtube.com/embed/{{v.id}}" allowfullscreen></iframe>
        <div class="title">{{v.title}}</div>
        <div class="channel">{{v.channel}}</div>
    </div>
{% endfor %}
</div>

<footer>
    © 2026 MyTube | Web video demo bằng Python Flask
</footer>

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

