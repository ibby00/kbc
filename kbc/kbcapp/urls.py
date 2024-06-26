from django.urls import path
from . import views

urlpatterns = [
    path('kbcapp/', views.kbcapp_list),
    path('kbc_list/', views.KbcAppApi.as_view()),
]