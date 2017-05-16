from django.conf.urls import url, include
from users.views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    url(r'^register/', UserRegistrationAPIView.as_view(), name="create"),
    url(r'^login/', UserLoginAPIView.as_view(), name="login"),
    url(r'^logout/', UserLogoutAPIView.as_view(), name="logout"),

]
