# from django import forms

# # class ClaimForm(forms.form):
# #     case_id=forms.CharField(max_length=20)
# #     policy_id=forms.charField(max_length=20)
# #     claim_date = forms.DateField()
# #     sum_insured_inr = forms.PositiveIntegerField(min_value=0)
# #     decision = forms.CharField(max_length=30)



from django import forms
from .models import Claim


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim
        fields = '__all__'