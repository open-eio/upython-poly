# upython-poly
Web based interface to polybot hardware running CircuitPython firmware with pawpaw framework.

## Development

Next, you'll need to set up a `.env` file, which contains:
* `FEATHER_ADDRESS` the local port where the feather is located (if attached) for pushing new builds
* `LOCAL_DEV_SERVER_ADDRESS` IP addresses for the local development server (the python server that runs from inside this repo)
* `REMOTE_DEV_SERVER_ADDRESS` IP address for a remote development server (for if you want to edit your frontend on your local machine but have API requests go to a feather on your local network).

### Build and flash the micropython firmware
First install the micropython firmware on the [ESP8266](https://github.com/micropython/micropython/tree/master/esp8266) or [ESP32](https://github.com/micropython/micropython-esp32/tree/esp32/esp32) device.

Ref.
 - Adafruit's [Building and Running MicroPython on the ESP8266](https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/overview)
 - Adafruit's [MicroPython ESP32 building and loading firmware with Tony D!](https://www.youtube.com/watch?v=qa2406iiSbI)


### Install the `pawpaw` package dependency
Within your prefered git directory clone the repo, e.g.:
```
cd ~
mkdir gitwork
cd gitwork
mkdir open-eio
cd open-eio
git clone https://github.com/open-eio/upython-pawpaw.git
```
Within this repo directory set up the symlink to the pawpaw package, e.g.:
```
cd ~/gitwork/open-eio/upython-poly
ln -s ~/gitwork/open-eio/upython-pawpaw/pawpaw
```
### Build and load the `poly_app` and its dependencies
Generate the `.mpy` files:
```
./mpy_all.sh
```
Load the files onto the device:
```
./load_scripts.sh
```
### Test by running the REPL
```
./run_repl.sh
<ctrl-d>
```
