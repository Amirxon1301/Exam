from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maqolalar/', MaqolaView.as_view()),
    path('', register),
    path('login', login_view),
    path('logout/', logout_view),
    path('maqola/<int:pk>/', Bitta_mView.as_view()),


]
