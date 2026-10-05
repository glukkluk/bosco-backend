from django import template

register = template.Library()


@register.filter(name="to_uah")
def to_uah(value, convert: bool = False):
    if convert:
        return f"{value * 45} ₴"
    return value


@register.simple_tag(name="product_count")
def product_count(products):
    return len(products)
