from django import forms
from .models import Person, Example
from info.models import Game

class addgameForm(forms.ModelForm):
    def save(self, commit=True):
        print(self)
        return super.save()
    class Meta:
        model = Game
        fields = ()


#例
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ("name", )

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name", "age")