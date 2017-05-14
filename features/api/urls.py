from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import FeatureView, FeatureDetailsView


urlpatterns = {
    url(r'^features/$', FeatureView.as_view(), name="list_create"),
    url(r'^features/(?P<pk>[0-9]+)/$',
        FeatureDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
