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
  
class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(required=False)
    content = forms.CharField(widget=forms.Textarea())
    website_url = forms.CharField(label=u'Website URL', initial='http://', required=False, widget=TextInput(attrs={'class': 'form-field rounded-field'}))
    services = forms.MultipleChoiceField(required=False, widget=CheckboxSelectMultiple, choices=SERVICES)
    phone = forms.CharField(required=True, widget=TextInput(attrs={'class': 'form-field rounded-field'}))
    budget = forms.ChoiceField(required=True, choices=BUDGET)

  
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
