from django.db import models

class WorkingTime(models.Model):
    begining= models.TimeField() #12-19 7-12 7:30 12:00 7 15kazdy pacient ma svoj cas zamestnanec ho moze upravit aku zaklikne taka bude doba 45 minut 
    end = models.TimeField()
    day = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.day} {self.begining} {self.end}"

class TypeEmployee(models.Model):  #hygienik, sestra, lekar, zubny technik (strojcek), upratovacka
    name=models.CharField(max_length=234) 

    def __str__(self):
        return f"{self.name}"
    

class Employee(models.Model):               
    name= models.CharField(max_length=256)
    surname= models.CharField(max_length=256)
    title= models.CharField(max_length=16)
    type_employee=models.ForeignKey(TypeEmployee, on_delete=models.CASCADE, default='') 
    boss=models.BooleanField(default=False)
    workingtime =models.ManyToManyField(WorkingTime, related_name="employees", blank=True)
    #realworkingtime=


    class Meta:
        ordering=['surname']

    def __str__(self):
        return f"{self.title} {self.name} {self.surname}"



class Patient(models.Model):
    name= models.CharField(max_length=256)
    surname= models.CharField(max_length=256)
    title= models.CharField(max_length=16, blank=True)
    phone= models.IntegerField()
    email= models.CharField(max_length=100, blank=True)
   # rodnecislo=
    #zdravotnapoistovna=
    adrerss=models.CharField(max_length=256)
    Employee= models.ManyToManyField(Employee, related_name="employees", blank=True)

    class Meta:
        ordering=['surname']

    def __str__(self):
        return f"{self.title} {self.name} {self.surname} {self.phone} {self.email}"

class Actions(models.Model): #vykon
    name= models.CharField(max_length=256) #pozor zmena
    #partaction= #00celust sanka 01 celust 02 sanka 03 zuby od 18 az po 14 04 13 az 23 05 24 28 06 38 34 07 33 43 08 44 48
    employee=models.ManyToManyField(TypeEmployee,  blank=True)#pozor
    suma=models.IntegerField()

    def __str__(self):
        return f"{self.action} {self.employee} {self.suma} "


class Visits(models.Model):
    time= models.DateTimeField(auto_now_add=True)# 
    employee=models.ManyToManyField(Employee)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    actions=models.ForeignKey(Actions, on_delete=models.CASCADE)

    class Meta:
        ordering=['time']

    def __str__(self):
        return f"{self.patient} {self.employee} {self.time}"

class TypeWorking(models.Model):
    name=models.CharField(max_length=256) #dovolenka#pn#sanitacia#skolenie#ine
    
    def __str__(self):
        return f"{self.name}"


class RealWorkingTime(models.Model):
    date=models.DateField()
    time_bagining=models.TimeField()
    time_end=models.TimeField()
    typeworking= models.ForeignKey(TypeWorking, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.employee} {self.typeworking}"


class Config(models.Model):
    days_of_holiday=models.IntegerField()
    holiday_typeworking = models.ForeignKey(TypeWorking, on_delete=models.CASCADE)
    time_logout=models.DurationField()#doba odhl. 48hod.
    time_login=models.DurationField()#doba prihlasenia 36hod.

    def __str__(self):
        return f"{self.days_of_holiday} {self.holiday_typeworking}"

