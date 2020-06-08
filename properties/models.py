from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    level = models.IntegerField(default=1)


class Sleep(models.Model):
    post = models.IntegerField(default=0) #postId
    user_no = models.IntegerField(default=0)
    time = models.IntegerField(default=0, blank=True)
    physical_activity = models.IntegerField(default=0, blank=True)
    food_consumption = models.IntegerField(default=0, blank=True)
    dream_remembered = models.IntegerField(default=0, blank=True)
    day = models.IntegerField(default=0, blank=True)
    month = models.IntegerField(default=0, blank=True)
    year = models.IntegerField(default=0, blank=True)


class Dream(models.Model):
    user_no = models.IntegerField(default=0)
    post = models.IntegerField(default=0) #postId
    people_exist = models.IntegerField(default=0, blank=True, null=True)
    sound = models.IntegerField(default=0, blank=True, null=True)
    musical = models.IntegerField(default=0, blank=True, null=True)
    grayscale = models.IntegerField(default=0, blank=True, null=True)
    experience = models.IntegerField(default=0, blank=True, null=True)
    lucidity = models.IntegerField(default=0, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(max_length=1000000, blank=True, null=True)
    interpretation = models.CharField(max_length=1000000, blank=True, null=True)
    day = models.IntegerField(default=0, blank=True, null=True)
    month = models.IntegerField(default=0, blank=True, null=True)
    year = models.IntegerField(default=0, blank=True, null=True)


class People(models.Model):
    user_no = models.IntegerField(default=0)
    post = models.IntegerField(default=0) #postId
    first_name = models.CharField(max_length=255, blank=True)
    second_name = models.CharField(max_length=255, blank=True)
    third_name = models.CharField(max_length=255, blank=True)
    fourth_name = models.CharField(max_length=255, blank=True)
    fifth_name = models.CharField(max_length=255, blank=True)
    sixth_name = models.CharField(max_length=255, blank=True)
    seventh_name = models.CharField(max_length=255, blank=True)
    eighth_name = models.CharField(max_length=255, blank=True)
    ninth_name = models.CharField(max_length=255, blank=True)
    tenth_name = models.CharField(max_length=255, blank=True)
    first_impression = models.IntegerField(default=0, blank=True)
    second_impression = models.IntegerField(default=0, blank=True)
    third_impression = models.IntegerField(default=0, blank=True)
    fourth_impression = models.IntegerField(default=0, blank=True)
    fifth_impression = models.IntegerField(default=0, blank=True)
    sixth_impression = models.IntegerField(default=0, blank=True)
    seventh_impression = models.IntegerField(default=0, blank=True)
    eighth_impression = models.IntegerField(default=0, blank=True)
    ninth_impression = models.IntegerField(default=0, blank=True)
    tenth_impression = models.IntegerField(default=0, blank=True)


class QuestionnaireEntry(models.Model):
    user_no = models.IntegerField(default=0)
    post = models.IntegerField(default=0) # postID
    q1 = models.IntegerField(default=0, blank=True)
    q2 = models.IntegerField(default=0, blank=True)
    q3 = models.IntegerField(default=0, blank=True)
    q4 = models.IntegerField(default=0, blank=True)
    q5 = models.IntegerField(default=0, blank=True)
    q6 = models.IntegerField(default=0, blank=True)
    q7 = models.IntegerField(default=0, blank=True)
    q8 = models.IntegerField(default=0, blank=True)
    q9 = models.IntegerField(default=0, blank=True)
    q10 = models.IntegerField(default=0, blank=True)
    q11 = models.IntegerField(default=0, blank=True)
    q12 = models.IntegerField(default=0, blank=True)
    q13 = models.IntegerField(default=0, blank=True)
    q14 = models.IntegerField(default=0, blank=True)
    q15 = models.IntegerField(default=0, blank=True)
    q16 = models.IntegerField(default=0, blank=True)
    q17 = models.IntegerField(default=0, blank=True)
    q18 = models.IntegerField(default=0, blank=True)
    q19 = models.IntegerField(default=0, blank=True)
    result = models.IntegerField(default=0, blank=True)
