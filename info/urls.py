from django.urls import path

from info import views


app_name = 'info'

urlpatterns = [
    path('<int:id>', views.update, name='update'),
]