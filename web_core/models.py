from django.db import models
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class BENHNHAN(models.Model):
    GIOITINH = (
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    )
    id = ShortUUIDField(
        verbose_name='ID bệnh nhân',
        length=10,
        max_length=12,
        prefix="BN",
        alphabet="0123456789",
        primary_key=True)
    ho_ten = models.CharField('Họ tên', max_length = 100)
    gioi_tinh = models.CharField('Giới tính', max_length = 3, choices = GIOITINH)
    ngay_sinh = models.DateField('Ngày sinh', default = '01/01/1990', null=True)
    dia_chi = models.CharField('Địa chỉ', max_length = 255, null = True)
    def __str__(self):
        line = str(self.id) + ' | ' + self.ho_ten
        return line


class DANHMUC(models.Model):
    CATEGORIES = (
        ('Bệnh', 'Bệnh'),
        ('Thuốc', 'Thuốc'),
        ('Đơn vị', 'Đơn vị'),
        ('Cách dùng', 'Cách dùng'),
    )
    id = ShortUUIDField(
        verbose_name='ID Danh mục',
        length=10,
        max_length=12,
        prefix="DM",
        alphabet="0123456789",
        primary_key=True)
    ten = models.CharField('Tên', max_length=255, unique = True)
    loai = models.CharField('Loại', max_length=20, choices=CATEGORIES)
    gia_tri = models.IntegerField('Giá trị', null=True, blank=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.ten


class SUDUNGTHUOC(models.Model):
    id_phieukham = models.ForeignKey('PHIEUKHAM', on_delete = models.CASCADE, verbose_name = 'ID phiếu khám', null = True)
    thuoc = models.ForeignKey(DANHMUC, on_delete = models.CASCADE, limit_choices_to = {'loai':'Thuốc'}, related_name = 'thuoc', verbose_name = 'Thuốc', null = True)
    soluong = models.IntegerField('Số lượng', validators = [MinValueValidator(1)])
    don_vi = models.ForeignKey(DANHMUC, on_delete = models.CASCADE, limit_choices_to = {'loai':'Đơn vị'}, related_name = 'don_vi', verbose_name = 'Đơn vị', null = True)
    cach_dung = models.ForeignKey(DANHMUC, on_delete = models.CASCADE, limit_choices_to = {'loai':'Cách dùng'}, related_name = 'cach_dung', verbose_name = 'Cách dùng', null = True)

class PHIEUKHAM(models.Model):
    id = ShortUUIDField(
        verbose_name='ID phiếu khám',
        length=10,
        max_length=12,
        prefix="PK",
        alphabet="0123456789",
        primary_key=True
    )
    id_benhnhan = models.ForeignKey(BENHNHAN, on_delete = models.CASCADE,verbose_name = 'ID bệnh nhân', null = True)
    ngay_kham = models.DateTimeField('Ngày khám', auto_now_add = True)
    trieu_chung = models.CharField('Triệu chứng', max_length = 100, blank = False)
    loai_benh = models.ForeignKey(DANHMUC, on_delete = models.CASCADE, limit_choices_to = {'loai':'Bệnh'}, related_name = 'benh',verbose_name = 'Loại bệnh',null = True)
    def __str__(self):
        return self.id


class THAMSO(models.Model):
    CATEGORIES = (
        ('Tiền khám', 'Tiền khám'),
        ('Số lượng bệnh nhân tối đa', 'Số lượng bệnh nhân tối đa'),
    )
    loai = models.CharField('Loại', max_length=50, choices=CATEGORIES, primary_key=True)
    now_value = models.IntegerField('Hiện tại', validators=[MinValueValidator(0), MaxValueValidator(10 ** 6)],
                                    default=0)

    def __str__(self):
        return self.loai
