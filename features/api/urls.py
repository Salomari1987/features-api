from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import FeatureView


urlpatterns = {
    url(r'^features/$', FeatureView.as_view(), name="features"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
