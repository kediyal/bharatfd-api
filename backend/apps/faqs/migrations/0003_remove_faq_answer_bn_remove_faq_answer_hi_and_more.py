# Generated by Django 5.1.5 on 2025-01-31 20:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("faqs", "0002_alter_faq_answer_bn_alter_faq_answer_hi_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="faq",
            name="answer_bn",
        ),
        migrations.RemoveField(
            model_name="faq",
            name="answer_hi",
        ),
        migrations.RemoveField(
            model_name="faq",
            name="question_bn",
        ),
        migrations.RemoveField(
            model_name="faq",
            name="question_hi",
        ),
    ]
