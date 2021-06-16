from django.urls import path

from main import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index-page'),
]
