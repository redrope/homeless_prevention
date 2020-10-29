from django.forms import ModelForm
from .models import Contact, HPAPP, Housing, Utilities

#Start of ClientForm
class ClientForm(ModelForm):

    class Meta:
        model = Contact

        fields = [
            "first_name", "middle_initial", "last_name",
            "address1",
            "address2",
            "city",
            "state",
            "zipcode",
            "home_phone",
            "mobile_phone",
            "email",
            "DOB",
            "veteran",

        ]

        labels = {
                'first_name':'First Name ',
                'middle_initial': 'Middle Initial ',
                'last_name': 'Last Name ',
                'address1': 'Address',
                'address2':'Apartment or Unit Number',
                'email':'Email Address',
                'DOB':'Date of Birth',
                'veteran':'Select if you are a Veteran',

        }

        def form_valid(self, form):
            # assign Contact username with current logged in User
            form.save(commit=False)
            form.instance.username = self.request.user
            form.save()

            return super(ClientForm, self).form_valid(form)

            #self.object = form.save(commit=False)
            #self.object.username = self.request.user
            #self.object.save()

            #return super(ContactModelCreate, self).form_valid(form)


#End of ClientForm

class HPAPPForm(ModelForm):
        class Meta:
            model = HPAPP

            fields = [
                "highest_grade_level",
                "disability_deaf",
                "disability_mobility",
                "disability_speech",
                "disability_learning",
                "disability_visual",
                "disability_health",
                "disability_housebound",
                "disability_other",
                "primary_client",
                "assistance_type",
                "housing_type",
                "adults_num",
                "kids_num",
                "elderly_num",
                "income_type",
                "hh_income",
                "crisis_other",
                "crisis_job_related",
                "crisis_health_problems",
                "crisis_expenses",
            ]

            labels = {
                'housing_type':'Type of Housing Assistance',
                'income_type':'Select the Type of Income',
                'hh_income':'Total Monthly Household Income',
                'primary_client':'Select if you are the Primary Lease or Home Owner',
                'highest_grade_level':'Select your highest school grade level',
                'crisis_other':'Explain your situation or crisis.',
                'disability_other':'Add additionals comments about your Disability',                
                'adults_num':'Number of Adults Living in the Home (18 and older)',
                'kids_num':'Number of children (17 and younger) living in the house.',
                'elderly_num':'Number of adults over age 65',

            }


class HousingForm(ModelForm):
        class Meta:
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

            labels = {
                 'll_or_mortage_co': 'Landlord or Mortgage Company',
                 'mailing_address1': 'Mailing Address',
                 'mailing_address2': 'Suite Number',
                 'monthly_payment_amount': 'Monthly Payment Amount',
                 'current_amount_due': 'Current Amount Due',
            }