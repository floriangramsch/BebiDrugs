from utime import sleep_ms, ticks_ms
from machine import Pin
import machine

from lib.lcd.lcd import LCD
from lib.box.box import Box
from misc import wifi, button_a_pressed, button_b_pressed, switch_selection, switch_state

def main():
    print("Initializing everything...")
    
    selected_drug = "medikinet"
    
    lcd = LCD(rs_pin=Pin(15),
              enable_pin=Pin(2),
              d4_pin=Pin(4),
              d5_pin=Pin(16),
              d6_pin=Pin(17),
              d7_pin=Pin(5),
              backlight_pin=None,
              num_lines=2, num_columns=16)

    
    led = machine.Pin(27, machine.Pin.OUT)

    wifi(lcd) # clears screen afterwards
    
    lcd.writeFirstLine(selected_drug)

    box = Box(lcd, led)
    
    drugs = box.fetch_taken_drugs()

    lcd.writeSecondLine(drugs["medikinet"], drugs["vitamin_d"], drugs["eisen"])

    last_state_button_a = box.get_button_a_value()
    last_state_button_b = box.get_button_b_value()
    last_refresh = ticks_ms()
    print("Starting loop..")
    while True:
        current_state_button_a = box.get_button_a_value()
        current_state_button_b = box.get_button_b_value()

        if button_a_pressed(last_state_button_a, current_state_button_a):
            selected_drug = switch_selection(selected_drug)
            lcd.writeFirstLine(selected_drug)
        if button_b_pressed(last_state_button_b, current_state_button_b):
            drugs = switch_state(drugs, selected_drug)
            lcd.writeSecondLine(
                    drugs["medikinet"], drugs["vitamin_d"], drugs["eisen"]
                )
            box.change_drug_state(selected_drug, drugs[selected_drug])
            

        # alle 5 Minuten aktualisieren
        if ticks_ms() - last_refresh >= 300_000:  # 300000 ms = 5 Minuten
            drugs = box.fetch_taken_drugs()
            last_refresh = ticks_ms()

        last_state_button_a = current_state_button_a
        last_state_button_b = current_state_button_b
        sleep_ms(10)


print(__name__)
if __name__ == "__main__":
    main()