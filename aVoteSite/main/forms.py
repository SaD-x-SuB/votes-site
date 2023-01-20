from .models import Votes
from django.forms import ModelForm, TextInput, DateTimeInput
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
def default_datetime(): return datetime.date.today()
class VotesFormAdd(ModelForm):
    class Meta:
        model = Votes
        fields = ['title','text','ansvers','date']

        widgets={
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Голосования'
            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите немного о голосовании'
            }),
            'ansvers': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ответы в формате(используйте только буквы): answer_one,answer_two'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),


        }
        date = default_datetime()
