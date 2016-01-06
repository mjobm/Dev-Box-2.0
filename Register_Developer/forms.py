from django.forms import ModelForm
from crispy_forms_foundation.forms import *
from crispy_forms_foundation.layout import Layout,Field, Fieldset,Reset,SplitDateTimeField, Row, Column, ButtonHolder, Submit
from .models import Developer,Portfolio
from django.utils.translation import ugettext as _


class ProfileForm(ModelForm):

    class Meta:
        model = Developer
        exclude = ('date_created', 'date_updated')

    def __init__(self, *args, **kwargs):
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action ='/dev/profile/create/'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(

            Field('first_name',placeholder="enter your first name here"),
            Field('last_name',placeholder="enter your last name here"),
            Field('email_address',placeholder="enter your email here"),
            Field('bio',css_class='text_area',placeholder="e.g what you do & are as an engineer"),
            Field('languages',placeholder="separate with commas e.g. html,css,javascript,python,django"),
            Field('software_title',placeholder="software engineering title e.g backend-engineer"),
            Field('years_exp'),
            Field('profile_picture',placeholder="a url for you profile picture"),
            Field('website_url',placeholder="a url to your website"),

            ButtonHolder(
                Submit('submit', _('Register'),css_class='save_btn'),
                Reset('reset',_('Reset'),css_class='reset_btn')
            ),
        )
        super(ProfileForm, self).__init__(*args, **kwargs)

# Portfolio Form


class PortfolioForm(ModelForm):

    class Meta:
        model = Portfolio
        exclude = ('date_created', 'date_updated','owner')

    def __init__(self, *args, **kwargs):
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action ='/dev/profile/create/portfolio/'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(

            Field('title',css_class='portfolio_title'),
            Field('image',css_class='portfolio_image'),
            Field('description',css_class='text_area'),
            Field('github_link',css_class='portfolio_link'),

            ButtonHolder(
                Submit('submit', _('Create'),css_class='save_btn'),
                Reset('reset',_('Reset'),css_class='reset_btn')
            ),

        )
        super(PortfolioForm, self).__init__(*args, **kwargs)
