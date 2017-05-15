from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import FeatureView, FeatureDetailsView


urlpatterns = {
    url(r'^$', FeatureView.as_view(), name="list_create"),
    url(r'^(?P<pk>[0-9]+)/$',
        FeatureDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
