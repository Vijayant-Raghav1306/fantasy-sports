from app import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/about')
def about():
    return "about page"

@app.route('/teams')
def teams():
    return "Premier league teams!"
