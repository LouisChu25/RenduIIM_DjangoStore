from django.urls import path

from . import views

urlpatterns = [
    path('create', views.create_view, name="create"),
    path('', views.list_view, name="list" ),
    path('<id>', views.detail_view, name="details"),
    path('edit/<id>', views.update_view, name="edit"),
    path('delete/<id>', views.delete_view, name="delete")
]