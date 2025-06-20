# Generated by Django 4.2.5 on 2023-10-04 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCreator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'Author'), ('ILLUSTRATOR', 'Illustrator')], max_length=20, verbose_name='The role this creator had in the book')),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_names', models.CharField(help_text="The author's first name or names", max_length=50)),
                ('last_names', models.CharField(help_text="The author's last name or names", max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AddField(
            model_name='bookcreator',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.book'),
        ),
        migrations.AddField(
            model_name='bookcreator',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.creator'),
        ),
        migrations.AddField(
            model_name='book',
            name='creator',
            field=models.ManyToManyField(through='reviews.BookCreator', to='reviews.creator'),
        ),
    ]
