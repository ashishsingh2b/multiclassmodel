# Generated by Django 4.0.2 on 2024-05-10 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_parentsname_student_parentsname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='Salary',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Subjectname',
            new_name='subjectname',
        ),
    ]