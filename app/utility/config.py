import os


class GlobalConfig:
    # auth
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    TOKEN_URL = os.getenv("TOKEN_URL", "/api/v1/auth/token")
    LOGIN_MAX_RETRY = os.getenv("LOGIN_MAX_RETRY", 5)

    # db
    DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:password@localhost:3306/db")

    # amqp
    AMQP_HOST = os.getenv("AMQP_HOST", "localhost")
    AMQP_PORT = os.getenv("AMQP_PORT", 5672)
    AMQP_USERNAME = os.getenv("AMQP_USERNAME", "user")
    AMQP_PASSWORD = os.getenv("AMQP_PASSWORD", "pass")
    EXCHANGE_NAME = os.getenv("EXCHANGE_NAME", "")
    EXCHANGE_TYPE = os.getenv("EXCHANGE_TYPE", "")
    QUEUE_NAME = os.getenv("QUEUE_NAME", "task")
    ROUTING_KEY = os.getenv("ROUTING_KEY", "task")

    # redis
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    MAX_KEY_REQUEST = os.getenv("MAX_KEY_REQUEST", 3)