from datetime import datetime
from django import forms

from bme.apps.listings.models import Listing

class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        exclude = ('owner', 'state',)



