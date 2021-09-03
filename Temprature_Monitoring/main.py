import time
import confy_main
from boltiot import Bolt
import json 
my_device= Bolt(confy_main.Api_Key,confy_main.Device_Id)

while True:
    try:
        response=my_device.analogRead('A0')
        data=json.loads(response)
        sensor_value=int(data['value'])
        temprature=((100*sensor_value)/1024)
        print(temprature)
    except Exception as e:
        print("Error occured in Input file:     ",e)
    temprature=((100*sensor_value)/1024)
    if temprature   > confy_main.Min_Temprature and temprature   < confy_main.Max_Temprature:
        if temprature    >= confy_main.Suspicious_Temprature_upper:
            import suspicious_high
            print("The situation is Suspicious High")
        elif temprature    <= confy_main.Suspicious_Temprature_lower:
            import suspicious_low
            print("The situation is Suspicious Low")
        else:
            print("Temprature is being monitored and seems to be fine  :)")
            
    elif temprature     >= confy_main.Critical_temprature_Upper:
        import critical_high
        print("The condition is Critical HIGH, Cooling System Crashed  :(  ")
    elif temprature     <= confy_main.Critical_temprature_lower:
        import critical_low
        print("The condition is CRITICAL LOW, Heating system crashed :( ")
    time.sleep(30)