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
        sleep_ms(50)  # Debounce delay
        return True
    else: 
        return False
    
def button_b_pressed(last_state: int | None, new_state: int | None):
    if last_state == 1 and new_state == 0:
        sleep_ms(50)  # Debounce delay
        return True
    else: 
        return False
            
def switch_selection(selection):
    if selection == "medikinet":
        return "vitamin_d"
    elif selection == "vitamin_d":
        return "eisen"
    elif selection == "eisen":
        return "medikinet"
    return "medikinet"

def switch_drug_state(drug):
    if drug == "not_taken":
        return "taken"
    elif drug == "taken":
        return "skipped"
    elif drug == "skipped":
        return "not_taken"
    return "not_taken"


def switch_state(drugs, selected_drug):
    if selected_drug in drugs:
        drugs[selected_drug] = switch_drug_state(drugs[selected_drug])
    return drugs