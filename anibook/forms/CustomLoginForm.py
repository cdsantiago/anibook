from flask_security.forms import LoginForm, EmailValidation
from wtforms import StringField, validators, EmailField, BooleanField


class CustomLoginForm(LoginForm):
    email = EmailField(
        "Email",
        render_kw={"autocomplete": "email"},
        validators=[validators.Optional(), EmailValidation(verify=False)],
    )
    remember = BooleanField("Remember me")
    # Modify other form fields and validation rules as needed
