from django.conf.urls import url
from qa.views import test, new_q, single, popular



urlpatterns = [
    url(r'^$', new_q, name='new_q'),
    url(r'^single/(?P<pk>\d+)/', single, name='single'),
    url(r'^popular/', popular, name='popular'),
]
