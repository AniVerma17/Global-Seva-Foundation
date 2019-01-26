# from django import forms
# from django.forms import ModelForm


# class UserSignupForm(ModelForm):

#     first_name = forms.CharField(
#         required=True
#     )
#     last_name = forms.CharField(
#         required=True
#     )
#     gender = forms.ChoiceField(
#         choices=User.gender_choices,
#         widget=forms.widgets.RadioSelect
#     )
#     mobile = forms.CharField(
#         required = True,
#         label = 'Mobile Number'
#     )
#     password1 = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput,
#         label='Password'
#     )

#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#             'gender',
#             'mobile',
#         ]

