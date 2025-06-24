from flask import Blueprint

# This route is intended to add a new patient to the database.
# It expects the following parameters (with validation):
# - FirstName (str, required validation - no digits, no special characters)
# - LastName (str, required validation - no digits, no special characters)
# - ID (int, required validation - must be a valid integer with 9 digits)
# - DateOfBirth (str, required validation - must be in ISO format, e.g., YYYY-MM-DD)
# - Gender (str, required validation - must be in one of ['male', female', 'other'])
# - MedicalHistory (str, no validation)
# - HomeAddress (str,  no validation)
# - InterfaceLanguage (str, required validation - 2 letters max)
# The Parameters will be formatted as JSON in the request body.
# The route must return an appropriate message for each specific failure or success.
# If validation fails, return 400 status. If successful, return 200 status.


add_patient_bp = Blueprint('add_patient', __name__)

@add_patient_bp.route('/api/add-patient', methods=['POST'])
def add_patient():
    try:
        # Put your code here
        return {"message": "all good", "status_code": 111}, 200


    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500