from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from config.api import api
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout
{ % if cookiecutter.api == 'REST' % }

{ % elif cookiecutter.api == 'GraphQL' % }

{ % endif % }


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    { % if cookiecutter.api == 'REST' % }
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    { % elif cookiecutter.api == 'GraphQL' % }
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG))),
    { % endif % }
]
