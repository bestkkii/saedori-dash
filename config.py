import os

class BaseConfig:
    DEBUG = False
    REQUESTS_PATHNAME_PREFIX = "/"
    ASSETS_PATH = "/assets"

class DevConfig(BaseConfig):
    DEBUG = True
    REQUESTS_PATHNAME_PREFIX = "/"
    ASSETS_PATH = "/assets"

class ProdConfig(BaseConfig):
    DEBUG = False
    REQUESTS_PATHNAME_PREFIX = "/saedori/"
    ASSETS_PATH = "/saedori/assets"

# 환경에 따라 Config 객체를 자동으로 선택
ENV = os.getenv("ENV", "dev")
Config = DevConfig if ENV == "dev" else ProdConfig