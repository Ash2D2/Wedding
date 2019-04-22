from flask import Flask
app = Flask(__name__)

@app.route("/")
def title1():
    return "Welcome to Our Wedding Sign In!"
    return "Tell us a little about yourself."    #this is not showing up 