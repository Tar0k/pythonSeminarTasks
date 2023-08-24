from django.urls import path
from .views import show_contacts, generate_contacts, delete_contacts, AddContactView, EditContactView, RemoveContactView

urlpatterns = [
    path('', show_contacts, name="show_contacts"),
    path('generate_contacts/<int:times>', generate_contacts, name="generate_contacts"),
    path('delete_contacts/', delete_contacts, name="delete_contacts"),
    path('create_contact/', AddContactView.as_view(), name="create_contact"),
    path('edit_contact/<int:pk>', EditContactView.as_view(), name="edit_contact"),
    path("remove_contact/<int:pk>", RemoveContactView.as_view(), name="remove_contact"),
]
