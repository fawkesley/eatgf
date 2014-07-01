[![Build Status](https://travis-ci.org/paulfurley/gluten-free-liverpool.svg?branch=master)](https://travis-ci.org/paulfurley/gluten-free-liverpool)

# Configuring a new Heroku app

After setting up a new app, you need to configure a number of environment
variables through the herkou command line, for example:

```
export APP_NAME="eatgf-staging"
export DOMAIN="www-staging.eatgf.org"

# DJANGO_SETTINGS_MODULE
heroku config:set DJANGO_SETTINGS_MODULE=eatgf.settings.production --app ${APP_NAME}

# DATABASE
heroku addons:add heroku-postgresql:dev --app ${APP_NAME}
heroku pg:promote <name of database ie HEROKU_POSTGRESQL_ROSE_URL> --app ${APP_NAME}
heroku addons:add pgbackups --app ${APP_NAME}

# SECRET_KEY
heroku config:set SECRET_KEY=$(openssl rand -base64 64) --app ${APP_NAME}

# DOMAINS
heroku domains:add ${DOMAIN} --app ${APP_NAME}

# WORKERS (after first deploy)
heroku ps:scale web=1 --app ${APP_NAME}
```

# URLs

https://reviews.eatgf.org/liverpool/ [redirect to next]
https://reviews.eatgf.org/gluten-free-restaurants-in-liverpool

https://reviews.eatgf.org/liverpool/alma-de-cuba-restaurant

# Search listings

```
Gluten-free restaurant reviews in Liverpool | eatglutenfree
reviews.eatgf.org/liverpool-gluten-free-restaurant-reviews/
Reviews & recommendations from our members for eating out gluten-free in Liverpool
```
