from serverless_wsgi import handle_request
from app import create_app


# Initialize the Flask app
app = create_app()

def lambda_handler(event, context):
    try:
        # Pass requests to the Flask app through serverless-wsgi
        response = handle_request(app, event, context)
        
        return response
    except Exception as e:
        # Log the exception for debugging
        raise

