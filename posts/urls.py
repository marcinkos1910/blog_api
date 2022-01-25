from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostApiList.as_view(), name='list'),
    path('<int:pk>/', views.DetailPost.as_view(), name='detail')
]
