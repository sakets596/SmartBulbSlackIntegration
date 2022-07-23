#pip install slackclient
from slack import RTMClient
import requests
import os
from tuyaBulb import bulb_on, bulb_off

@RTMClient.run_on(event="message")
def smartBot(**payload):
    """
    This function triggers when someone sends
    a message on the slack(fn name can be anything)
    """
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")

    # If a message is not send by the bot
    if bot_id == "":
        channel_id = data["channel"]

        # Extracting message send by the user on the slack
        text = data.get("text", "")
        text = text.split(">")[-1].strip()

        response = ""
        if "on" in text.lower():
            try:
                bulb_on()
                response = "Bulb is on."
            except Exception as e:
                response = f"Error occured: {e}"

        elif "off" in text.lower():
            try:
                bulb_off()
                response = "Bulb is off."
            except Exception as e:
                response = f"Error occured: {e}"
        elif "help" in text.lower():
            response = f"Try below:\n @smartbot bulb on \n @smartbot bulb off"
        else:
            response = f"Invalid command."
        
        # Sending message back to slack
        web_client.chat_postMessage(channel=channel_id, text=response)

try:
    SLACK_TOKEN = os.environ['SLACK_TOKEN']
    rtm_client = RTMClient(token=SLACK_TOKEN)
    print("Bot is up and running!")
    rtm_client.start()
except Exception as err:
    print(err)