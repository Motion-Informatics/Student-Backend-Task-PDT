# Define the JSON payload
$body = @{
    httpMethod = "POST"
    path = "/api/add-patient"
    headers = @{ "Content-Type" = "application/json" }
    body = (@{
        FirstName = "Alice"
        LastName = "Bennett"
        ID = 987654321
        DateOfBirth = "1985-07-14T00:00:00"
        Gender = "Female"
        MedicalHistory = "Hypertension"
        HomeAddress = "456 Oak Street"
        InterfaceLanguage = "he"
    } | ConvertTo-Json -Compress)
} | ConvertTo-Json -Compress

# Send the request
Invoke-RestMethod -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body | ConvertTo-Json