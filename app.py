from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>HAU WEB</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                height: 100vh;
                background: linear-gradient(135deg, #ff00cc, #3333ff, #00ffcc);
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
            }
            .box {
                background: rgba(0,0,0,0.6);
                padding: 30px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 0 30px rgba(0,0,0,0.7);
            }
            iframe {
                margin-top: 20px;
                border-radius: 15px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🔥 Chào mừng đến với HAU WEB 🔥</h1>
            <p>Web Python đầu tiên của tôi 🚀</p>

            <iframe width="560" height="315"
                src="https://www.youtube.com/embed/I_3jF658WEY"
                title="YouTube video"
                frameborder="0"
                allowfullscreen>
            </iframe>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run()



