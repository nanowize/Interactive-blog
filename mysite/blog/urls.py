from django.conf.urls import url
from blog import views
from blog.views import UserEditView, EditProfilePageView, ShowProfilePageView, CreateProfilePageView

app_name = 'blog'

urlpatterns = [
    url(r'(?P<id>\d+)/post_edit/$', views.post_edit, name="post_edit"),
    url(r'(?P<id>\d+)/post_delete/$', views.post_delete, name="post_delete"),
    url(r'(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail, name="post_detail"),
    url(r'post_create/$', views.post_create, name="post_create"),
    url(r'settings/$', UserEditView.as_view(), name='settings'),
    url(r'edit_profile_page/(?P<pk>\d+)/$', EditProfilePageView.as_view(), name='edit_profile_page'),
    url(r'user_profile/(?P<pk>\d+)/$', ShowProfilePageView.as_view(), name='user_profile'),
    url(r'create_profile_page/$', CreateProfilePageView.as_view(), name="create_profile_page"),
]
