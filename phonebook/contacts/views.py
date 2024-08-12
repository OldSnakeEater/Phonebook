from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Contact
from .forms import AddContactForm, SearchContactForm, ChangeContactForm
from django.core.paginator import Paginator
import os


def contact_view(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            form = AddContactForm(request.POST, request.FILES)
            search = SearchContactForm()
            if form.is_valid():
                contact_name = form.cleaned_data['name']
                contact_subdivision = form.cleaned_data['subdivision']
                contact_number = form.cleaned_data['number']
                contact_email = form.cleaned_data['email']
                contact_jobtitle = form.cleaned_data['jobtitle']
                contact_image = form.cleaned_data['image']
                contact = Contact.objects.create(name=contact_name, subdivision=contact_subdivision,
                                                 number=contact_number, jobtitle=contact_jobtitle,
                                                 mail=contact_email, photo=contact_image)
                contact.save()
                form = AddContactForm()
                return render(request, 'contacts/phonebook.html', {'search': search, 'form': form})
        elif 'ContactChangeModalButton' in request.POST:
            contact_id = request.POST.get('changeContactId')
            contact = Contact.objects.get(id=contact_id)
            if contact.photo and (request.POST.get('photo') != ""):
                for filename in os.listdir('media/images'):
                    if ''.join(['images/', filename]) == str(contact.photo):
                        os.remove(os.path.join('media/images/', filename))
            change_contact = ChangeContactForm(request.POST, request.FILES, instance=contact)
            if change_contact.is_valid():
                change_contact.save()
            search = SearchContactForm()
            form = AddContactForm()
            return render(request, 'contacts/phonebook.html', {'search': search, 'form': form})

        elif 'delete_contact' in request.POST:
            contact_id = request.POST.get('delete_contact')
            contact = Contact.objects.get(id=contact_id)
            if request.POST.get('photo') != '':
                for filename in os.listdir('media/images'):
                    if ''.join(['images/', filename]) == str(contact.photo):
                        os.remove(os.path.join('media/images/', filename))
            contact.delete()
            search = SearchContactForm()
            form = AddContactForm()
            return render(request, 'contacts/phonebook.html', {'search': search, 'form': form})
    elif request.method == "GET":
        search = SearchContactForm(request.GET)
        if search.is_valid():
            ser_name = search.cleaned_data['searchName']
            ser_number = search.cleaned_data['searchNumber']
            ser_subdivision = search.cleaned_data['searchSubdivision']
            ser_jobtitle = search.cleaned_data['searchJobTitle']
            ser_mail = search.cleaned_data['searchEmail']
            data = Contact.objects.filter(number__contains=ser_number, name__contains=ser_name,
                                          subdivision__contains=ser_subdivision,
                                          jobtitle__contains=ser_jobtitle, mail__contains=ser_mail)

            paginator = Paginator(data, 3)
            page_number = request.GET.get('page')
            data = paginator.get_page(page_number)
            form = AddContactForm()
            change_contact = ChangeContactForm()
            return render(request, 'contacts/phonebook.html', {'search': search, 'form': form,
                                                               'searched_data': data, 'change_contact': change_contact})


def download_contacts_json(request):
    contacts = Contact.objects.all()
    data = serializers.serialize('json', contacts)

    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="contacts.json"'
    return response

# Create your views here.
