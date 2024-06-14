
# Import necessary modules
from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)

# Define the route
@app.route('/')
def home():
    return render_template('home.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
