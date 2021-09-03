import json
import time 
import requests
from boltiot import Bolt,Email
import confy_main
from twilio.rest import Client
import input1
try:
    for i in range(5):
        if i%2==0:
            my_device=Bolt(confy_main.Api_Key,confy_main.Device_Id)
            led=my_device.analogWrite('0','250')
            buzz=my_device.analogWrite('1','200')
            time.sleep(2)
        elif i%2!=0:
            my_device=Bolt(confy_main.Api_Key,confy_main.Device_Id)
            led=my_device.analogWrite('0','0')
            buzz=my_device.analogWrite('1','0')
            time.sleep(2)
        print("The temprature has exceeded Suspicious High Zone and buzz and LED would be on working state.\n")
except Exception as e:
        print("Error Occured in Suspicious High Zone,\n   ",e)

# telegram alert

url="https://api.telegram.org/"+confy_main.telegram_bot_id+"/sendMessage"
data={
        "chat_id":confy_main.telegram_chat_id,
        "text": f'The Suspicious High Zone temprature has been HIGH . '
    }
try:
    input1.temprature =requests.request(
            "POST",
            url,
            params=data
    )
    print("This is the Telegram URl \n: ")
    print(url)
    print("This is the Telegram Response    ")
    print(input1.temprature .text)
    telegram_data=json.loads(input1.temprature .text)
    telegram_data["ok"]
    print("Alert sent to Telegram\n")
except Exception as e  :
    print(" Error Occured while sendinng alert in Telegram for Suspicious High Zone:  \n", e)