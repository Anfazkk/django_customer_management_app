from django.urls import path

from events import views


app_name = 'events'

urlpatterns = [
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<int:id>', views.edit_event, name='edit_event'),
    path('delete_event/<int:id>', views.delete_event, name='delete_event'),
    path('go/', views.go_back, name='go_back'),
]