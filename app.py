from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Video</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                background: linear-gradient(135deg, #667eea, #764ba2);
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                color: white;
            }

            .box {
                background: rgba(0, 0, 0, 0.4);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 0 30px rgba(0,0,0,0.5);
            }

            h1 {
                margin-bottom: 15px;
            }

            iframe {
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🎬 Web Video YouTube</h1>
            <iframe width="560" height="315"
            src="https://www.youtube.com/embed/I_3jF658WEY"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen></iframe>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)


