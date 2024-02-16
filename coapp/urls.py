from django.urls import path
from coapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home',views.home),
    path('about',views.about),
    path('course',views.course),
    path('login',views.login_user),
     path('logout',views.user_logout),
    path('my_course',views.my_course),
    path('profile',views.profile),
    path('dashboard',views.dashboard),
    path('addcourse/<cid>',views.addcourse),
    path('enroll/<cid>',views.enroll),
  
    path('reg',views.reg),
    path('makepayment',views.makepayment),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)