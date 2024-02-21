from django import template

register = template.Library()


@register.filter
def e_to_p_number(number):
    number = str(number)
    persian = '۰١٢٣٤٥٦٧٨٩'
    english = '0123456789'
    e_to_p = number.maketrans(english, persian)
    return number.translate(e_to_p)
