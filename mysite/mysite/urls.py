from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import views
#from eccomerce import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name="post_list"),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^register/$', views.register, name="register"),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^comments/delete_own/(?P<id>.*)/$', views.delete_own_comment, name='delete_own_comment'),
    url(r'^oauth/', include('social_django.urls', namespace="social")),
    url(r'^like/$', views.like_post, name="like_post"),
    url(r'^solar/$', views.solar_page, name="solar_page"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
