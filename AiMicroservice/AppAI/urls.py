from django.urls import path
from . import views


urlpatterns = [
    path('todo/test', views.getRoutes, name='routes'),
    path('todo/test-auth', views.getProducts, name='products'),
    path('prompts/<str:pk>', views.getPrompts, name='promts-userId'),
    path('prompts/delete/<str:pk>', views.deletePromptById, name='promts-delete'),
    path('create', views.createPrompt, name='promts-create'),

]