from django import template

register = template.Library()


@register.filter
def active_comment(comments):
    return comments.filter(active=True)




