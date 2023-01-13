from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholder and classes, remove labels and set focus
        on first name field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
            'reason': 'Reason for contact',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
