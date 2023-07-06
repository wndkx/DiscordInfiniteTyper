import requests
import json
import time

if __name__ == "__main__":
    while True:
        configfile = open("config.json", "r")
        config = json.loads(configfile.read())
        configfile.close()
        headers = {
            "Authorization": config["token"]
        }
        response = requests.post(f"https://discord.com/api/v9/channels/{config['channel_id']}/typing", headers=headers)
        if response.status_code == 204:
            if config["debug_mode"]:
                print(f"Received status code {response.status_code}")
                print(response.text)
            else:
                pass
        else:
            if config["debug_mode"]:
                print(f"Error: {response.status_code} \n {response.text} \n")
            else:
                print("An error occurred \n")
        time.sleep(8)