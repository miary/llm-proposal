from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import ProposalModel


class ProposalForm(forms.ModelForm):
    class Meta:
        model = ProposalModel
        fields = '__all__' # ['title', 'description', 'attachment']

    # def __init__(self, *args, **kwargs):
    #     super(ProposalModel, self).__init__(*args, **kwargs) # type: ignore
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save Proposal'))

