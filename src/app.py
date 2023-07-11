from flask import Flask

app = Flask(__name__)
DiscordClientSecret = "8dyfuiRyqFvVc3RRr_edRk-fZ__JItpP" ;
aws_access_key = "AKIASP2TPHJS3AVMLWWW",
aws_access_token = "AKIASP2TPHJS3AVMLYYY"

@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()

