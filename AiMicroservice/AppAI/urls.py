from django.urls import path
from . import views


urlpatterns = [
    path('todo/test', views.getRoutes, name='routes'),
    path('todo/test-auth', views.getProducts, name='products'),
    path('prompts/<str:pk>', views.getPrompts, name='promts-userId'),

]