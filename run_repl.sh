#!/bin/bash -x
source .env
echo $FEATHER_ADDRESS
screen $FEATHER_ADDRESS 115200
