from django.conf.urls import url, include
from users.views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    url(r'^register/', UserRegistrationAPIView.as_view(), name="create"),
    url(r'^login/', UserLoginAPIView.as_view(), name="login"),
]
