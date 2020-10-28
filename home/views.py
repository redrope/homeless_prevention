from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Contact, HPAPP, Housing, Utilities, Documents
from .forms import ClientForm, HPAPPForm

class OwnObjectsMixin():
     """
     Only returns objects that belongs to the current user. Assumes the object
     has a 'user' foreignkey to a User.
     """
     def get_queryset(self):
         username = self.request.user
         return super(OwnObjectsMixin, self).get_queryset().filter(username=username)


# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})

class StartAppView(TemplateView):
    context_object_name = 'startapp_list'
    template_name = 'home/startapp.html'
    title = 'some title'

    def get_context_data(self, **kwargs):
        context = super(StartAppView, self).get_context_data(**kwargs)
        if Contact.objects.filter(username=self.request.user).exists():
            context['c_info'] = Contact.objects.get(username=self.request.user)
            context['contact_exists'] = True
        else:
            context['contact_exists'] = False

        if HPAPP.objects.filter(username=self.request.user).exists():
            context['hpapp_info'] = HPAPP.objects.get(username=self.request.user)
            context['hpapp_exists'] = True
        else:
            context['hpapp_exists'] = False

        if Housing.objects.filter(username=self.request.user).exists():
            context['housing_info'] = Housing.objects.get(username=self.request.user)
            context['housing_exists'] = True
        else:
            context['housing_exists'] = False

        if Utilities.objects.filter(username=self.request.user).exists():
            context['utils_exists'] = True
        else:
            context['utils_exists'] = False

        return context


"""
    def get_context_data(self, *args, **kwargs):
        context = super(StartAppView, self).get_context_data(*args, **kwargs)
        context['name'] = 'Gryffindor'


        #check if Contact Object exists for User
        if Contact.objects.filter(username=self.request.user).exists():
            qs = Contact.objects.filter(username=self.request.user)
            context['username'] = qs.username
            print(qs.username)
"""


@login_required
def dashboard(request): #TO DO If statement to bypass Dashboard for new user
    #get Contact object based on logged in user
        c_query = Contact.objects.get(username=request.user.id)
        hp_query = HPAPP.objects.get(contact=c_query.id) #Get ForeignKey Contact.id
        print('Owner id is ' + str(int(c_query.id)))

        return render(request, 'home/dashboard.html', {'c_query': c_query, 'hp_query': hp_query})

class DashboardView(ListView):
    context_object_name = 'dashboard'
    template_name = 'home/dashboard.html'


    def get_queryset(self):
        #queryset = Contact.objects.get(username=request.user.id)
    #    self.Contact = get_object_or_404(Contact, username=self.kwargs[self.request.user.id])

        return Contact.objects.filter(username=self.request.user.id)

    #return context

class FAQView(TemplateView):
        template_name = 'home/hpapp_faq.html'


#@login_required used in urls.py for CBV
class ContactModelCreate(CreateView):
    #added reverse URL to TestModel in models.py
    model = Contact

    fields = [
        # "username",
        "first_name", 
        "middle_initial", 
        "last_name",
        "home_phone",
        "mobile_phone",
        "email",
        "address1",
        "address2",
        "city",
        "state",
        "zipcode",
        "DOB",
        "veteran",
    ]

    def form_valid(self, form):
        #assign Contact username with current logged in User
        form.instance.username = self.request.user
        # form.save()

        return super(ContactModelCreate, self).form_valid(form)

#@login_required
class ContactModelList(OwnObjectsMixin, ListView):
    model = Contact

    def get_queryset(self):
        return self.model.objects.filter(username=self.request.user)

    #def index_view(request):
    #   p = Contact.objects.filter(user=request.user)
    #   return render(request, 'app/index.html', {'objects': p})


class ContactModelDetail(DetailView):
    model = Contact

    def get_queryset(self):
        return self.model.objects.filter(username=self.request.user)

class ContactModelUpdate(UpdateView):
    model = Contact

    #Specify the fields
    fields = [
        "first_name", "middle_initial", "last_name",
        "home_phone",
        "mobile_phone",
        "email",
        "address1",
        "address2",
        "city",
        "state",
        "zipcode",
        "DOB",
        "veteran",
    ]
    #can specify success URL to redirect after successful Update
    #success_url = "/"
    #redirect added to Contact Model in models.py

class ContactModelDelete(DeleteView):
    model = Contact

    def get_queryset(self):
        return self.model.objects.filter(username=self.request.user)

    #can specify success URL to redirect after successful Update
    success_url = reverse_lazy('home:contact_list')

