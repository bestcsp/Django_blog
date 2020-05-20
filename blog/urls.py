from django.urls import path,include
from . import views
from .views import (PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


urlpatterns = [

    #path('',views.home,name='home'),
    path('',PostListView.as_view(),name='home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('post/new/',PostCreateView.as_view(),name='create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='delete'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user'),
    


    path('about',views.about,name='about'),


]
