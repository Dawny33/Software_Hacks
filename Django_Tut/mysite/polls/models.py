import datetime

from django.db import models
from django.utils import timezone


#Creating models

class Question(models.Model):
    #For displaying name when using xyz.objects.all()
    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')



class Choice(models.Model):
    #Same as above. Check it, dammit
    def __unicode__(self):
        return self.choice_text

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

#By these models, Django creates a db schema for the app,
#and create a database-access API for accessing Question and Choice.


#So, now add "polls" to the INSTALLED_APPS in settings.py
