from django.db import models


class AuthenticationCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=500)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    url = models.CharField(max_length=100, null=True)

    class Meta:
        managed = False
        db_table = 'authentication_customuser'


class Project(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    inference_description = models.TextField()
    inference_name = models.CharField(max_length=20)
    url = models.CharField(max_length=100, null=True)
    order_num = models.IntegerField()

    def __str__(self):
        return self.name


class Step(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100, null=True)
    order_num = models.IntegerField()

    def __str__(self):
        return self.name
