from django.forms import ModelForm
from crispy_forms.layout import Layout, Field, Reset, Submit, Button
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from Register_Employer.models import Employer, JobPost
from django.utils.translation import ugettext as _


class EmployerForm(ModelForm):

    class Meta:
        model = Employer
        exclude = ('date_created', 'date_updated', 'is_employer', 'user')

    def __init__(self, *args, **kwargs):
        super(EmployerForm, self).__init__(*args, **kwargs)
        # Init layout form with crispy

        self.helper = FormHelper()
        self.helper.form_action = '/emp/create/'
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(

            Field('user_name', placeholder="enter your username here"),
            Field('first_name', absplaceholder="enter your first name here"),
            Field('last_name', placeholder="enter your last name here"),
            Field('email_address', placeholder="enter your email here"),
            Field('company_name', css_class='text_area',
                  placeholder="e.g DevBox or Freelance"),
            Field('location', placeholder="where you are located"),

            FormActions(
                Submit('submit', _('Register'),
                       css_class='btn btn-primary btn-lg'),
                Reset('reset', _('Reset'), css_class='btn btn-danger btn-lg')
            ),
        )


class JobForm(ModelForm):

    class Meta:
        model = JobPost
        exclude = ('date_created', 'date_updated', 'owner')

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        # Init layout form with crispy
        self.helper = FormHelper()
        self.helper.form_action = '/emp/job/post/'
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Field('title', placeholder="title of the job"),
            Field('description', placeholder="the scope of the job"),
            Field('skills_required',
                  placeholder="programming knowledge separated by commas,e.g HTML,CSS,JS"),
            Field('location', placeholder="where the job is at"),
            FormActions(
                Submit('submit', _('Post'),
                       css_class='btn btn-primary btn-lg'),
                Reset('reset', _('Reset'), css_class='btn btn-danger btn-lg')
            ),
        )
