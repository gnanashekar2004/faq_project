from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField() # Rich text support for WYSIWYG editor
    question_hi = models.TextField(blank=True, null=True) # Hindi transalation
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True) # Bengali transalation
    answer_bn = RichTextField(blank=True, null=True)

    def get_translation(self, lang='en'):
        """
        Returns the translation question and answer based on the requested language.
        Defaults to english if translation is unavailable for the requested language.
        """
        return {
            'question': getattr(self, f'question_{lang}',self.question),
            'answer': getattr(self,f'answer_{lang}',self.answer),
        }

    def __str__(self):
        return self.question #Displays question as a string