import json
import time 
import requests
from boltiot import Bolt,Email
import confy_main
from twilio.rest import Client
import input

my_device= Bolt(confy_main.Api_Key,confy_main.Device_Id)

account_sid = 'AC7c8aaacf161a836b17986b565ac3f1aa'
auth_token = '911a4c6124c8dee2d1dfa1d0112b431f'
client=Client(account_sid,auth_token)


mailer= Email(confy_main.MAILGUN_API_KEY,confy_main.SANDBOX_URL,confy_main.SENDER_EMAIL,confy_main.RECIPIENT_EMAIL)


try:
    my_device=Bolt(confy_main.Api_Key,confy_main.Device_Id)
    led=my_device.analogWrite('0','255')
    buzz=my_device.analogWrite('1','255')
    print("The led and buzzer sounds are active and are in criticle condition(High).\n")
except Exception as e:
    print("Error Occured while processing:  \n", e)

# telegram alert

url="https://api.telegram.org/"+confy_main.telegram_bot_id+"/sendMessage"
data={
        "chat_id":confy_main.telegram_chat_id,
        "text": f'The temprature has been CRITICAL (HIGH). '
    }
try:
    input.temprature=requests.request(
            "POST",
            url,
            params=data
    )
    print("This is the Telegram URl \n: ")
    print(url)
    print("This is the Telegram Response    ")
    print(input.temprature.text)
    telegram_data=json.loads(input.temprature.text)
    telegram_data["ok"]
    print("Alert sent to Telegram\n")
except Exception as e  :
    print(" Error Occured while sendinng alert in Telegram for CRITICAL HIGH:  \n", e)

# SENDING AN SMS AND AN E-MAIL ALERT TO THE OWNER OR MANAGER ONLY AT CRITICAL CONDITIONS
 
#E-MAIL AND SMS FOR CRITICAL 

try:
    print("Making request to Twilio to send a SMS")
    client.api.account.messages.create(
        to="+918958468703",
        from_="+12107023037",
        body="Alert ! The Current temperature sensor value is CRITICAL.")
    print("SMS has been sent.\n")
except Exception as e :
    print(" Error Occured while sending sms:  \n", e)
# SENDING MAIL 

try:
    print('Making request to Mailgun to send an email\n')
    mail=mailer.send_email("ALERT","The Current temperature sensor value is CRITICAL")
    response_text= json.loads(mail.text)
    print("Response received from Mailgun is :  "+ str(response_text['message']))
    print("E-Mail has been sent\n")
except Exception as e :
    print(" Error Occured while sending email:  \n", e)