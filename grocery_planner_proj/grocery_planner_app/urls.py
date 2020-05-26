from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path("register", views.register),
    path("logout", views.logout),
    path("success", views.success),
    path("login", views.login),
    path('process_message', views.post_mess),
    path('add_comment/<int:id>', views.post_comment),
    path('user_profile/<int:id>', views.profile),
    path('like/<int:id>', views.add_like),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.edit_page),
    path('process_edit/<int:id>', views.process_edit),
    path('add_item', views.add_item),
    path('remove/<int:id>', views.remove_item), 
    path('grocery_list', views.grocery_list)
]
