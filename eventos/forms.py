from django.forms import ModelForm
from . import models

class RegisterUser(ModelForm):
	class Meta:
		model = models.User
		fields = '__all__'

class LoginUser(ModelForm):
	class Meta:
		model = models.User
		fields = ['correo','password']

 	