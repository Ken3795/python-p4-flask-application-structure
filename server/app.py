from flask import Flask

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Route for dynamic user profile
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(port=5001, debug=True)

