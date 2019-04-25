from django.forms import ModelForm
from .models import Bb, Rubric
#----------------------------------------------
from django.forms import  modelform_factory, DecimalField
from django.forms.widgets import Select
from django import forms
#--------------------------------------------
#CAPTCHA
from captcha.fields import CaptchaField

class BbForm(ModelForm):
    """форма из модели"""
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
        labels = {'title': 'Название товара'}
        help_texts = {'rubric': 'Не забудьте выбрать рубрику!'}
        field_classes= {'price': DecimalField},
        widgets = {'rubric': Select(attrs={'size': 8})},



class BbForm(forms.ModelForm):
    """Полное объявnение всех полей формы"""
    title = forms.CharField(label='Название товара')
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика',help_text='Не забудьте задать рубрику', widget=forms.widgets.Select(attrs={'size': 8}))
    #captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'})
    class Meta:
        model = Bb
        fields = ('kind', 'title', 'content', 'price', 'rubric')



class SearchForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    keyword = forms.CharField(max_length=20, label='Искомое слово')
    rucric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика')