from django.contrib import admin

# Registering the models
from .models import Question

#For putting the pub_date above question_text in the admin panel
class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    


admin.site.register(Question, QuestionAdmin)
