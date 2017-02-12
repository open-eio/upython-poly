#!/bin/bash -x
source .env
echo $FEATHER_ADDRESS
ampy -p $FEATHER_ADDRESS -b 115200 put SECRET_CONFIG.json
ampy -p $FEATHER_ADDRESS -b 115200 mkdir html
ampy -p $FEATHER_ADDRESS -b 115200 put ./html/404.html /html/404.html
ampy -p $FEATHER_ADDRESS -b 115200 put ./html/index.html /html/index.html
ampy -p $FEATHER_ADDRESS -b 115200 put ./html/test.html /html/test.html
ampy -p $FEATHER_ADDRESS -b 115200 put platform_setup.py
ampy -p $FEATHER_ADDRESS -b 115200 put network_setup.py
ampy -p $FEATHER_ADDRESS -b 115200 put time_manager.py
ampy -p $FEATHER_ADDRESS -b 115200 put dump_logs.py
ampy -p $FEATHER_ADDRESS -b 115200 put am2315.py
ampy -p $FEATHER_ADDRESS -b 115200 put poly_app.py
ampy -p $FEATHER_ADDRESS -b 115200 put main.py
ampy -p $FEATHER_ADDRESS -b 115200 put boot.py
