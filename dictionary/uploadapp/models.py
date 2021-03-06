from django.db import models

# Create your models here.

class simbol(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=5)
    lang = models.CharField(max_length=5)
    font = models.CharField(max_length=3)
    transkrip = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    pole1 = models.CharField(max_length=200)
    pole2 = models.CharField(max_length=200)
    pole3 = models.CharField(max_length=200)

class oboznach(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=200)
    lang = models.CharField(max_length=2)
    font = models.CharField(max_length=3)
    transkrip = models.CharField(max_length=200)
    udaren = models.IntegerField(max_length=200)
    chast_rechi = models.CharField(max_length=50)
    used = models.CharField(max_length=200)
    pole1 = models.CharField(max_length=100)
    pole2 = models.CharField(max_length=100)
    pole3 = models.CharField(max_length=100)
    pole4 = models.CharField(max_length=100)

class memi(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=300)
    s_ru = models.CharField(max_length=300)
    s_en = models.CharField(max_length=300)
    s_de = models.CharField(max_length=300)
    s_fr = models.CharField(max_length=300)
    s_ua = models.CharField(max_length=300)
    p_ru = models.CharField(max_length=300)
    p_en = models.CharField(max_length=300)
    p_de = models.CharField(max_length=300)
    p_fr = models.CharField(max_length=300)
    p_ua = models.CharField(max_length=300)
    e_ru = models.CharField(max_length=300)
    e_en = models.CharField(max_length=300)
    e_de = models.CharField(max_length=300)
    e_fr = models.CharField(max_length=300)
    e_ua = models.CharField(max_length=300)
    activ = models.BooleanField()
    permis = models.BooleanField()

class sform_ru(models.Model):
    id = models.AutoField(primary_key=True)
    oboznach = models.CharField(max_length=300)
    slovoform = models.CharField(max_length=300)
    transkrip = models.CharField(max_length=200)
    udaren = models.IntegerField(max_length=200)
    pole1 = models.CharField(max_length=100)
    pole2 = models.CharField(max_length=100)
    pole3 = models.CharField(max_length=100)
    pole4 = models.CharField(max_length=100)

class sform_en(models.Model):
    id = models.AutoField(primary_key=True)
    oboznach = models.CharField(max_length=300)
    slovoform = models.CharField(max_length=300)
    transkrip = models.CharField(max_length=200)
    udaren = models.IntegerField(max_length=200)
    pole1 = models.CharField(max_length=100)
    pole2 = models.CharField(max_length=100)
    pole3 = models.CharField(max_length=100)
    pole4 = models.CharField(max_length=100)

class sform_de(models.Model):
    # id = models.AutoField(primary_key=True)
    oboznach = models.CharField(max_length=300)
    slovoform = models.CharField(max_length=300)
    transkrip = models.CharField(max_length=200)
    udaren = models.IntegerField(max_length=200)
    pole1 = models.CharField(max_length=100)
    pole2 = models.CharField(max_length=100)
    pole3 = models.CharField(max_length=100)
    pole4 = models.CharField(max_length=100)

class sform_fr(models.Model):
    # id = models.AutoField(primary_key=True)
    oboznach = models.CharField(max_length=300)
    slovoform = models.CharField(max_length=300)
    transkrip = models.CharField(max_length=200)
    udaren = models.IntegerField(max_length=200)
    pole1 = models.CharField(max_length=100)
    pole2 = models.CharField(max_length=100)
    pole3 = models.CharField(max_length=100)
    pole4 = models.CharField(max_length=100)

class lang_pair_ru_en(models.Model):
    # id = models.AuoField(primary_key=True)
    first_lang = models.CharField(max_length=300)
    second_char = models.CharField(max_length=300)
    first_discr  = models.CharField(max_length=200)
    second_discr  = models.CharField(max_length=200)
    first_e  = models.CharField(max_length=200)
    second_e  = models.CharField(max_length=200)
    active = models.IntegerField(max_length=200)

class lang_pair_ru_de(models.Model):
    # id = models.AuoField(primary_key=True)
    first_lang = models.CharField(max_length=300)
    second_char = models.CharField(max_length=300)
    first_discr  = models.CharField(max_length=200)
    second_discr  = models.CharField(max_length=200)
    first_e  = models.CharField(max_length=200)
    second_e  = models.CharField(max_length=200)
    active = models.IntegerField(max_length=200)

class lang_pair_en_de(models.Model):
    # id = models.AuoField(primary_key=True)
    first_lang = models.CharField(max_length=300)
    second_char = models.CharField(max_length=300)
    first_discr  = models.CharField(max_length=200)
    second_discr  = models.CharField(max_length=200)
    first_e  = models.CharField(max_length=200)
    second_e  = models.CharField(max_length=200)
    active = models.IntegerField(max_length=200)

class gramma(models.Model):
    # id = models.AuoField(primary_key=True)
    role = models.CharField(max_length=50)
    chast_rechi = models.CharField(max_length=50)
    pole1 = models.CharField(max_length=100)
    pole2 = models.CharField(max_length=100)
    pole3 = models.CharField(max_length=100)
    pole4 = models.CharField(max_length=100)
