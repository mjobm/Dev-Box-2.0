from django.forms import ModelForm
from crispy_forms_foundation.forms import *
from crispy_forms_foundation.layout import Layout,Field, Fieldset,Reset,SplitDateTimeField, Row, Column, ButtonHolder, Submit
from Register_Employer.models import Employer,JobPost
from django.utils.translation import ugettext as _

class EmployerForm(ModelForm):

    class Meta:
        model = Employer
        exclude = ('date_created', 'date_updated', 'is_employer')

    def __init__(self, *args, **kwargs):
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action ='/emp/create/'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Field('user_name',placeholder="enter your username here"),
            Field('first_name',placeholder="enter your first name here"),
            Field('last_name',placeholder="enter your last name here"),
            Field('email_address',placeholder="enter your email here"),
            Field('company_name',css_class='text_area',placeholder="e.g DevBox or Freelance"),
            Field('location',placeholder="where you are located"),

            ButtonHolder(
                Submit('submit', _('Register'),css_class='save_btn'),
                Reset('reset',_('Reset'),css_class='reset_btn')
            ),
        )
        super(EmployerForm, self).__init__(*args, **kwargs)


class JobForm(ModelForm):

    class Meta:
        model = JobPost
        exclude = ('date_created', 'date_updated','employer')

    def __init__(self, *args, **kwargs):
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action ='/emp/job/create/'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Field('title',placeholder="title of the job"),
            Field('description',placeholder="the scope of the job"),
            Field('skills_required',placeholder="programming knowledge separated with commas,e.g HTML,CSS,JS"),
            Field('location',placeholder="where the job is at"),
            ButtonHolder(
                Submit('submit', _('Register'),css_class='save_btn'),
                Reset('reset',_('Reset'),css_class='reset_btn')
            ),
        )
        super(JobForm, self).__init__(*args, **kwargs)
