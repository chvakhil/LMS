from django import forms


class create_user_form(forms.Form):
    uname = forms.CharField(label='User Name')
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')
    pwd1 = forms.CharField(widget=forms.PasswordInput,label='Password')
    pwd2 = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')
    email = forms.EmailField()
    a_leaves = forms.IntegerField(label='Annual Leaves')
    s_leaves = forms.IntegerField(label='Sick Leaves')
    wfh_data = forms.IntegerField(label='WorkFromHome Days')

class user_login_form(forms.Form):
    uname = forms.CharField(label="User Name",widget=forms.TextInput())
    print("\n")
    pwd = forms.CharField(widget=forms.PasswordInput,label='Password')
