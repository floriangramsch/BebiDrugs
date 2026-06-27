`ls /dev/tty.*`
`dmesg -w` gibt genauere infos

Linux -> `/dev/ttyUSB0`

`mpremote connect /dev/ttyUSB0 repl`

`mpremote connect /dev/ttyUSB0 repl run main.py`

`uvicorn main:app --reload`

`mpremote connect /dev/ttyUSB0 repl fs cp script.py :main.py`

`mpy-cross` ???
