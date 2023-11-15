from django import forms

class LoginForm(forms.Form):
    user_account = forms.CharField(label='账号', max_length=30)
    user_password = forms.CharField(label='密码', widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    user_account = forms.CharField(label='账号', max_length=30)
    user_name = forms.CharField(label='姓名', max_length=20)
    user_password = forms.CharField(label='密码', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput)
    user_email = forms.EmailField(label='邮箱', required=False)
    user_phone = forms.CharField(label='电话号码', required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('user_password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("密码和确认密码不匹配")

        return cleaned_data

