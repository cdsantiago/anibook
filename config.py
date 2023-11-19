"""app configuration class"""
import os


class Config:
    """configuration parameters"""
    SECRET_KEY = os.getenv('SECRET_KEY')
