from .models import Votes
from django.forms import ModelForm

class VotesFormAdd(ModelForm):
    class Meta:
        model = Votes