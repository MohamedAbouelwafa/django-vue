# django-vue
Integrate Vue Js with Django templates.

## Motivation
A trial to get the best of both Django in the backend and VueJs in the frontend.

## Add a new component
1. Add the .vue component under vueapp/src/components
2. Update the routes.json file under vueapp/src/router with the new componenet path and component name
And ... That's it!

## Local development
- Both Django local server and VueJs local server should be running.
- The VueJs app is configured to build the binaries, while serving the content with the local server.
- Django will grab the new binaries and serve the new content dynamically. No need to stop and rerun the server. A page refresh will do if not refreshed automatically.

### In a terminal window
```
./manage.py runserver
```

### In another terminal window
```
cd vueapp
yarn serve
```

## Build artifacts for production deployment
In the main project directory
```
./build.sh
```
