#!/bin/bash -x
source .env
echo $FEATHER_ADDRESS
ampy -p $FEATHER_ADDRESS -b 115200 put SECRET_CONFIG.json
ampy -p $FEATHER_ADDRESS -b 115200 mkdir html
ampy -p $FEATHER_ADDRESS -b 115200 put ./html/404.html html/404.html
#ampy -p $FEATHER_ADDRESS -b 115200 put ./html/index.html html/index.html
ampy -p $FEATHER_ADDRESS -b 115200 put ./html/test.html html/test.html
ampy -p $FEATHER_ADDRESS -b 115200 mkdir logs
ampy -p $FEATHER_ADDRESS -b 115200 put platform_setup.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put network_setup.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put time_manager.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put dump_logs.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put am2315.mpy
ampy -p $FEATHER_ADDRESS -b 115200 mkdir pawpaw
ampy -p $FEATHER_ADDRESS -b 115200 put ./pawpaw/__init__.mpy pawpaw/__init__.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put ./pawpaw/template_engine.mpy pawpaw/template_engine.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put ./pawpaw/http_connection_reader.mpy pawpaw/http_connection_reader.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put ./pawpaw/http_connection_writer.mpy pawpaw/http_connection_writer.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put ./pawpaw/http_server.mpy pawpaw/http_server.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put ./pawpaw/auto_tree_format.mpy pawpaw/auto_tree_format.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put ./pawpaw/url_tools.mpy pawpaw/url_tools.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put ./pawpaw/web_app.mpy pawpaw/web_app.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put poly_app.mpy
ampy -p $FEATHER_ADDRESS -b 115200 put loop.py
ampy -p $FEATHER_ADDRESS -b 115200 put main.py
ampy -p $FEATHER_ADDRESS -b 115200 put boot.py
