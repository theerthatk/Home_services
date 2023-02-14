from django.db import models


# Create your models here.
class regmodel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=50)


class empuploadmodel(models.Model):
    choice = [
        ('Electritian', 'Electritian'),
        ('Plumber', 'Plumber'),
        ('Housekeeper', 'Housekeeper'),
        ('Security guard', 'Security guard'),
        ('Gardener', 'Gardener'),
        ('Driver', 'Driver'),
        ('Nanny /Babysitter', 'Nanny /Babysitter'),
        ('Pet caretaker', 'Pet caretaker'),
        ('Mechanic', 'Mechanic'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField()
    services = models.CharField(max_length=20, choices=choice)
    location = models.CharField(max_length=50)
    phone = models.IntegerField()
    # image=models.ImageField()
    bio = models.CharField(max_length=200)


class userregmodel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=50)


class useruploadmodel(models.Model):
    cho = [
        ('Electritian', 'Electritian'),
        ('Plumber', 'Plumber'),
        ('Housekeeper', 'Housekeeper'),
        ('Security guard', 'Security guard'),
        ('Gardener', 'Gardener'),
        ('Driver', 'Driver'),
        ('Nanny /Babysitter', 'Nanny /Babysitter'),
        ('Pet caretaker', 'Pet caretaker'),
        ('Mechanic', 'Mechanic'),
        ('Other', 'Other'),
    ]

    fname = models.CharField(max_length=50)
    email = models.EmailField()
    service = models.CharField(max_length=20, choices=cho)
    phone = models.IntegerField()
    location = models.CharField(max_length=50)


class empapplymodel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=15)
    age = models.IntegerField()
    phone = models.IntegerField()
    service = models.CharField(max_length=30)
    experience = models.IntegerField()


class userapplymodel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=15)
    phone = models.IntegerField()
    service = models.CharField(max_length=30)


class userwishlistmodel(models.Model):
    fname = models.CharField(max_length=50)
    email = models.EmailField()
    service = models.CharField(max_length=20)
    phone = models.IntegerField()
    location = models.CharField(max_length=50)


class empwishlistmodel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    services = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    phone = models.IntegerField()
    bio = models.CharField(max_length=200)
