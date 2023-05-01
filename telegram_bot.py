import requests


API_link = "https://api.telegram.org/bot5896829658:AAGWQT6f97UZyKJR9WJWNKyA8UMvQ5edVdY"
updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]


chat_id = message["from"]["id"]
text = message["text"]


input_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Hello, It's a playlist bot from SHERONFATE {text}")
