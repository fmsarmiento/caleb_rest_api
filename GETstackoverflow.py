import requests, json

# Making a request to a webpage

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
print(response)
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(f"{data['title']} - {data['link']}\n")
    else:
        print("Skipped.")