from flask import Blueprint

# This route is intended to add a new session to the database.
# It expects the following parameters (with validation):
# - PatientID (int, required validation - must be a valid integer and exist in the Patients table)
# - StartDate (str, required validation - must be in ISO format, e.g., YYYY-MM-DD)
# - EndDate (str, required validation - must be in ISO format, e.g., YYYY-MM-DD)
# - Summary (str, no validation)
# - TherapistID (int, required validation - must be a valid integer and exist in the Users table)
# # The Parameters will be formatted as JSON in the request body.
# The route must return an appropriate message for each specific failure or success.
# If validation fails, return 400 status. If successful, return 200 status.


setup_session_bp = Blueprint('setup_session', __name__)

@setup_session_bp.route('/api/setup-session', methods=['POST'])
def setup_session():
    try:
        # Put your code here
        return {"message": "all good", "status_code": 111}, 200

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500