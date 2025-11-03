from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# The Flask application will now look for 'index.html' inside a 'templates' folder.
@app.route("/")
def index():
    """Renders the HTML template containing the embedded Dialogflow Messenger."""
    return render_template('index.html')

if __name__ == "__main__":
    # Use 0.0.0.0 host and port 8080 for compatibility with Cloud Shell Preview
    print("Starting Flask app. Access the preview on port 8080.")
    app.run(debug=True, host='0.0.0.0', port=8080)