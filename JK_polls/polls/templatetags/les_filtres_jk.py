import sys
from django import template

register = template.Library()

@register.filter(name="diviser")
def diviser(value, arg):
    try:
        a =  str(round((int(value) / int(arg)) *100,2))
#        print("v: %d ; a: %d ; r: %s" %(value, arg, a), file=sys.stderr)
        return a
    except (ValueError, ZeroDivisionError):
        return None