class HPAPPCreate(CreateView):
    #added reverse URL to TestModel in models.py
    model = HPAPP

    fields = [
            "assistance_type",
            "primary_client",
            "hh_income",
            "income_type",
            "highest_grade_level",
            "housing_type",
            "adults_num",
            "kids_num",
            "elderly_num",
            "crisis_job_related",
            "crisis_health_problems",
            "crisis_expenses",
            "crisis_other",
            "disability_deaf",
            "disability_mobility",
            "disability_speech",
            "disability_learning",
            "disability_visual",
            "disability_health",
            "disability_housebound",
            "disability_other",

        ]

    def form_valid(self, form):
        #assign Contact username with current logged in User
        form.instance.contact = Contact.objects.get(username=self.request.user)
        form.instance.username = self.request.user

        return super(HPAPPCreate, self).form_valid(form)

class HPAPPDetail(DetailView):
    model = HPAPP

    def get_queryset(self):
        owner = Contact.objects.get(username=self.request.user)
        return self.model.objects.filter(contact=owner) #return object owned by logged in User

class HPAPPUpdate(OwnObjectsMixin, UpdateView):
    model = HPAPP

    fields = [
            "assistance_type",
            "primary_client",
            "hh_income",
            "income_type",
            "highest_grade_level",
            "housing_type",
            "adults_num",
            "kids_num",
            "elderly_num",
            "crisis_job_related",
            "crisis_health_problems",
            "crisis_expenses",
            "crisis_other",
            "disability_deaf",
            "disability_mobility",
            "disability_speech",
            "disability_learning",
            "disability_visual",
            "disability_health",
            "disability_housebound",
            "disability_other",

        ]

    #def get_queryset(HPAPPUpdate, self):
        #qs = super(HPAPPUpdate, self).get_queryset(self)
        #owner = HPAPP.objects.get(username=self.request.user)
        #return qs.filter(contact=owner)
        #return HPAPP.objects.filter(username=self.request.user)
        #return self.model.objects.filter(contact=owner) #return object owned by logged in User

class HousingModelCreate(CreateView):
    #added reverse URL to TestModel in models.py
    #TODO Add labels to field names on the form
    model = Housing
    fields = [
        'll_or_mortage_co',
        'contact_person',
        'contact_phone',
        'mailing_address1',
        'mailing_address2',
        'city',
        'state',
        'zipcode',
        'monthly_payment_amount',
        'current_amount_due',
    ]

    def form_valid(self, form):
        #assign Contact username with current logged in User
        qs = Contact.objects.get(username=self.request.user)
        # form.instance.contact = qs['id']
        form.instance.contact = Contact.objects.get(username=self.request.user)
        form.instance.username = self.request.user #TODO Create filter to get object from Contact Model & User Model

        return super(HousingModelCreate, self).form_valid(form)


class HousingModelDetail(DetailView):
    model = Housing

    def get_queryset(self):
        return self.model.objects.filter(username=self.request.user)

# class HPAPPDetail(DetailView):
#     model = HPAPP

#     def get_queryset(self):
#         owner = Contact.objects.get(username=self.request.user)
#         return self.model.objects.filter(contact=owner) #return object owned by logged in User

class HousingModelList(ListView):
    model = Housing

    def get_queryset(self):
        return self.model.objects.filter(username=self.request.user)

class HousingModelUpdate(UpdateView):
    model = Housing

    #Specify the fields
    #fields = []


    #can specify success URL to redirect after successful Update
    #success_url = "/"
    #redirect added to Contact Model in models.py

class HousingModelDelete(DeleteView):
    model = Housing

    def get_queryset(self):
        return self.model.objects.filter(username=self.request.user)

    #can specify success URL to redirect after successful Update
    success_url = reverse_lazy('home:housing_list')


class UtilitiesModelCreate(CreateView):
    model = Utilities
    fields = [
    'utility_provider',
    'utility_type',
    'account_no',
    'name_on_acct',
    'total_amount_due',
    'statement',
    ]

    def form_valid(self, form):
        form.instance.contact = Contact.objects.get(username = self.request.user)
        form.instance.username = User.objects.get(username = self.request.user)
        return super(UtilitiesModelCreate,self).form_valid(form)


class UtilitiesModelDetail(DetailView):
    model = Utilities

    def get_queryset(self):
        return self.model.objects.filter(username=self.request.user)

class UtilitiesModelUpdate(OwnObjectsMixin, UpdateView):
    model = Utilities
    fields = [
        'utility_provider',
        'utility_type',
        'account_no',
        'name_on_acct',
        'total_amount_due',
        'statement',
    ]
    success_url = reverse_lazy('home:utils_list')

class UtilitiesModelList(OwnObjectsMixin, ListView):
    model = Utilities


class DocumentsModelCreate(OwnObjectsMixin, CreateView):
    model = Documents

class DocumentsModelDetail(OwnObjectsMixin,DetailView):
    model = Documents

class DocumentsModelUpdate(OwnObjectsMixin, UpdateView):
    model = Documents

class DocumentsModelList(OwnObjectsMixin, ListView):
    model = Documents

class SubmitAppView(TemplateView):

    template_name = 'home/submit_app.html'