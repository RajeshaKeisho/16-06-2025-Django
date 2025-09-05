from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.article_list, name='article_list'),
    path('blog/about/', views.about_view, name='about'),
    path('blog/contact/', views.contact_view, name='contact'),
]
