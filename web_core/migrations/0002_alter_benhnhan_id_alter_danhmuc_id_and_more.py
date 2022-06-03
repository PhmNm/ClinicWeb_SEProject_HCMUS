# Generated by Django 4.0.4 on 2022-06-03 10:59

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('web_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benhnhan',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='BN', primary_key=True, serialize=False, verbose_name='ID bệnh nhân'),
        ),
        migrations.AlterField(
            model_name='danhmuc',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='DM', primary_key=True, serialize=False, verbose_name='ID Danh mục'),
        ),
        migrations.AlterField(
            model_name='phieukham',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='PK', primary_key=True, serialize=False, verbose_name='ID phiếu khám'),
        ),
    ]
