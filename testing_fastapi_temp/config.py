import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="testing_fastapi_temp",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="testing_fastapi_temp_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from testing_fastapi_temp.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export testing_fastapi_temp_KEY=value
export testing_fastapi_temp_KEY="@int 42"
export testing_fastapi_temp_KEY="@jinja {{ this.db.uri }}"
export testing_fastapi_temp_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
testing_fastapi_temp_ENV=production testing_fastapi_temp run
```

Read more on https://dynaconf.com
"""
