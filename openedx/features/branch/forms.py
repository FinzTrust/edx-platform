"""
Forms for the Announcement Editor
"""


from pickle import FALSE
from django import forms

from .models import Branch


class BranchForm(forms.ModelForm):
    """
    Form for editing Branch
    """
    proile_picture = forms.ImageField(label='Profile Picture', required=False)
    name_kh = forms.CharField(widget=forms.TextInput, label='Khmer Name', required=False)
    name_en = forms.CharField(widget=forms.TextInput, label='English Name', required=False)
    short_name = forms.CharField(widget=forms.TextInput, label='Short Name', required=False)
    contact_person = forms.CharField(widget=forms.TextInput, label='Contact Person', required=False)
    contact_number = forms.CharField(widget=forms.TextInput, label='Contact Number', required=False)
    contact_number_2 = forms.CharField(widget=forms.TextInput, label='Contact Number II', required=False)
    address = forms.CharField(widget=forms.Textarea, label='Address', required=False)
    website = forms.CharField(widget=forms.TextInput, label='Website', required=False)
    email = forms.CharField(label='Email')
    facebook = forms.CharField(widget=forms.TextInput, label='Facebook', required=False)
    telegram = forms.CharField(widget=forms.TextInput, label='Telegram', required=False)
    whatsapp = forms.CharField(widget=forms.TextInput, label='What\'s App', required=False)
    is_active = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Branch
        fields = '__all__'
