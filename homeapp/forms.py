from django import forms

class regform(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=50)

class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=50)

class empuploadform(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    services =forms.CharField(max_length=20)
    location=forms.CharField(max_length=50)
    phone=forms.IntegerField()
    # image=forms.ImageField()
    bio=forms.CharField(max_length=200)


class userregform(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=50)

class userlogform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=50)


class useruploadform(forms.Form):
    fname = forms.CharField(max_length=50)
    email = forms.EmailField()
    service =forms.CharField(max_length=20)
    phone=forms.IntegerField()
    location=forms.CharField(max_length=50)

class empapplyform(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    gender=forms.CharField(max_length=15)
    age=forms.IntegerField()
    phone=forms.IntegerField()
    service=forms.CharField(max_length=30)
    experience=forms.IntegerField()



class userapplyform(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    address=forms.CharField(max_length=15)
    phone=forms.IntegerField()
    service=forms.CharField(max_length=30)
