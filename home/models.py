from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    #Choices

    #fields of the model
    username = models.OneToOneField(User, on_delete=models.CASCADE, unique = True, null = True)
    first_name = models.CharField(max_length=200)
    middle_initial = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, default = 'AZ')
    zipcode = models.CharField(max_length=200)
    mobile_phone = models.CharField(max_length=200)
    home_phone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200)
    DOB = models.DateField()
    veteran = models.BooleanField()

    #rename instance of the model
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}'

    #Set the redirect after an Update (POST)
    
    def get_absolute_url(self):
        return reverse('home:contact_detail', args=[self.id])

class HPAPP(models.Model):
        EDUCATION_CHOICES = [('00-08 Grade','00-08 Grade'),('09-12 Non-Graduate','09-12 Non-Graduate'),('High school Diploma or GED','High school Diploma or GED'),('Some College/Trade School','Some College/Trade School'),('Associate Degree','Associate Degree'),('4 Year College Degree','4 Year College Degree'),('Masters Degree','Masters Degree'),('PhD','PhD')]

        HOUSING_TYPE = [('NONE','NONE'),('Rent','Rent'),('Mortgage','Mortgage')]

        INCOME_TYPE = [('Full-Time','Full-Time'),('Part-Time','Part-Time'),('2nd Job','2nd Job'),('3rd Job','3rd Job'),('TANF','TANF'),('SSI','SSI'),('Pension','Pension'),('Unemployment','Unemployment')]

        RACE = [('White','White'),('Black or African American','Black or African American'),('Hispanic or Latino','Hispanic or Latino'),('Asian or Asian American','Asian or Asian American'),('American Indian or Alaska Native','American Indian or Alaska Native'),('Native Hawaiian or other Pacific Islander','Native Hawaiian or other Pacific Islander'),('American Indian or Alaska Native AND White','American Indian or Alaska Native AND White'),('Asian AND White','Asian AND White'),('Black or African American AND White','Black or African American AND White'),('American Indian or Alaska Native AND Black or African American','American Indian or Alaska Native AND Black or African American'),('Other Multiracial','Other Multiracial')]

        ASSISTANCE_REQUESTED = [('Rent/Mortgage','Rent/Mortgage'),('Rent/Mortgage & Utilities','Rent/Mortgage & Utilities')]

        #fields
        contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
        username = models.ForeignKey(User, on_delete=models.CASCADE)
        SSN = models.CharField(max_length=200,blank=True)
        race = models.CharField(max_length=200, choices=RACE)
        highest_grade_level = models.CharField(max_length=200, choices=EDUCATION_CHOICES)
        disability_deaf = models.BooleanField()
        disability_mobility = models.BooleanField()
        disability_speech = models.BooleanField()
        disability_learning = models.BooleanField()
        disability_visual = models.BooleanField()
        disability_health = models.BooleanField()
        disability_housebound = models.BooleanField()
        disability_other = models.TextField(blank=True)
        date_applied = models.DateTimeField(auto_now_add=True)
        date_submitted = models.DateField(null=True, blank=True)
        updated = models.DateTimeField(auto_now=True)
        primary_client = models.BooleanField()
        assistance_type = models.CharField(max_length=200, choices=ASSISTANCE_REQUESTED)
        housing_type = models.CharField(max_length=200, choices=HOUSING_TYPE)
        adults_num = models.IntegerField()
        kids_num = models.IntegerField()
        elderly_num = models.IntegerField()
        income_type = models.CharField(max_length=200, choices=INCOME_TYPE)
        hh_income = models.DecimalField(max_digits=8, decimal_places=2)
        #TODO Add Fields to upload paystubs or pay statements
        crisis_other = models.TextField()
        crisis_job_related = models.BooleanField()
        crisis_health_problems = models.BooleanField()
        crisis_expenses = models.BooleanField()
        #TODO Add Field to upload Crisis Doc such as Umemployment, etc.

        def get_absolute_url(self):
            return reverse('home:hpapp_detail', args=[self.id])

        def __str__(self):
            return f'{self.contact} {self.assistance_type}'

class Housing(models.Model):
        contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
        username = models.ForeignKey(User, on_delete=models.CASCADE)
        ll_or_mortage_co = models.CharField(max_length=250)
        contact_person = models.CharField(max_length=200)
        contact_phone = models.CharField(max_length=20)
        mailing_address1 = models.CharField(max_length=250)
        mailing_address2 = models.CharField(max_length=250)
        city = models.CharField(max_length=200)
        state = models.CharField(max_length=10, default='AZ')
        zipcode = models.CharField(max_length=20)
        monthly_payment_amount = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
        current_amount_due = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)

        def get_absolute_url(self):
            return reverse('home:housing_detail', args=[self.id])

        def __str__(self):
            return f'{self.ll_or_mortage_co} {self.contact_person} {self.contact_phone}'


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Utilities(models.Model):
        UTILITY_TYPE = [('water','Water'), ('electric', 'Electric'), ('gas', 'Gas')]
        UTILITY_PROVIDER = [('SRP', 'SRP'), ('APS', 'APS'), ('Southwest Gas', 'Southwest Gas'), ('City of Phoenix', 'City of Phoenix'), ('City of Mesa', 'City of Mesa'),
                            ('City of Peoria', 'City of Peoria'), ('City of Tempe', 'City of Tempe'), ('City of Glendale', 'City of Glendale'), ('City of Chandler', 'City of Chandler'),
                            ('City of Goodyear', 'City of Goodyear'), ('City of Buckeye', 'City of Buckeye'), ('City of Scottsdale', 'City of Scottsdale'), ('Epcor', 'Epcor'), ('Liberty', 'Liberty')
                            ]

        contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
        username = models.ForeignKey(User, on_delete=models.CASCADE)
        utility_provider = models.CharField(max_length=100, choices=UTILITY_PROVIDER)
        utility_type = models.CharField(max_length=100, choices=UTILITY_TYPE)
        account_no = models.CharField(max_length=200)
        name_on_acct = models.CharField(max_length=200)
        total_amount_due = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
        statement = models.FileField(upload_to=user_directory_path)

#TODO Add Model 'Documents' to upload all necessary documents

