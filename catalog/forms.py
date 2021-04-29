import datetime 
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms


class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""
    renewal_date = forms.DateField(
            help_text="Adj meg új lejárati dátumot (4 héten belüli időpontot, 3 hét az alapértelmezett).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))
  
        return data