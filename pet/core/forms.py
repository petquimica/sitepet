from django import forms
from django.conf import settings
from .email import send_email_template


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_message(self):
        template = 'core/contact_email.html'
        subject = 'PET: E-mail do [%s]' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        send_email_template(
            subject,
            template,
            context,
            [settings.CONTACT_EMAIL],
            from_email=context['email']
        )
