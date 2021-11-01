from django.urls import path
from . import views

urlpatterns = [

    path('report/', views.report, name='report'),
    path('saved/', views.saved, name='saved'),
    path('sent/', views.sent, name='sent'),
    path('savereport/',views.savereport,name='savereport'),


]