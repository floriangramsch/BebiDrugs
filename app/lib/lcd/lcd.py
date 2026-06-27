from .esp_lcd_4bit import GpioLcd


class LCD(GpioLcd):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clear_line(self, line):
        """Clears a specific line on the LCD by overwriting with spaces."""
        self.move_to(0, line)
        self.putstr(' ' * self.num_columns)
        self.move_to(0, line)

    def writeFirstLine(self, drug_state):
        med = "[Med]" if drug_state == "medikinet" else "Med"
        vd = "[VD]" if drug_state == "vitamin_d" else "VD"
        fe = "[FE]" if drug_state == "eisen" else "FE"
        
        self.clear_line(0)
        self.move_to(0, 0) if drug_state == "medikinet" else self.move_to(1, 0)
        self.putstr(med)
        self.move_to(6, 0) if drug_state == "vitamin_d" else self.move_to(7, 0)
        self.putstr(vd)
        self.move_to(11, 0) if drug_state == "eisen" else self.move_to(12, 0)
        self.putstr(fe)
        
    def writeSecondLine(self, a, b, c):
        check_left = bytearray([
            0b00000,
            0b00000,
            0b00000,
            0b11000,
            0b01100,
            0b00111,
            0b00011,
            0b00000
        ])
        
        check_right = bytearray([
            0b00001,
            0b00011,
            0b00110,
            0b01100,
            0b11000,
            0b10000,
            0b00000,
            0b00000,
        ])
        
        pill_left = bytearray([
            0b00000,
            0b00111,
            0b01100,
            0b11000,
            0b11000,
            0b11000,
            0b01100,
            0b00111
        ])

        pill_mid = bytearray([
            0b01111,
            0b11111,
            0b11111,
            0b11111,
            0b11111,
            0b11111,
            0b11111,
            0b01111
        ])

        pill_right = bytearray([
            0b00000,
            0b11100,
            0b00110,
            0b00011,
            0b00011,
            0b00011,
            0b00110,
            0b11100
        ])


        pill_left = bytearray([
            0b00000,
            0b00111,
            0b01100,
            0b11000,
            0b11000,
            0b11000,
            0b01100,
            0b00111
        ])

        pill_mid = bytearray([
            0b00000,
            0b11111,
            0b00100,
            0b00100,
            0b00100,
            0b00100,
            0b00100,
            0b11111
        ])

        pill_right = bytearray([
            0b00000,
            0b11100,
            0b00110,
            0b00011,
            0b00011,
            0b00011,
            0b00110,
            0b11100
        ])


        skip_left = bytearray([
            0b00000,
            0b00111,
            0b01100,
            0b11000,
            0b11000,
            0b11000,
            0b01100,
            0b00111
        ])

        skip_mid = bytearray([
            0b01111,
            0b11111,
            0b11111,
            0b11111,
            0b11111,
            0b11111,
            0b11111,
            0b01111
        ])

        skip_right = bytearray([
            0b00000,
            0b11100,
            0b00110,
            0b00011,
            0b00011,
            0b00011,
            0b00110,
            0b11100
        ])
   

        self.custom_char(0, check_left)
        self.custom_char(1, check_right)
        self.custom_char(2, pill_left)
        self.custom_char(3, pill_mid)
        self.custom_char(4, pill_right)

        self.clear_line(1)
        self.move_to(1, 1)
        self.putstr(chr(0) + chr(1)) 
        self.move_to(7, 1)
        self.putstr(chr(2) + chr(3) + chr(4))
        