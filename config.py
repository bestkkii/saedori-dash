import os

class BaseConfig:
    DEBUG = False
    REQUESTS_PATHNAME_PREFIX = "/"

class DevConfig(BaseConfig):
    DEBUG = True
    REQUESTS_PATHNAME_PREFIX = "/"

class ProdConfig(BaseConfig):
    DEBUG = False
    REQUESTS_PATHNAME_PREFIX = "/saedori/"
