curl -sS -X POST 'http://localhost:9000/2015-03-31/functions/function/invocations' \
-H 'Content-Type: application/json' \
-d '{
  "httpMethod": "POST", 
  "path": "/api/add-patient", 
  "headers": { "Content-Type": "application/json" }, 
  "body": "{\"FirstName\": \"Alice\", \"LastName\": \"Bennett\", \"ID\": 987654321, \"DateOfBirth\": \"1985-07-14T00:00:00\", \"Gender\": \"Female\", \"MedicalHistory\": \"Hypertension\", \"HomeAddress\": \"456 Oak Street\", \"InterfaceLanguage\": \"he\"}"
}' | jq