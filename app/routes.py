from app import app

@app.route("/")
def home():
    return "Hello, CI/CD!"

@app.route("/about")
def about():
    return "About page"
