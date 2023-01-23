from .models import Votes
from django.forms import ModelForm, TextInput, DateTimeInput
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
def default_datetime(): return datetime.date.today()

def_title=''
def_text=''
def_ansvers=''



class VotesFormAdd(ModelForm,):


    class Meta():

        model = Votes
        fields = ['title','text','ansvers','date']

        widgets={

            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Голосования',
                'value': ''

            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите немного о голосовании',
                'value': ''
            }),
            'ansvers': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ответы в формате(используйте только буквы): answer_one,answer_two',
                'value': ''

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),


        }

        # def dfu_02(self, a, b, c,widgets):
        #     self.def_title = a
        #     self.def_text = b
        #     self.def_ansvers = c
        #     # kol = [self.def_title,self.def_text,self.def_ansvers]
        #     # return kol
        #     widgets['title'] = TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Название Голосования',
        #         'value': a
        #     })
        #     widgets['text'] = TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Напишите немного о голосовании',
        #         'value': b
        #     }),
        #     widgets['ansvers']= TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Напишите ответы в формате(используйте только буквы): answer_one,answer_two',
        #         'value': c
        #     }),



    # def puul_form(self, def_title='', def_text='', def_ansvers=''):
    #     class Meta:
    #         model = Votes
    #         fields = ['title', 'text', 'ansvers', 'date']
    #         widgets = {
    #             'title': TextInput(attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Название Голосования',
    #                 'value': '123'
    #             }),
    #             'text': TextInput(attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Напишите немного о голосовании',
    #                 'value': def_text
    #             }),
    #             'ansvers': TextInput(attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Напишите ответы в формате(используйте только буквы): answer_one,answer_two',
    #                 'value': def_ansvers
    #             }),
    #             'date': DateTimeInput(attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Дата'
    #             }),
    #
    #         }

        date = default_datetime()


def default_const(a,b,c,forma):
    def_title = a
    def_text = b
    def_ansvers = c

    forma.Meta.widgets['title'] = TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Голосования',
                'value': def_title
            }),
    forma.Meta.widgets['text'] = TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название Голосования',
        'value': def_text

    }),
    forma.Meta.widgets['ansvers'] = TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название Голосования',
        'value': def_ansvers

    }),

    return forma


