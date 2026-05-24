from django import template
from main.utils import return_title

register = template.Library()


@register.simple_tag(takes_context=True)
def t(context, key):

    request = context["request"]

    lang = getattr(
        request,
        "CURRENT_LANG",
        "uz"
    )

    return return_title(lang, key)