from django import forms
from .models import Lead

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'email','priority','status', 'phone', 'address', 'city', 'state', 'zipcode', 'title', 'industry', 'company', 'description')