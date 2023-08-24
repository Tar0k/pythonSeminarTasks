import random
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from faker import Faker
from .models import Contacts
# Create your views here.

fake = Faker("ru-Ru")


def show_contacts(request):
    data = Contacts.objects.all
    context = {"data": data}
    return render(request, "phonebook/contacts.html", context=context)


class AddContactView(CreateView):
    model = Contacts
    fields = ['first_name', 'last_name', 'middle_name', 'phone_number']
    template_name = 'phonebook/create_contact.html'
    success_url = reverse_lazy(show_contacts)


def generate_contacts(request, times):
    if type(times) is not int:
        return HttpResponseBadRequest

    def create_random_person():
        gender = random.choice(['male', 'female'])
        person = {}
        if gender == 'male':
            person['first_name'] = fake.first_name_male()
            person['last_name'] = fake.last_name_male()
            person['middle_name'] = fake.middle_name_male()
        elif gender == 'female':
            person['first_name'] = fake.first_name_female()
            person['last_name'] = fake.last_name_female()
            person['middle_name'] = fake.middle_name_female()
        person['phone_number'] = fake.phone_number()
        return person

    contacts_quantity = Contacts.objects.count()
    for _ in range(times):
        if contacts_quantity < 100:
            new_person = create_random_person()
            Contacts.objects.create(first_name=new_person['first_name'],
                                    last_name=new_person['last_name'],
                                    middle_name=new_person['middle_name'],
                                    phone_number=new_person['phone_number'])

    return redirect(show_contacts)


def delete_contacts(request):
    Contacts.objects.all().delete()
    return redirect(show_contacts)
