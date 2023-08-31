from django import template


register = template.Library()

CENSORED = ['редиска', 'собака', 'какашка']
@register.filter()
def censor(value):
   if value in CENSORED:
      return value.replace(***)
   else:
      pass