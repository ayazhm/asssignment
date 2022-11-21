from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140)

    class Meta:
        managed = False
        db_table = 'diseasetype'
        verbose_name = 'Disease Type'
        verbose_name_plural = 'Disease Types'

    def __str__(self):
        return f"{self.id}"

class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id = models.ForeignKey(Diseasetype, models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'
        verbose_name = 'Disease'
        verbose_name_plural = 'Diseases'

    def __str__(self):
        return f"{self.disease_code}"

class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f"{self.cname}"

class Discover(models.Model):
    cname = models.ForeignKey('Country', models.DO_NOTHING, db_column='cname')
    disease_code = models.OneToOneField(Disease, models.DO_NOTHING, db_column='disease_code', primary_key=True)
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)
        verbose_name = 'Discovered'
        verbose_name_plural = 'Discovered'

    def __str__(self):
        return f"{self.disease_code}"

class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.email}"

class Doctor(models.Model):
    email = models.OneToOneField('Users', on_delete=models.CASCADE, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return f"{self.email}"

class Specialize(models.Model):
    id = models.OneToOneField(Diseasetype, on_delete=models.CASCADE, db_column='id', primary_key=True)
    email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'specialize'
        unique_together = (('id', 'email'),)
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'

    def __str__(self):
        return f"{self.email}"

class Publicservant(models.Model):
    email = models.OneToOneField('Users', on_delete=models.CASCADE, db_column='email', primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicservant'
        verbose_name = 'Public Servant'
        verbose_name_plural = 'Public Servants'

    def __str__(self):
        return f"{self.email}"

class Record(models.Model):
    email = models.OneToOneField('Publicservant', models.DO_NOTHING, db_column='email')
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)
        verbose_name = 'Record'
        verbose_name_plural = 'Records'




