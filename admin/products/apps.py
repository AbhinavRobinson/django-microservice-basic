from django.apps import AppConfig

from .config import AMQPURL


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    amqpUrl = AMQPURL
