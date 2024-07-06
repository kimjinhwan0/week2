from django.urls import path
from .views import GetMessageView

urlpatterns = [
    path('get_message/', GetMessageView.as_view(), name='get_message'),
]