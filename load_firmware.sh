#!/bin/bash -x
source .env
echo $FEATHER_ADDRESS
esptool.py -p $FEATHER_ADDRESS --baud 460800 erase_flash
esptool.py -p $FEATHER_ADDRESS --baud 460800 write_flash --flash_size=detect 0 linkto_firmware-circuitpython-pawpaw.bin
