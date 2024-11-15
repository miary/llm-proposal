from django.urls import path
from .views import home, proposal

urlpatterns = [
     path('', home, name='home'),
     path('proposal/', proposal, name='proposal')
]

