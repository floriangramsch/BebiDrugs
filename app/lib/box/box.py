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
        # self.mqtt = mqtt
        self.button_a = Pin(14, Pin.IN, Pin.PULL_UP)
        self.button_b = Pin(32, Pin.IN, Pin.PULL_UP)

    def init(self):
        pass
        # self.fetch_time()

        # self.lcd.writeSecondLine(self.cats[0].ate, self.cats[1].ate)

        # self.checkIfFed()

    # def fetch_time(self) -> None:
    #     for cat in self.cats:
    #         # url = f"https://cats.floxsite.de/api/ate/today/{cat.name}"
    #         url = env.API_ATE + str(cat.name)
    #         response = urequests.get(url)
    #         data = response.json()
    #         response.close()

    #         # Array → Erstes Element → "time"
    #         if len(data) == 0:
    #             continue
    #         # z.B. "2025-07-08T23:08:37.000Z"
    #         last_time: str = data[-1]["time"]
    #         [_, uhrzeit] = last_time.split("T")
    #         time_str = uhrzeit[:5]
    #         cat.ate = time_str

    #     self.write_second_line()

    # def feed(self, cat_name):
    #     # url = "https://cats.floxsite.de/api/feed"
    #     url = env.API_FEED
    #     headers = {
    #         "Content-Type": "application/json"
    #     }

    #     payload = {
    #         "cat": cat_name,
    #     }

    #     response = urequests.post(
    #         url, data=ujson.dumps(payload), headers=headers)
    #     data = response.json()
    #     response.close()

    #     # z.B. "2025-07-08T23:08:37.000Z"
    #     last_time: str = data["time"]
    #     [_, time_str] = last_time.split(",")
    #     uhrzeit = time_str.strip()[:5]

    #     # time_str = data["time"]
    #     # uhrzeit = time_str[10:15]  # "23:08"

    #     self.lcd.clear()
    #     self.lcd.putstr("Feeding...")
    #     sleep_ms(2000)
    #     self.lcd.writeFirstLine("Naseweis", "Leo")
    #     self.led.value(0)

    #     for cat in self.cats:
    #         if cat.name == cat_name:
    #             cat.ate = uhrzeit

    #     self.write_second_line()

    # def checkIfFed(self):
    #     """
    #         Checks if the cats have been fed based on the current local hour and updates the LED indicator accordingly.
    #     """
    #     hour_now = get_local_time()
    #     # Automatische LED-Berechnung
    #     self.mqtt.led_auto = 0
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
    #     self.mqtt.led_auto = led_auto
    #     self.mqtt.update_led()
      
    def get_button_a_value(self):
        return self.button_a.value()
      
    def get_button_b_value(self):
        return self.button_b.value()

    # def write_second_line(self):
    #     self.lcd.writeSecondLine(self.cats[0].ate, self.cats[1].ate)