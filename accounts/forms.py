from django.forms import CharField, TextInput, PasswordInput, Form


class LoginForm(Form):
    username = CharField(label='Username', widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'name': 'username',
        'placeholder': 'Enter Username'
    }))
    password = CharField(label='Password', widget=PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'placeholder': 'Enter Password'
    }))


class RegisterForm(Form):
    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'first_name',
        'name': 'first_name',
        'placeholder': 'Enter First Name'
    }))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'last_name',
        'name': 'last_name',
        'placeholder': 'Enter Last Name'
    }))
    username = CharField(label='Username', widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'name': 'username',
        'placeholder': 'Enter Username'
    }))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password1',
        'name': 'password1',
        'placeholder': 'Password'
    }))
    password2 = CharField(label='Confirm Password', widget=PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password2',
        'name': 'password2',
        'placeholder': 'Confirm Password'
    }))
