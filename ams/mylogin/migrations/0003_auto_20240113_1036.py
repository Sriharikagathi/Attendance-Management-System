# Generated by Django 3.1.2 on 2024-01-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylogin', '0002_student_branch_student_section_student_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]