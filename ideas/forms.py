from django import forms
from django.forms import ModelForm, Textarea, ChoiceField, TextInput

from .models import Idea

CATEGORIES = (
    ('FIN', 'resource:org.apache.tvmnetwork.Team#FIN'),
    ('TVM', 'resource:org.apache.tvmnetwork.Team#TVM'),
    ('RTM', 'resource:org.apache.tvmnetwork.Team#RTM'),
    # ('FIN', 'FIN'),
    # ('TVM', 'TVM'),
    # ('RTM', 'RTM'),
)

# STAGES = (
#     ('CRID1', 'CRID1'),
#     ('CRID2', 'CRID2'),
#     ('CRID3', 'CRID3'),
#     # ('FIN', 'FIN'),
#     # ('TVM', 'TVM'),
#     # ('RTM', 'RTM'),
# )

class IdeaForm(forms.ModelForm):

    owner = forms.ChoiceField(choices=CATEGORIES, required=True )
    CRID = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Idea ID'}))
    # CRIDStage = forms.ChoiceField(choices=STAGES, required=True )

    class Meta:
        model = Idea
        fields = [ 'CRID', 'market', 'plantCode', 'model', 'tvmCategory', 'ideaType', 'partNumber', 'supplierGSDB', 'description', 'ChangeFrom', 'changeTo', 'ideaInDate', 'bcDate', 'leadFunction', 'spoc', 'ideaSource', 'CRIDStage', 'remark', 'expImpDate', 'weekShownOnImp', 'weekShownForProj',
         'annualSavings', 'calSaving', 'carryOverSavings', 'ageingDays', 'rank', 'GSR', 'ideaGeneratedBy', 'dateOfImp', 'owner']

        # widgets = {
        #     'owner': ChoiceField(choices=CATEGORIES, required=True),
        #
        # }

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=50)
    card_file = forms.FileField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
