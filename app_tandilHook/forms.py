from django import forms
from .models import Lure, Cloth, Tool

class LureForm(forms.ModelForm):
    class Meta:
        model = Lure
        fields = '__all__'

class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = '__all__'

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'