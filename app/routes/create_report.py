from flask import Blueprint

# This route should return a summary table for all patients using the pandas library.
# It should query the database for all sessions and group them by PatientID.
# The result should be a table with the following columns: PatientID | number_of_session | total_duration
# If the query is successful, return the summary table with a 200 status code.
# If any error occurs during processing, return a 500 error with the error message.


create_report_bp = Blueprint('create_report', __name__)

@create_report_bp.route('/api/create-report', methods=['GET'])
def create_report():
    try:
        # Put your code here
        return {"message": "all good", "status_code": 111}, 200

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500