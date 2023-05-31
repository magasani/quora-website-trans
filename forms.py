from django import forms
from transimp.models import User,Answer
class userForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
class Answerform(forms.ModelForm):
    class Meta:
        model=Answer
        fields='__all__'