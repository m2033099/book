from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/detail', views.book_detail, name="book_detail"),
    path('<int:book_id>/edit/', views.book_edit, name="book_edit"),
    path('<int:book_id>/delete/', views.book_delete, name='book_delete'),
    path('add/', views.Book_Add.as_view(), name='book_add'),
    path('<int:book_id>/like/', views.like, name='like'),
    path('<int:book_id>/like/', RedirectView.as_view(url='/book/')),
]
