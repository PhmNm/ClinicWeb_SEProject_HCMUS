# Generated by Django 4.0.4 on 2022-05-25 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phieukham',
            name='su_dung_thuoc',
        ),
        migrations.AlterField(
            model_name='benhnhan',
            name='ngay_sinh',
            field=models.DateField(default='01/01/1990', null=True, verbose_name='Ngày sinh'),
        ),
        migrations.AlterField(
            model_name='phieukham',
            name='id_benhnhan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_core.benhnhan', verbose_name='ID bệnh nhân'),
        ),
        migrations.RemoveField(
            model_name='phieukham',
            name='loai_benh',
        ),
        migrations.AddField(
            model_name='phieukham',
            name='loai_benh',
            field=models.ForeignKey(limit_choices_to={'loai': 'Bệnh'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benh', to='web_core.danhmuc', verbose_name='Loại bệnh'),
        ),
        migrations.RemoveField(
            model_name='sudungthuoc',
            name='cach_dung',
        ),
        migrations.AddField(
            model_name='sudungthuoc',
            name='cach_dung',
            field=models.ForeignKey(limit_choices_to={'loai': 'Cách dùng'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cach_dung', to='web_core.danhmuc'),
        ),
        migrations.RemoveField(
            model_name='sudungthuoc',
            name='don_vi',
        ),
        migrations.AddField(
            model_name='sudungthuoc',
            name='don_vi',
            field=models.ForeignKey(limit_choices_to={'loai': 'Đơn vị'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='don_vi', to='web_core.danhmuc'),
        ),
        migrations.AlterField(
            model_name='sudungthuoc',
            name='id_phieukham',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_core.phieukham', verbose_name='ID phiếu khám'),
        ),
        migrations.RemoveField(
            model_name='sudungthuoc',
            name='thuoc',
        ),
        migrations.AddField(
            model_name='sudungthuoc',
            name='thuoc',
            field=models.ForeignKey(limit_choices_to={'loai': 'Thuốc'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thuoc', to='web_core.danhmuc'),
        ),
    ]
