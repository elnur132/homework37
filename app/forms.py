from django.forms import ModelForm
from .models import Computer
from captcha.fields import CaptchaField


class ComputerForm(ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid':'Неправильный текст'}, generator='captcha.helpers.math_challenge')
    class Meta:
        model = Computer
        fields = ('name', 'image', 'files', 'captcha')