from django.urls import path

from blog.views import post_list, post_detail

app_name = 'blog'
urlpatterns = [
    # post views
    path('', post_list, name='post_list'),
    path('<int:year>/int:month/<int:day>/<slug:poat>/', post_detail, name='post_detail'),
]
