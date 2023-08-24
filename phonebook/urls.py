from django.urls import path
from .views import show_contacts, generate_contacts, delete_contacts, AddContactView

urlpatterns = [
    path('', show_contacts, name="show_contacts"),
    path('generate_contacts/<int:times>', generate_contacts, name="generate_contacts"),
    path('delete_contacts/', delete_contacts, name="delete_contacts"),
    path('create_contact/', AddContactView.as_view(), name="create_contact"),
]
