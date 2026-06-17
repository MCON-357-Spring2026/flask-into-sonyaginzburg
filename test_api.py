import requests

# Making it look nice with separated lines so I understand the output
def separator(title):
    print(f"\n{'='*50}")
    print(f"  {title}")
    print('='*50)

#1 testing Welcome route
separator("1. Welcome")
response = requests.get('http://localhost:5000/')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

#2 testing About route
separator("2.About")
response = requests.get('http://localhost:5000/about')
print(f"Status Code: {response.status_code}")
data = response.json()
print(f"Name        : {data['name']}")
print(f"Course      : {data['course']}")
print(f"Semester    : {data['semester']}")

#3 testing Greeting route
separator("3. Greeting ")
response = requests.get('http://localhost:5000/greet/Leah')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")
assert "Leah" in response.text, "Name not found in response."
print("Name found in response")

#4 testing Calculator route
separator("4. Calculator")

#addition
r = requests.get('http://localhost:5000/calculate?num1=10&num2=5&operation=add')
print(f"10 + 5  →  {r.json()}")

#multiplication
r = requests.get(f"http://localhost:5000/calculate?num1=6&num2=7&operation=multiply")
print(f"6 × 7   →  {r.json()}")

#division by zero
r = requests.get(f"http://localhost:5000/calculate?num1=10&num2=0&operation=divide")
print(f"10 ÷ 0  →  Status {r.status_code} | {r.json()}")

#5 testing Echo route
separator("5.Echo")
payload  = {"message": "Hello Flask", "author": "Sonya"}
response = requests.post('http://localhost:5000/echo', json=payload)
print(f"Status Code : {response.status_code}")
body = response.json()
print(f"Response    : {body}")
assert body.get("echoed") is True, "'echoed' key not True!"
print("✓ 'echoed': true is present")

#6 Status Code route testing
separator("6.Status Codes")
payload = {"message": "Hello World"}
for code in [200, 404, 201]:
    response = requests.get(f"http://localhost:5000/status/{code}")
    print(f"Status Code : {response.status_code} | Response: {response.text}")

#7 Custom headers
separator("7. Custom headers")
response = requests.get('http://localhost:5000/')
custom_header = response.headers.get("X-Custom-Header")
print(f"Custom Header : {custom_header}")
assert custom_header == "FlaskRocks", "FlaskRocks missing."
print("X-Custom-Header: FlaskRocks")


#8 testing error handling
separator("8. Error handling")
response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

