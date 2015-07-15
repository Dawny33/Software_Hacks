from django.contrib import admin

# Registering the models
from .models import Question

#For adjusting the pub_date and question_text in the admin panel
class QuestionAdmin(admin.ModelAdmin):
    #Puts the pub_date above question_text
    #fields = ['pub_date', 'question_text']

    fieldsets = [
        ("Question text",                  {'fields': ['question_text']}),
        ('Date Information'   ,   {'fields': ['pub_date']}),
    ]




admin.site.register(Question, QuestionAdmin)
