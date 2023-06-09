from django.db import models

class About_me(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_icon = models.ImageField(upload_to='images/')
    skill_description = models.TextField()
    skill_document = models.TextField()

    def __str__(self):
        return self.skill_name

class Education(models.Model):
    education_name = models.CharField(max_length=100)
    education_icon = models.ImageField(upload_to='images/')
    education_description = models.TextField()
    education_link = models.CharField(max_length=100)

    def __str__(self):
        return self.education_name
    
class Experience(models.Model):
    experience_name = models.CharField(max_length=100)
    experience_description = models.TextField()
    experience_link = models.CharField(max_length=100)

    def __str__(self):
        return self.experience_name
    
class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='images/')
    project_link = models.CharField(max_length=100)
    project_github = models.CharField(max_length=100)
    about_me = models.ForeignKey(About_me, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
