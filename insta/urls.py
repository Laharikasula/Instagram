from django.urls import path
from insta import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='instapost'),
    path('create',views.create,name='createpost'),
    path('login',views.login_view,name='loginpage'),
    path('register',views.register_view,name='registerpage'),
    path('logout',views.logoutView,name='logoutpage'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)