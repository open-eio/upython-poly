#!/bin/bash -x
./mpy-cross platform_setup.py
./mpy-cross network_setup.py
./mpy-cross time_manager.py
./mpy-cross dump_logs.py
./mpy-cross am2315.py
./mpy-cross pawpaw/__init__.py
./mpy-cross pawpaw/template_engine.py
./mpy-cross pawpaw/http_connection_reader.py
./mpy-cross pawpaw/http_connection_writer.py
./mpy-cross pawpaw/http_server.py
./mpy-cross pawpaw/auto_tree_format.py
./mpy-cross pawpaw/url_tools.py
./mpy-cross pawpaw/web_app.py
./mpy-cross poly_app.py
./mpy-cross loop.py
./mpy-cross main.py
./mpy-cross boot.py
