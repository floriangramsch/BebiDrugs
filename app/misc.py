from utime import sleep_ms
from time import localtime
import ntptime
import machine

from lib.wifi.wifi import connect_wifi
from lib.lcd.lcd import LCD
from lib.mqtt.mqtt import Mqtt

try:
    from typing import Literal
    DrugState = Literal["medikinet", "vitamin_d", "eisen"]
except ImportError:
    DrugState = str

def get_local_time(offset_hours=2):  # Sommerzeit = 2, Winterzeit = 1
    t = localtime()
    hour = (t[3] + offset_hours) % 24
    # return (hour, t[4])  # (Stunde, Minute)
    return hour  # (Stunde, Minute)


def wifi(lcd):
    lcd.putstr("Connecting wifi...")
    connect_wifi()
    ntptime.settime()
    lcd.clear()
    lcd.putstr("Connected!")
    sleep_ms(1000)
    lcd.clear()
    
def button_a_pressed(last_state: int | None, new_state: int | None):
    if last_state == 1 and new_state == 0:
        print("State switch")
        sleep_ms(50)  # Debounce delay
        return True
    else: 
        return False
        
# def button_pressed(mqtt: Mqtt, last_state: int | None, new_state: int | None, callback):
#     if last_state == 1 and new_state == 0:
#         callback()
#         print("Fed")
#         mqtt.pub(b"kodzenbox/button/01/state", b"Button pressed")
#         sleep_ms(50)  # Debounce delay
#     elif last_state == 0 and new_state == 1:
#         mqtt.pub(b"kodzenbox/button/01/state", b"Button released")
        
# def publish_all(mqtt: Mqtt, lcd: LCD, led: machine.Pin):
#     mqtt.pub(b'kodzenbox/led/state', b"ON" if led.value() else b"OFF")
#     mqtt.pub(b'kodzenbox/lcd/state', b"ON" if lcd.backlight else b"OFF")
    
def switch_state(state):
    print(state)
    if state == "medikinet":
        return "vitamin_d"
    elif state == "vitamin_d":
        return "eisen"
    elif state == "eisen":
        return "medikinet"
    return "medikinet"
