from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maqolalar/', MaqolaView.as_view()),
    path('', register),
    path('login', login_view),
    path('logout/', logout_view),
    path('maqola/<int:pk>/', Bitta_mView.as_view()),


]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    ]
