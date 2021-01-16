from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from registration import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookshelf/', include('bookshelf.urls')),
    # urlが何もない時に、Home画面に移動させる。
    path('', RedirectView.as_view(url='bookshelf/')),
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("send_mail/", views.SendMailView.as_view(), name="send_mail"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),

]
