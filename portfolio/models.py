from django.db import models


class Profile(models.Model):
    tagline = models.TextField()
    #
    # def __str__(self):
    #     return self.tagline

class Python(models.Model):
    library = models.CharField(max_length=100)

    def __str__(self):
        return self.library

class Web(models.Model):
    lang = models.CharField(max_length=100)

    def __str__(self):
        return self.lang

class Data(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Testing(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class OS(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Deployment(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class General(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class WorkHistory(models.Model):
    company = models.CharField(max_length=75)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return self.company

class Education(models.Model):
    school = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=75)
    subject = models.CharField(max_length=75)

    def __str__(self):
        return self.school

class References(models.Model):
    full_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
