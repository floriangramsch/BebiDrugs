import ujson
import urequests
from utime import sleep_ms
from misc import get_local_time, wifi
from machine import Pin
import env

class Box():
    def __init__(self, lcd, led: Pin) -> None:
        self.lcd = lcd
        self.led = led
        self.button_a = Pin(14, Pin.IN, Pin.PULL_UP)
        self.button_b = Pin(32, Pin.IN, Pin.PULL_UP)

    def fetch_taken_drugs(self) -> dict[str, str]:
        url = env.API_DRUGS_TODAY
        response = urequests.get(url)
        data = response.json()
        response.close()

        drugs = {
            "medikinet": "not_taken",
            "vitamin_d": "not_taken",
            "eisen": "not_taken"
        }
        
        for drug in data["value"]:
            if drug["name"] in drugs:
                drugs[drug["name"]] = drug["value"]
        
        print(data)
        return drugs

    def change_drug_state(self, drug, value):
        url = env.API_DRUG_CHANGE
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "drug": drug,
            "value": value
        }

        urequests.post(
            url, data=ujson.dumps(payload), headers=headers)


    # def checkIfFed(self):
    #     """
    #         Checks if the cats have been fed based on the current local hour and updates the LED indicator accordingly.
    #     """
    #     hour_now = get_local_time()
    #     # Automatische LED-Berechnung
    #     led_auto = 0

    #     for cat in [self.cats[0]]:
    #         if cat.ate is None:
    #             led_auto = 1
    #             break

    #         last_fed_hour = int(cat.ate[:2])
    #         if 5 <= hour_now < 17 and last_fed_hour < 5:
    #             led_auto = 1
    #             break
    #         elif hour_now >= 17 and last_fed_hour < 17:
    #             led_auto = 1
    #             break
      
    def get_button_a_value(self):
        return self.button_a.value()
      
    def get_button_b_value(self):
        return self.button_b.value()
