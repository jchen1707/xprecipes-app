from flask import request, g
from flask_wtf.csrf import validate_csrf

def csrf_validation_middleware(func):
    def wrapper(*args, **kwargs):
        if not validate_csrf(request.form.get("csrf_token")):
            return {"message": "Invalid CSRF token"}, 400
        return func(*args, **kwargs)
    return wrapper
