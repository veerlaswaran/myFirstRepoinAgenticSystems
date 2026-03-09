import json

api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

response_data = json.loads(api_response)

request_id = response_data["id"]
status = response_data["status"]
text_result = response_data["result"]["text"]
confidence_score = response_data["result"]["confidence"]

print(f"Request ID: {request_id}")
print(f"Status: {status}")
print(f"Text: {text_result}")
print(f"Confidence: {confidence_score}")

if confidence_score < 0.9:
    print("⚠️ Warning: Confidence score is below 0.9")

follow_up_result = {
    "id": "req_124",
    "status": "success",
    "result": {
        "text": "Follow-up response",
        "confidence": 0.92
    }
}

follow_up_json = json.dumps(follow_up_result, indent=2)

with open("response.json", "w") as file:
    file.write(follow_up_json)

print("\nFollow-up JSON written to response.json")
