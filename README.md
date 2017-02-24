# upython-poly
Web based interface to polybot hardware running MicroPython firmware with 
`pawpaw` framework.
The dynamic JavaScript frontend is based on Preact.js (a small version of React).

## Development Environment

Set up a `.env` file, which contains:
* `FEATHER_ADDRESS` the local port where the feather is located (if attached) for pushing new builds
* `LOCAL_DEV_SERVER_ADDRESS` IP addresses for the local development server (the python server that runs from inside this repo)
* `REMOTE_DEV_SERVER_ADDRESS` IP address for a remote development server (for if you want to edit your frontend on your local machine but have API requests go to a feather on your local network).

## Backend - Development

### Build and flash the micropython firmware
...on the [ESP8266](https://github.com/micropython/micropython/tree/master/esp8266) 
or [ESP32](https://github.com/micropython/micropython-esp32/tree/esp32/esp32) device.

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

## Fontend Development - JavaScript

To make it go, start with an
```
npm install
```
You can start the development server in two modes:
```
npm run dev-remote
```
which will expose the variable `SERVER_ADDRESS` thoughout your javascript code 
as the `REMOTE_DEV_SERVER_ADDRESS`
```
npm run dev-local
```
which will expose the variable `SERVER_ADDRESS` thoughout your javascript code 
as the `LOCAL_DEV_SERVER_ADDRESS` and also start the local python development 
server.

Both commands will make the page available at `localhost:3000` and start up 
watchers that do a few slick things:
* Re-build JS on changes
* Re-build SCSS (the superset of CSS we're using for styling) on changes
* Trigger Livereload to hot-replace styles as changes are made (you'll need to
  have the livereload pluggin installed and actived in your browser)
* Hot reload components in the Preact app while preserving state

All of that means that any changes you make inside of the `src` directory where
the javascript and scss sources live will be instantly visible.


### Build

Just hit
```
npm run build
```
and presto! (hopefully presto) your app will roll up in a tiny ball and go 
cower inside one file in `html/index.html`. That means that if you run 
`./load-scripts` after `npm run build` your changes will push directly to the 
attached feather, no extra steps!

When built, the `SERVER_ADDRESS` variable will default to sending requests just
to the root where the page is served from, which will be the case once 
`index.html` is being served from the device.
