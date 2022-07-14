from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

# basically override
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Token'