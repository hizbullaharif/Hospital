from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Employee Model

class Employee_Profile(models.Model):
    status      =   (
        ('active', 'active'),
        ('pending','pending'),
        ('rejected','rejected')
    )
    user        =   models.ForeignKey(User, on_delete = models.DO_NOTHING)
    name        =   models.CharField(max_length=100, blank=False)
    email       =   models.EmailField(null=True, blank=True)
    address     =   models.TextField(max_length=300, blank=True)
    contact     =   models.CharField(max_length=11, blank=False)
    status      =   models.CharField(max_length=8,choices=status)
    is_deleted  =   models.BooleanField(default=False)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)
    
    class Meta:     
        verbose_name_plural = 'Employee Profiles'

    def __str__(self):
        return self.name 

# Degree Model
class Degree(models.Model):
    name        =   models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

# Doctor Department Model
class Department(models.Model):
    name        =   models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.name 


# doctor profile model 

class Doctor_Profile(models.Model):
    user        =   models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name        =   models.CharField(max_length=200, blank=False)
    email       =   models.EmailField(null=True,blank=True)
    address     =   models.TextField(max_length=300, blank=True)
    department  =   models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, related_name='department')
    degree      =   models.ManyToManyField(Degree, related_name='degree')
    contact     =   models.CharField(max_length=11,blank=False)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural =  "Doctor`s Profile"
        
    def __str__(self):
        return self.name 
    
# Package class Model

class Package(models.Model):
    name        =   models.CharField(max_length=200,verbose_name='Package Name')
    detail      =   models.TextField(max_length=400, blank=True, verbose_name='Package details')
    price       =   models.IntegerField(verbose_name='Package Price', default="00")
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =" Packages "


# Patient Model  
class Patient(models.Model):
    gender = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    patient_name        =   models.CharField(max_length=200, blank=False, verbose_name='Patient Name')
    gender              =   models.CharField(max_length=10, choices=gender, blank=False, default='Male')
    age                 =   models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)], blank=False, null=True)
    month               =   models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(0)], blank=True, null=True)
    admit_date          =   models.DateTimeField(auto_now_add=True,verbose_name='Admition Date')
    bed_no              =   models.CharField(max_length=20, verbose_name='Bed No.')
    address             =   models.TextField(max_length=300, blank=True)
    phone               =   models.CharField(max_length=11, blank=True)
    problem             =   models.TextField(max_length=300, blank=True)
    assign_doctor       =   models.ForeignKey(Doctor_Profile, on_delete=models.DO_NOTHING, related_name='doctor')
    patient_father_name =   models.CharField(max_length=100, verbose_name='Father`s Name')
    patient_mother_name =   models.CharField(max_length=100, verbose_name='Mother`s Name')
    guardian_name       =   models.CharField(max_length=100, blank=True, verbose_name='Guardian Name')
    guardian_phone_no   =   models.CharField(max_length=11, blank=True, verbose_name='Guardian`s Phone Number')
    is_leave            =   models.BooleanField(default=False)

    def __str__(self):
        return self.patient_name 

    class Meta:
        verbose_name_plural = "Patients"








