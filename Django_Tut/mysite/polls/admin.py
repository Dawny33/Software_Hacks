from django.contrib import admin

# Registering the models
from .models import Choice, Question

#For enabling to add choices when creating questions.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


#For adjusting the pub_date and question_text in the admin panel
class QuestionAdmin(admin.ModelAdmin):
    #Puts the pub_date above question_text
    #fields = ['pub_date', 'question_text']

    fieldsets = [
        ("Question text"      ,   {'fields': ['question_text']}),
        ('Date Information'   ,   {'fields': ['pub_date'], 'classes':['collapse']}),
    ]

    #For adding choices.
    inlines = [ChoiceInline]




admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
