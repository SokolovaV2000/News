from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = '__all__'

   def clean(self):
       cleaned_data = super().clean()
       body = cleaned_data.get("body")
       if body is not None and len(body) < 20:
           raise ValidationError({
               "description": "Текст Вашей статьи не может быть менее 20 символов, как бы кратко и лаконично Вы не умели писать!"
           })
       head = cleaned_data.get("head")
       if head == body:
           raise ValidationError(
               "Заголовок не может быть таким же, как текст статьи!"
           )

       return cleaned_data