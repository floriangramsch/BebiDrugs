#!/bin/bash

mpremote connect /dev/ttyUSB0 fs cp app/main.py :main.py
mpremote connect /dev/ttyUSB0 fs cp app/misc.py :misc.py
mpremote connect /dev/ttyUSB0 fs cp app/env.py :env.py
mpremote connect /dev/ttyUSB0 fs rm -r :lib                
mpremote connect /dev/ttyUSB0 fs cp -r app/lib :lib

mpremote connect /dev/ttyUSB0 exec "exec(open('main.py').read())"