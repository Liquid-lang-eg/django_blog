from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('add_post/', views.add_post, name='add_post'),
    path('add_post/', views.PostCreateView.as_view(), name='add_post'),
    path('post/<int:pk>/add_comment/', views.CommentCreateView.as_view(), name='add_comment'),
    # path('post/<int:pk>/edit/', views.edit_post, name='edit_post')
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post')
]