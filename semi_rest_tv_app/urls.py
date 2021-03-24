from django.urls import path
from . import views
urlpatterns = [
    #display
    path('shows', views.get_shows),
    path('shows/new', views.get_new_show),
    path('shows/<int:id>/edit', views.get_edit_show),
    path('shows/<int:id>', views.get_show_details),

    #action
    path('', views.index), #root is redirect to home page (shows)
    path('shows/create', views.post_new_show),
    path('shows/<int:id>/update', views.post_update),
    path('shows/<int:id>/destroy', views.post_delete),
]