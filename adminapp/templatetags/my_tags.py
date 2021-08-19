from django import template
from django.conf import settings

register = template.Library()


def media_folder_products(string):
    if not string:
        string = "products_images/default.png"
    return settings.MEDIA_URL + str(string)


register.filter("media_folder_products", media_folder_products)


@register.filter(name="media_folder_user")
def media_folder_user(string):
    if not string:
        string = "users_avatars/default.jpg"
    return settings.MEDIA_URL + str(string)