from flask import Blueprint

# This route is intended to add a new user to the database.
# It expects the following parameters (with validation):
# - UserName (str, required validation - no digits, no special characters)
# - CreatedDate (str, required validation - must be in ISO format, e.g., YYYY-MM-DD)
# - FirstName (str, required validation - no digits, no special characters)
# - LastName (str, required validation - no digits, no special characters)
# - PhoneNumber (str, required validation - must be a valid phone number format - e.g., 10 digits)
# - HomeAddress (str, no validation)
# - ID (str, required validation - must be a valid identifier, e.g., 9 digits)
# - Email (str, required validation - must be a valid email format)
# # The Parameters will be formatted as JSON in the request body.
# The route must return an appropriate message for each specific failure or success.
# If validation fails, return 400 status. If successful, return 200 status.



add_user_bp = Blueprint('add_user', __name__)

@add_user_bp.route('/api/add-user', methods=['POST'])
def add_user():
    try:
        # Put your code here
        return {"message": "all good", "status_code": 111}, 200

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500