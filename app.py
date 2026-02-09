from flask import Flask, request, redirect, session, render_template_string

app = Flask(__name__)
app.secret_key = "my_secret_key_123"

USERS = {
    "admin": "123",
    "user": "456"
}

VIDEOS = [
    {"title": "Nhạc chill", "id": "5qap5aO4i9A"},
    {"title": "Video giải trí", "id": "xf1F5Frzzbg"},
]

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Đăng nhập</title>
<style>
body {
    font-family: Arial;
    background: linear-gradient(135deg,#667eea,#764ba2);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.box {
    background: white;
    padding: 30px;
    border-radius: 12px;
    width: 300px;
}
input,button {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
}
button {
    background: #667eea;
    color: white;
    border: none;
}
</style>
</head>
<body>
<div class="box">
<h2>Đăng nhập</h2>
<form method="post">
<input name="username" placeholder="Username" required>
<input name="password" type="password" placeholder="Password" required>
<button>Đăng nhập</button>
<p style="color:red">{{error}}</p>
</form>
</div>
</body>
</html>
"""

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>MyTube</title>
<style>
body { background:#111; color:white; font-family:Arial; margin:0 }
header {
    background:#202020;
    padding:15px;
    display:flex;
    justify-content:space-between;
}
.container {
    padding:20px;
    display:grid;
    grid-template-columns: repeat(auto-fill,minmax(300px,1fr));
    gap:20px;
}
iframe { width:100%; height:180px; border-radius:10px }
a { color:red; text-decoration:none }
</style>
</head>
<body>

<header>
<div>▶ MyTube</div>
<div>
Xin chào <b>{{user}}</b> |
<a href="/logout">Đăng xuất</a>
</div>
</header>

<div class="container">
{% for v in videos %}
<div>
<iframe src="https://www.youtube.com/embed/{{v.id}}" allowfullscreen></iframe>
<p>{{v.title}}</p>
</div>
{% endfor %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect("/home")

    error = ""
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        if u in USERS and USERS[u] == p:
            session["user"] = u
            return redirect("/home")
        else:
            error = "Sai tài khoản hoặc mật khẩu"

    return render_template_string(LOGIN_HTML, error=error)

@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")
    return render_template_string(
        HOME_HTML,
        user=session["user"],
        videos=VIDEOS
    )

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run()
