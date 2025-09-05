from django import template
import re

register = template.Library()


@register.filter
def uppercase(value):
    return value.upper()

@register.filter
def word_count(value):
    return len(value.split())

@register.filter
def first_word(value):
    return value.split()[0] if value else ""

@register.filter
def last_word(value):
    return value.split()[-1] if value else ""

@register.filter
def remove_punctuation(value):
    return re.sub(r"[^\w\s]", '', value)

@register.filter
def reverse_string(value):
    return value.slice[::-1]

@register.filter
def word_limit(value, num):
    words  = value.split()
    return " ".join(words[:num]) + ("..." if len(words) > num else "")


@register.filter
def char_count(value):
    return len(value.replace(" ", ""))
