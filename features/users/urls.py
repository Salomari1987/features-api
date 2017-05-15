from django.conf.urls import url
from users.views import UserRegistrationAPIView

urlpatterns = [
    url(r'^$', UserRegistrationAPIView.as_view(), name="list_create"),
]
