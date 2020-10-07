from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Contact, HPAPP
from .forms import ClientForm, HPAPPForm

class OwnObjectsMixin():
     """
     Only returns objects that belongs to the current user. Assumes the object
     has a 'user' foreignkey to a User.
     """
     def get_queryset(self):
         username = self.request.user
         return super(OwnObjectsMixin, self).get_queryset().filter(user=username)


# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})


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

#@login_required used in urls.py for CBV
class ContactModelCreate(CreateView):
    #added reverse URL to TestModel in models.py
    model = Contact

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

    def form_valid(self, form):
        #assign Contact username with current logged in User
        form.instance.username = self.request.user

        return super(ContactModelCreate, self).form_valid(form)

#@login_required
class ContactModelList(ListView):
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
        #form.instance.contact = self.request.user

        return super(HPAPPCreate, self).form_valid(form)

class HPAPPDetail(DetailView):
    model = HPAPP

    def get_queryset(self):
        owner = Contact.objects.get(username=self.request.user)
        return self.model.objects.filter(contact=owner) #return object owned by logged in User


class HPAPPUpdate(UpdateView):
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

    def get_queryset(HPAPPUpdate, self):
        qs = super(HPAPPUpdate, self).get_queryset(self)
        owner = Contact.objects.get(username=self.request.user)
        return qs.filter(contact=owner)
        #return self.model.objects.filter(contact=owner) #return object owned by logged in User
