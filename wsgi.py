from main import app

if __name__ == "__main__":
    # Only for testing and development, to run the app using Flask's built-in development server.
    app.run(debug=True)

# The following is required for deployment to a WSGI server like Gunicorn or uWSGI.
# The WSGI server will use this 'application' variable to run your Flask app.
application = app
