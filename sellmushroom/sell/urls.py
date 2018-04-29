from django.urls import path
# from .views import *
from sell.views import form
urlpatterns = [
    path('form/', form ),
]
