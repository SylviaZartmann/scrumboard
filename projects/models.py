from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import CustomUser


class Client(models.Model):
    name = models.CharField(max_length=150)
    phone = PhoneNumberField(default='')
    first_contact = models.DateField(default='')
    origin_city = models.CharField(max_length=50)
    origin_street = models.CharField(max_length=50)
    origin_post_code = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    firstname = models.CharField(default='', max_length=50)
    lastname = models.CharField(default='', max_length=50)
    email = models.EmailField(default='')
    phone = PhoneNumberField(default='')
    company= models.OneToOneField(
        Client, 
        default='', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True)
    color = models.CharField(
        default="#000000", 
        max_length=7)
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Contract(models.Model):
    CONTRACTING_KINDS = [
        ('estimation', 'Kostenschätzung'),
        ('calculation', 'Kostenberechnung'),
        ('tender', 'Ausschreibung'),
    ]
        
    number = models.CharField(
        default='', 
        max_length=10
        )
    contracting_date = models.DateField(
        default=None, 
        blank=False, 
        null=True
        )
    contracting_kind = models.CharField(
        max_length=20, 
        choices=CONTRACTING_KINDS, 
        default=""
        )
    order_value = models.IntegerField(default='')
    contractor = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, related_name='contractor', 
        default=''
        )
    client = models.ForeignKey(
        Client, 
        default='', 
        on_delete=models.SET_NULL, 
        null=True)
    date_start = models.DateField(
        default=None, 
        blank=False, 
        null=True)
    date_end = models.DateField(
        default=None, 
        blank=False, 
        null=True)
    precessing_time = models.DurationField(default='')
    
    
    
class Project(models.Model):
    name = models.CharField(
        default="", 
        max_length=50
    )
    contract = models.OneToOneField(
        Contract, 
        on_delete=models.SET_NULL, 
        default="", 
        null=True, 
        blank=True
    )
    shortage = models.CharField(
        default="", 
        max_length=5
    )
    project_lead = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        default="",
        related_name="lead_projects",
    )
    project_team = models.ManyToManyField(
        CustomUser, 
        default="", 
        related_name="team_projects"
    )
    client = models.OneToOneField(
        Client, 
        on_delete=models.SET_NULL, 
        default="", 
        null=True
    )
    processing_time = models.DurationField(
        default=""
    )
    date_start = models.DateField(
        default=None, 
        blank=False, 
        null=True
    )
    date_end = models.DateField(
        default=None, 
        blank=False, 
        null=True
    )
    features = models.CharField(
        default="", 
        max_length=500
    )

    def __str__(self):
        return self.name
    
    
    
