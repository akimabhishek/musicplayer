from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/',include('music.urls',namespace="music")),
    #url(r'^', include('music.urls')),
    #url('social-auth/',include('social.apps.django_app.urls',namespace='social')),
    #url('',include('social.apps.django_app.urls',namespace='social')),
    #url(r'^',include('social_django.urls',namespace='social')),
    #url(r'^auth-social/',include('social_django.urls',namespace='social'))
    url("^soc/", include("social_django.urls", namespace="social"))
]
