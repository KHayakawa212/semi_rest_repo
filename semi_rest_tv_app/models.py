from django.db import models
import datetime

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "title should be at least 2 characters"
        for show in Show.objects.all():
            if postData['title'] == show.title:
                errors['title_repeat'] = "Title name is already being used, please choose different title."
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if postData['description']!="":
            if len(postData['description']) < 10:
                errors["description"] = "description should be at least 10 characters"
                
        # datetime object conversion
        date_time_obj = datetime.datetime.strptime(postData['release_date'], '%Y-%m-%d')
        if date_time_obj > datetime.datetime.today():
            errors["release_date"]= "Release date must be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __str__(self):
        s = '\n'
        s += f'Title: {self.title}\n'
        s += f'Network: {self.network}\n'
        s += f'Release Date: {self.release_date}\n'