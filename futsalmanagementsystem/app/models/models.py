from django.db import models


class Team(models.Model):
    team_id = models.AutoField(auto_created=True, primary_key=True)
    team_name = models.CharField(max_length=100)
    team_image = models.ImageField()

    class Meta:
        db_table = "teams"


class Ground(models.Model):
    ground_id = models.AutoField(auto_created=True, primary_key=True)
    ground_name = models.CharField(max_length=100)
    ground_image = models.ImageField(default='img.jpg')

    class Meta:
        db_table = "grounds"


class Book(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = "books"


class User(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"
