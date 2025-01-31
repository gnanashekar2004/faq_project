# import asyncio
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def get_translation(self, lang='en'):
        """
        Returns the translated question and answer based on the requested language.
        Defaults to English if translation is unavailable.
        """
        return {
            'question': getattr(self, f'question_{lang}', self.question),
            'answer': getattr(self, f'answer_{lang}', self.answer),
        }

    def __str__(self):
        return self.question
