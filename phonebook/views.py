import random
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from faker import Faker
from .models import Contacts

# Create your views here.

fake = Faker("ru-Ru")


def show_contacts(request):
    if request.method == "POST":
        data = Contacts.objects
        if request.POST["first_name"] != "":
            data = data.filter(first_name__contains=request.POST["first_name"])
        if request.POST["middle_name"] != "":
            data = data.filter(middle_name__contains=request.POST["middle_name"])
        if request.POST["last_name"] != "":
            data = data.filter(last_name__contains=request.POST["last_name"])
        if request.POST["phone_number"] != "":
            data = data.filter(phone_number__contains=request.POST["phone_number"])
        data = data.all()
    else:
        data = Contacts.objects.all()
    context = {"data": data}
    return render(request, "phonebook/contacts.html", context=context)


class AddContactView(CreateView):
    template_name = 'phonebook/create_contact.html'
    model = Contacts
    fields = ['first_name', 'last_name', 'middle_name', 'phone_number']
    success_url = reverse_lazy(show_contacts)


class EditContactView(UpdateView):
    template_name = 'phonebook/edit_contact.html'
    model = Contacts
    fields = ['first_name', 'last_name', 'middle_name', 'phone_number']
    success_url = reverse_lazy(show_contacts)


class RemoveContactView(DeleteView):
    template_name = 'phonebook/remove_contact.html'
    model = Contacts
    success_url = reverse_lazy(show_contacts)


def generate_contacts(request, times):
    if type(times) is not int:
        return HttpResponseBadRequest

    def create_random_person():
        gender = random.choice(['male', 'female'])
        match gender:
            case 'male':
                contact = Contacts(first_name=fake.first_name_male(),
                                   last_name=fake.last_name_male(),
                                   middle_name=fake.middle_name_male(),
                                   phone_number=fake.phone_number())
            case 'female':
                contact = Contacts(first_name=fake.first_name_female(),
                                   last_name=fake.last_name_female(),
                                   middle_name=fake.middle_name_female(),
                                   phone_number=fake.phone_number())
            case _:
                contact = None
        return contact

    contacts_quantity = Contacts.objects.count()
    if contacts_quantity + times < 100:
        new_contacts = []
        for _ in range(times):
            new_contacts.append(create_random_person())
        Contacts.objects.bulk_create(new_contacts)
    return redirect(show_contacts)


def delete_contacts(request):
    Contacts.objects.all().delete()
    return redirect(show_contacts)
