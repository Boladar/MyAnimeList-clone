# Generated by Django 2.0.2 on 2018-05-06 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180430_1059'),
        ('anime_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnimeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='listelement',
            name='anime',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='anime_user_list', to='anime_database.AnimeModel'),
        ),
        migrations.AddField(
            model_name='useranimelist',
            name='list_content',
            field=models.ManyToManyField(blank=True, null=True, related_name='list_content', to='anime_list.ListElement'),
        ),
        migrations.AddField(
            model_name='useranimelist',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='accounts.UserProfile'),
        ),
    ]