from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings', views.bookings, name="bookings"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]