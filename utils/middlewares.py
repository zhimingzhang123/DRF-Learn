from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser

def get_user(request):
    print('1'*50)
    jwt = request.COOKIES.get('jwt_token', None)
    print(jwt)
    if jwt is None:
        user = AnonymousUser()
        return user

class SSOMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # request.user = get_user(request)
        assert hasattr(request, 'session'), (
            "The Django SSO authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE%s setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'sso.middleware.SSOAuthenticationMiddleware'."
        ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.user = SimpleLazyObject(lambda: get_user(request))