# Generated by Django 5.1.5 on 2025-01-31 18:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq_app", "0002_alter_faq_answer_hi_alter_faq_question_hi"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="answer_hi",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="faq",
            name="question_hi",
            field=models.TextField(blank=True, null=True),
        ),
    ]
