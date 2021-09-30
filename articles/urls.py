from django.urls import path
from . import views


urlpatterns = [
      path('articles/',views.article_view,name='blog'),
      path('create/',views.create_view,name='create'),
      path('show/<int:id>/',views.show_view, name='show'),
]