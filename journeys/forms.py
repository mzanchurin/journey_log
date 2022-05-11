from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Journey


class JourneyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = Journey
        fields = ('vehicle', 'time', 'length', 'passengers')
        widgets = {
            # 'time': forms.SplitDateTimeWidget
            # 'project': ProjectChoiceWidget(attrs={'data-width': '700px'})
        }
