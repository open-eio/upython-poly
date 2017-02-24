# upython-poly
Web based interface to polybot hardware running CircuitPython firmware with pawpaw framework.

# javascript things
This repo includes a bunch of junk for creating a dynamic webapp based on Preact.js (a small version of React).

## Installation

To make it go, start with an
```
npm install
```

## Development

Next, you'll need to set up a `.env` file, which contains:
`FEATHER_ADDRESS` the local port where the feather is located (if attached) for pushing new builds
`LOCAL_DEV_SERVER_ADDRESS` IP addresses for the local development server (the python server that runs from inside this repo)
`REMOTE_DEV_SERVER_ADDRESS` IP address for a remote development server (for if you want to edit your frontend on your local machine but have API requests go to a feather on your local network).

You can start the development server in two modes:
```
npm run dev-remote
```
which will expose the variable `SERVER_ADDRESS` thoughout your javascript code as the `REMOTE_DEV_SERVER_ADDRESS`
```
npm run dev-local
```
which will expose the variable `SERVER_ADDRESS` thoughout your javascript code as the `LOCAL_DEV_SERVER_ADDRESS` and also start the local python development server.

Both commands will make the page available at `localhost:3000` and start up watchers that do a few slick things:
* Re-build JS on changes
* Re-build SCSS (the superset of CSS we're using for styling) on changes
* Trigger Livereload to hot-replace styles as changes are made (you'll need to have the livereload pluggin installed and actived in your browser)
* Hot reload components in the Preact app while preserving state

All of that means that any changes you make inside of the `src` directory where the javascript and scss sources live will be instantly visible.


## Build

Just hit
```
npm run build
```
and presto! (hopefully presto) your app will roll up in a tiny ball and go cower inside one file in `html/index.html`. That means that if you run `./load-scripts` after `npm run build` your changes will push directly to the attached feather, no extra steps!


