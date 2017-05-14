from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import FeatureView, FeatureDetailsView


urlpatterns = {
    url(r'^features/$', FeatureView.as_view(), name="list_create"),
    url(r'^features/(?P<pk>[0-9]+)/$',
        FeatureDetailsView.as_view(), name="details"),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
}

urlpatterns = format_suffix_patterns(urlpatterns)
