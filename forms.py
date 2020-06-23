from django import forms
from .models import Estimate
class ImageForm(forms.ModelForm):
    class Meta:
        model=Estimate
        fields=['username','contact','license_name','license_image']