import os

env = os.getenv("APP_ENV", "DEVELOPMENT")

if env == "PRODUCTION":  # pragma no covers
    from api.config.production import *
elif env == "TEST":  # pragma no covers
    from api.config.test import *
else:
    from api.config.development import *
