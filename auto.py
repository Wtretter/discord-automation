import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://discord.com/api/v10"
token = os.environ.get("TOKEN")
user_id = os.environ.get("USER_ID")

def send_dm(user_id: str, text: str):
    response = requests.post(
        base_url+"/users/@me/channels", 
        json={"recipient_id": user_id}, 
        headers={
            "Authorization": f"Bot {token}",
            "User-Agent": "DiscordBot (github.com/wtretter/discord-automation, 0.1)"
        }
    ).json()
    channel_id = response["id"]
    requests.post(
        base_url+f"/channels/{channel_id}/messages", 
        json={"content": text}, 
        headers={
            "Authorization": f"Bot {token}",
            "User-Agent": "DiscordBot (github.com/wtretter/discord-automation, 0.1)"
        }
    )



file_contents = None
while True:
    with open("data.txt", "r") as data_file:
        new_data = data_file.read()
        if file_contents != None and new_data != file_contents:
            print("sending message")
            send_dm(user_id, new_data)
        else: 
            print("no changes")
        file_contents = new_data
            
    time.sleep(5)

    

