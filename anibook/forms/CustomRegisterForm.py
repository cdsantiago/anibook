from flask_security.forms import RegisterForm, EmailValidation, ConfirmRegisterForm, NextFormMixin
from wtforms import validators, PasswordField, EmailField, SubmitField

class CustomRegisterForm(RegisterForm,ConfirmRegisterForm, NextFormMixin):
    # Password optional when Unified Signin enabled.
    password_confirm = PasswordField(
        "Confirm password",
        validators=[
            validators.EqualTo("password", message="RETYPE_PASSWORD_MISMATCH"),
            validators.Optional(),
        ],   
    )
    
    email = EmailField(
        "Email",
        render_kw={"autocomplete": "email"},
        validators=[validators.Optional(), EmailValidation(verify=False)],
    )
    
    submit = SubmitField("Sign up")
