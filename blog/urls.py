from django.urls import path,include
import blog.views

urlpatterns = [
    path('HelloWorld', blog.views.HelloWorld),
    path('content',blog.views.content),
    path('index',blog.views.getIndexPage),
    path('detail/<int:articleId>',blog.views.getDetailPage)
]