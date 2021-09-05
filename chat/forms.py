from django import forms
from simplemathcaptcha.fields import MathCaptchaField

class MyForm(forms.Form):
    some_text_field = models.CharField(max_length=50)
    captcha = MathCaptchaField()