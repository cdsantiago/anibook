"""configurations module"""

SECRET_KEY = "z8-oCrPLq7H8R2N5U-soOkzfamJ39qylYft02gMdwgU"

# flask-sql alchemy
SQLALCHEMY_DATABASE_URI = "postgresql:///anibook"
SQLALCHEMY_TRACK_MODIFICATIONS = True

# flask-security
SECURITY_PASSWORD_SALT = "281789554452959811915070470802888875921"
# have session and remember cookie be samesite (flask/flask_login)
REMEMBER_COOKIE_SAMESITE = "strict"
SESSION_COOKIE_SAMESITE = "strict"
# This option makes sure that DB connections from the
# pool are still valid. Important for entire application since
# many DBaaS options automatically close idle connections.
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
}
SECURITY_LOGIN_USER_TEMPLATE = "security/custom_login.html"

SECURITY_LOGIN_USER_TEMPLATE = "security/custom_login.html"
SECURITY_REGISTER_USER_TEMPLATE = "security/custom_register.html"
SECURITY_CONFIRMABLE = False
SECURITY_EMAIL_SUBJECT_REGISTER = "Welcome to Anibook!"
SECURITY_POST_REGISTER_VIEW = "/"
SECURITY_DEFAULT_REMEMBER_ME = True
SECURITY_POST_LOGIN_VIEW = "/"


# flask-mail
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "theanimotionteam@gmail.com"
MAIL_PASSWORD = "xvqvdfzgmvuituhl"
SECURITY_REGISTERABLE = True
SECURITY_USERNAME_ENABLE = True
SECURITY_USERNAME_REQUIRED = True
SECURITY_REGISTER_URL = "/signup"
SECURITY_RECOVERABLE = True
SECURITY_RESET_PASSWORD_TEMPLATE = "security/custom_reset.html"
SECURITY_FORGOT_PASSWORD_TEMPLATE = "security/custom_forgot.html"
