from django.conf.urls import url , include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$' , views.post_neighbourhood , name='homepage'),
    url(r'^user/' , views.userpage , name='username'),
    url(r'^accounts/' ,include('registration.backends.simple.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
