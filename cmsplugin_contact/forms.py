from django import forms
from django.forms.widgets import CheckboxSelectMultiple, TextInput, Textarea
from cmsplugin_contact.nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm

SERVICES = (
    ('bcdesign', 'BigCommerce Templates'),
    ('bcmod', 'BigCommerce Modifications (Jquery)'),
    ('bcauto', 'BigCommerce Automation'),
    ('bctraining', 'BigCommerce Training'),
    ('bcseo', 'BigCommerce SEO'),
    )

BUDGET = (
    ('under500', '< $500'),
    ('over1000', '$1000 - $3000'),
    ('over3000', '$3000 - $5000'),
    ('over5000', '$5000 - $7000'),
    ('other', 'Other'),
    )

CONTACT_METHOD = (
    ('email','Email'),
    ('phone', 'Phone')
)
  
class ContactForm(forms.Form):
    email = forms.EmailField(max_length=256)
    subject = forms.CharField(max_length=256, required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'span5', 'rows':5}))
    website_url = forms.CharField(max_length=256, label=u'Website URL', initial='http://', required=False, widget=TextInput())
    services = forms.MultipleChoiceField(required=False, widget=CheckboxSelectMultiple, choices=SERVICES)
    phone = forms.CharField(max_length=256, required=True, widget=TextInput())
    budget = forms.ChoiceField(required=True, choices=BUDGET)
    name = forms.CharField(max_length=256, required=True, widget=TextInput())
    how_to_contact = forms.ChoiceField(label='Contact me via', required=True, choices=CONTACT_METHOD)

  
class HoneyPotContactForm(HoneyPotForm):
    pass

class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        'comment_content': 'content'
    }
    akismet_api_key = None
    

class RecaptchaContactForm(RecaptchaForm):
    recaptcha_public_key = None
    recaptcha_private_key = None
    recaptcha_theme = None
