# workout suggestor

## Deploy on heroku

```
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
heroku config:set DISABLE_POETRY_CREATE_RUNTIME_FILE=1
heroku config:set POETRY_VERSION=1.1.4
```
