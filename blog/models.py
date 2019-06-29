from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.

def media(instance, filename):
    image = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, image)

class Catalog(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(db_index=True, upload_to=media)

    def get_absolute_url(self):
        return reverse('catalog_detail_url', kwargs={'slug': self.slug})
	# TV
	# a_laptop
	# Phone


    def __str__(self):
        return self.title

# ======================================================================================
# Category

class Category_TV(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='tv_catalog')

    def get_absolute_url(self):
        return reverse('category_tv_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

# ------------------------------------------------------------------------------

class Category_Phone(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='phone_catalog')

    def get_absolute_url(self):
        return reverse('category_phone_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

# -------------------------------------------------------------------------------

class Category_a_laptop(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='a_laptop_catalog')

    def get_absolute_url(self):
        return reverse('category_a_laptop_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

# ==============================================================================




# ==============================================================================
# TV


class LG(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    lgs_tv = models.ForeignKey(Category_TV, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    screen = models.CharField(max_length=30, db_index=True) # Ultra HD 4K (3840x2160 пикселей)
    connect = models.CharField(max_length=30, db_index=True) # Wi-fi
    size = models.CharField(max_length=30, db_index=True) #77 дюймов (195 см)    
    # text = models.TextField(blank=True, db_index=True)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_tv = models.ManyToManyField('Category_TV', blank=True, related_name='lg_tv')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='lg_tv_catalog')

    def get_absolute_url(self):
        return reverse('lg_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


#1

# Change lg

# Catalogs:  TV
# Image:
# Currently: LG_OLED77C9PLA/LG_OLED77C9PLA.jpg


# Slug:
# LG_OLED77C9PLA
# Title:
# LG OLED77C9PLA
# Screen:
# 4K Cinema HDR (3840 × 2160)
# Connect:
# Wi-Fi
# Size:
# 77(дюймы)
# Decimal:
# 175,00

#---------------------------------------------------


#2
# Catalogs:
# Image:
# Currently: LG_OLED77W8/LG_OLED77W8.jpg

# Slug:
# LG_OLED77W8
# Title:
# LG OLED77W8
# Screen:
# 4K Cinema HDR
# Connect:
# Wi-Fi Bluetooth(Low Energy)
# Size:
# 77 (дюймы)
# Decimal:
# 145,00


#------------------------------------------------------

#3

# Catalogs: TV
# Image:
# Currently: LG_SIGNATURE_OLED/LG_SIGNATURE_OLED.jpg

# Image:
# Currently: LG_SIGNATURE_OLED/LG_SIGNATURE_OLED.jpg
# Change: 

# Slug:
# LG_OLED77W9PLA
# Title:
# LG OLED77W9PLA
# Screen:
# 4K Cinema HDR 3840 × 2160
# Connect:
# Wi-Fi
# Size:
# 77 (дюймы)
# Decimal:
# 128,00

# ------------------------------------------------------






class Samsung_TV(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    samsungs_tv = models.ForeignKey(Category_TV, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    screen = models.CharField(max_length=30, db_index=True) # Ultra HD 4K (3840x2160 пикселей)
    connect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    size = models.CharField(max_length=30, db_index=True) #77 дюймов (195 см) 
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_tv = models.ManyToManyField('Category_TV', blank=True, related_name='samsung_tv_tv')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='samsung_tv_tv_catalog')

    def get_absolute_url(self):
        return reverse('samsung_tv_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


# 1
# Catalogs: TV
# Image:
# Currently: 4K_Smart_RU8000/4K_Smart_RU8000.webp


# Slug:
# 4K_Smart_RU8000
# Title:
# Premium UHD 4K Smart TV RU8000
# Screen:
# 3840 x 2160
# Connect:
# Bluetooth
# Size:
# 65(дюймов)
# Decimal:
# 139,00


# --------------------------------

# 2
# Catalogs: TV
# Image:
# Currently: 4K_QLED_2019/4K_QLED_2019.webp

# Slug:
# 4K_QLED_2019
# Title:
# Q90R 4K Smart QLED TV 2019
# Screen:
# 3,840 x 2,160
# Connect:
# Bluetooth
# Size:
# 75 (дюймов),(42.4 кг)
# Decimal:
# 449,00


# ----------------------------------------
# 3
# Catalogs: TV
# Image:
# Currently: 8K_TV_2019/8K_TV_2019.webp

# Slug:
# 8K_TV_2019
# Title:
# Q900R 8K Smart QLED TV 2019
# Screen:
# 7680 x 4320
# Connect:
# Bluetooth WiFi
# Size:
# 98"(дюймов)
# Decimal:
# 499,00






class Sony(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    sonys_tv = models.ForeignKey(Category_TV, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    screen = models.CharField(max_length=30, db_index=True) # Ultra HD 4K (3840x2160 пикселей)
    connect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    size = models.CharField(max_length=30, db_index=True) #77 дюймов (195 см)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_tv = models.ManyToManyField('Category_TV', blank=True, related_name='sony_tv')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='sony_tv_catalog')

    def get_absolute_url(self):
        return reverse('sony_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


#  1
#  Catalogs: TV
# Image:
# Currently: 4K_Smart_RU8000/4K_Smart_RU8000.webp

# Slug:
# 4K_Smart_RU8000
# Title:
# Premium UHD 4K Smart TV RU8000
# Screen:
# 3840 x 2160
# Connect:
# Bluetooth
# Size:
# 65(дюймов)
# Decimal:
# 139,00

# --------------------------------
# 2
# Catalogs: TV
# Image:
# Currently: 4K_QLED_2019/4K_QLED_2019.webp



# Slug:
# 4K_QLED_2019
# Title:
# Q90R 4K Smart QLED TV 2019
# Screen:
# 3,840 x 2,160
# Connect:
# Bluetooth
# Size:
# 75 (дюймов),(42.4 кг)
# Decimal:
# 449,00




# ----------------------------------
# 3
# Catalogs: TV
# Image:
# Currently: 8K_TV_2019/8K_TV_2019.webp

# Slug:
# 8K_TV_2019
# Title:
# Q900R 8K Smart QLED TV 2019
# Screen:
# 7680 x 4320
# Connect:
# Bluetooth WiFi
# Size:
# 98"(дюймов)
# Decimal:
# 499,00







class Panasonic(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    panasonic_tv = models.ForeignKey(Category_TV, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    screen = models.CharField(max_length=30, db_index=True) # Ultra HD 4K (3840x2160 пикселей)
    connect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    size = models.CharField(max_length=30, db_index=True) #77 дюймов (195 см)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_tv = models.ManyToManyField('Category_TV', blank=True, related_name='panasonic_tv')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='panasonic_tv_catalog')

    def get_absolute_url(self):
        return reverse('panasonic_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


# 1
# Catalogs: TV
# Image:
# Currently: TX-42ER250ZZ/TX-42ER250ZZ.jpg

# Slug:
# TX-42ER250ZZ
# Title:
# TX 42ER250ZZ
# Screen:
# 1920×1080
# Connect:
# Wi-fi bluetooth
# Size:
# 42 (дюймов)
# Decimal:
# 239,00


# ---------------------------------
# 2
# Catalogs: TV
# Image:
# Currently: TX-43FSR400/TX-43FSR400.png

# Slug:
# TX-43FSR400
# Title:
# TX 43FSR400
# Screen:
# 1920x1080
# Connect:
# Wi-fi bluetooth
# Size:
# 43 (дюймов)
# Decimal:
# 229,00

# ------------------------------
# 3
# Catalogs: TV
# Image:
# Currently: TX-65FZR950/TX-65FZR950.png

# Slug:
# TX-65FZR950
# Title:
# TX 65FZR950
# Screen:
# 4K PRO HDR (1449 x 837)
# Connect:
# Bluetooth
# Size:
# 65 (дюймов) 164 см
# Decimal:
# 290,00





# ===============================Phone===================================


class Samsung(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    samsung_phone = models.ForeignKey(Category_Phone, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    camera = models.CharField(max_length=30, db_index=True) # 16px
    memory = models.CharField(max_length=30, db_index=True) # 16gb
    connect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_phone = models.ManyToManyField('Category_Phone', blank=True, related_name='samsung_phone')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='samsung_phone_catalog')

    def get_absolute_url(self):
        return reverse('samsung_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


# 1
# Catalogs: Phone
# Image:
# Currently: samsung_a6/samsung_a6.webp

# Slug:
# samsung_a6
# Title:
# Samsung A6
# Camera:
# 16,0 mp
# Memory:
# 32 ГБ
# Connect:
# Wi-fi bluetooth
# Decimal:
# 19,00 


# ----------------------------------

# 2
# Catalogs: Phone

# Image:
# Currently: Galaxy_A9/Galaxy_A9.webp


# Slug:
# Galaxy_A9
# Title:
# Galaxy A9
# Camera:
# 24.0 МП
# Memory:
# 128 ГБ
# Connect:
# Wi-fi bluetooth
# Decimal:
# 113,00


# ----------------------------------

# 3
# Catalogs: Phone
# Image:
# Currently: Galaxy_S8/Galaxy_S8.webp

# Slug:
# Galaxy_S8
# Title:
# Galaxy S8
# Camera:
# 12-Мп 8 Мп (Автофокус)
# Memory:
# 64 ГБ
# Connect:
# Wi-Fi Bluetooth
# Decimal:
# 399,00



class Apple(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    apple_phone = models.ForeignKey(Category_Phone, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    connect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    memory = models.CharField(max_length=30, db_index=True) # 16gb
    camera = models.CharField(max_length=30, db_index=True) # 16px
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_phone = models.ManyToManyField('Category_Phone', blank=True, related_name='apple_phone')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='apple_phone_catalog')

    def get_absolute_url(self):
        return reverse('apple_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


# 1
# Catalogs: Phone
# Image:
# Currently: iphone_6/iphone_6.png

# Slug:
# iphone_6
# Title:
# iphone 6
# Connect:
# Wi-Fi
# Memory:
# 128 gb
# Camera:
# 12 mp
# Decimal:
# 39,00

# ----------------------------------
# 2
# Catalogs: Phone
# Image:
# Currently: iphone_7/iphone_7.png

# Slug:
# iphone_7
# Title:
# iphone 7
# Connect:
# Wi-fi Touch ID
# Memory:
# 128 gb
# Camera:
# 12 mp
# Decimal:
# 34,00


# ----------------------------
# 3
# Catalogs: Phone
# Image:
# Currently: iphone_x/iphone_x.png

# Slug:
# iphone_x
# Title:
# iphone x
# Connect:
# Wi-fi Touch ID
# Memory:
# 64 Гб
# Camera:
# 12 + 12 (двойная)
# Decimal:
# 63,00



class Xiaomi(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    xiaomi_phone = models.ForeignKey(Category_Phone, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    onnect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    memory = models.CharField(max_length=30, db_index=True) # 16gb
    camera = models.CharField(max_length=30, db_index=True) # 16px
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_phone = models.ManyToManyField('Category_Phone', blank=True, related_name='xiaomi_phone')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='xiaomi_phone_catalog')

    def get_absolute_url(self):
        return reverse('xiaomi_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


#  1
# Catalogs: Phone
# Image:
# Currently: Xiaomi_Redmi_7/Xiaomi_Redmi_7.png

# Slug:
# Xiaomi_Redmi_7
# Title:
# Xiaomi Redmi 7
# Onnect:
# Wi-Fi Bluetooth GPS
# Memory:
# 32 gb
# Camera:
# 12px
# Decimal:
# 8,00


# -----------------------------------
# 2
# Catalogs: Phone
# Image:
# Currently: redmi_y1/redmi_y1.jpg

# Slug:
# redmi_y1
# Title:
# redmi y1
# Onnect:
# Wi-fi bluetooth
# Memory:
# 4 gb
# Camera:
# 13px
# Decimal:
# 13,00





# ============================ a laptop ================================


class Mac_OS(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    mac_a_laptop = models.ForeignKey(Category_a_laptop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    touch = models.CharField(max_length=30, db_index=True, blank=True) # Touch ID
    weight = models.CharField(max_length=30, db_index=True) # 1,25 кг
    memory = models.CharField(max_length=30, db_index=True) # 16gb
    onnect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    thickness = models.CharField(max_length=30, db_index=True) # толщина 15,6 мм
    ssd = models.CharField(max_length=30, db_index=True) # SSD‑накопитель до 1,5 ТБ 
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_a_laptop = models.ManyToManyField('Category_a_laptop', blank=True, related_name='mac_os_a_laptop')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='mac_os_a_laptop_catalog')

    def get_absolute_url(self):
        return reverse('mac_os_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

# 1
# Catalogs: a_laptop
# Image:
# Currently: MacBook_Air/MacBook_Air.png

# Slug:
# MacBook_Air
# Title:
# MacBook Air
# Touch:
# Touch ID
# Weight:
# 1,25 кг
# Memory:
# 8 gb
# Onnect:
# Wi-fi bluetooth
# Thickness:
# 1,56 см
# Ssd:
# 512 gb
# Decimal:
# 123,00


# -----------------------------------------
# 2
# Catalogs: a_laptop
# Image:
# Currently: MacBook_Pro/MacBook_Pro.png

# Slug:
# MacBook_Pro
# Title:
# MacBook Pro
# Touch:
# Touch ID
# Weight:
# 1,37 кг
# Memory:
# 8 gb
# Onnect:
# Wi-fi Bluetooth
# Thickness:
# 1,49 см
# Ssd:
# 512 gb
# Decimal:
# 171,00






class ASUS(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    asus_a_laptop = models.ForeignKey(Category_a_laptop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    touch = models.CharField(max_length=30, db_index=True, blank=True) # Touch ID
    weight = models.CharField(max_length=30, db_index=True) # 1,25 кг
    memory = models.CharField(max_length=30, db_index=True) # 16gb
    onnect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    thickness = models.CharField(max_length=30, db_index=True, blank=True) # толщина 15,6 мм
    ssd = models.CharField(max_length=30, db_index=True) # SSD‑накопитель до 1,5 ТБ 
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_a_laptop = models.ManyToManyField('Category_a_laptop', blank=True, related_name='asus_a_laptop')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='asus_a_laptop_catalog')

    def get_absolute_url(self):
        return reverse('asus_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


# 1
# Catalogs:  a_laptop
# Image:
# Currently: ASUS_VivoBook_S13/ASUS_VivoBook_S13.png
 

# Slug:
# ASUS_VivoBook_S13
# Title:
# ASUS VivoBook S13
# Touch:
# Weight:
# 1,2 кг
# Memory:
# 16 gb
# Onnect:
# Wi-fi bluetooth
# Thickness:
# 1,79 см
# Ssd:
# 128 gb SATA SSD
# Decimal:
# 38,00


# ----------------------------------------
# 2
# Catalogs:  a_laptop
# Image:
# Currently: ASUS_VivoBook_S14/ASUS_VivoBook_S14.png


# Slug:
# ASUS_VivoBook_S14
# Title:
# ASUS VivoBook S14
# Touch:
# Weight:
# 1,4 кг
# Memory:
# 16 ГБ
# Onnect:
# Wi-fi bluetooth
# Thickness:
# 1,8 см
# Ssd:
# 1 ТБ HDD
# Decimal:
# 51,00



# ----------------------------------------
# 3
# Catalogs:  a_laptop
# Image:
# Currently: ASUS_F540BA-GQ193T/ASUS_F540BA-GQ193T.png


# Slug:
# ASUS_F540BA-GQ193T
# Title:
# ASUS F540BA-GQ193T
# Touch:
# Weight:
# 2 кг
# Memory:
# 4 gb
# Onnect:
# Wi-fi bluetooth
# Thickness:
# Ssd:
# 500 gb HDD
# Decimal:
# 19,00






class ACER(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    acer_a_laptop = models.ForeignKey(Category_a_laptop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=30, db_index=True)
    touch = models.CharField(max_length=30, db_index=True, blank=True) # Touch ID
    weight = models.CharField(max_length=30, db_index=True) # 1,25 кг
    memory = models.CharField(max_length=30, db_index=True) # 16gb
    onnect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    thickness = models.CharField(max_length=30, db_index=True) # толщина 15,6 мм
    ssd = models.CharField(max_length=30, db_index=True) # SSD‑накопитель до 1,5 ТБ
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    category_a_laptop = models.ManyToManyField('Category_a_laptop', blank=True, related_name='acer_a_laptop')
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='acer_a_laptop_catalog')

    def get_absolute_url(self):
        return reverse('acer_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


# ----------------------------------------
# 1
# Catalogs:  a_laptop
# Image:
# Currently: SWITCH_7_SW713-51GNP-87T1/SWITCH_7_SW713-51GNP-87T1.png


# Slug:
# SWITCH_7_SW713-51GNP-87T1
# Title:
# SWITCH 7 SW713-51GNP-87T1
# Touch:
# Weight:
# 1.6 кг
# Memory:
# 16 gb
# Onnect:
# Wi-fi bluetooth
# Thickness:
# 9 мм
# Ssd:
# 512 gb SSD
# Decimal:
# 125,00


# ----------------------------------------
# 2
# Catalogs:  a_laptop
# Image:
# Currently: ASPIRE_A517-51G-810T/ASPIRE_A517-51G-810T.png


# Slug:
# ASPIRE_A517-51G-810T
# Title:
# ASPIRE A517-51G-810T
# Touch:
# Weight:
# 3 КГ
# Memory:
# 16 gb
# Onnect:
# Wi-fi bluetooth
# Thickness:
# 28 мм
# Ssd:
# HDD (1000 gb)  SSD (128 gb )
# Decimal:
# 76,00

# =====================================================================================

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# =================================================================================





# class Product(models.Model): 
#     catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200, db_index=True)

# Category.objects.values()
# [{'id': 1, 'catalogs_id': 1, 'slug': 'LG'},
#  {'id': 2, 'catalogs_id': 1, 'slug': 'Samsung-TV'},
#  {'id': 3, 'catalogs_id': 1, 'slug': 'Sony'},
#  {'id': 4, 'catalogs_id': 1, 'slug': 'Panasonic'},
#  {'id': 5, 'catalogs_id': 2, 'slug': 'Samsung'},
#  {'id': 6, 'catalogs_id': 2, 'slug': 'Apple'},
#  {'id': 7, 'catalogs_id': 2, 'slug': 'Xiaomi'},
#  {'id': 8, 'catalogs_id': 3, 'slug': 'Apple_OS'},
#  {'id': 9, 'catalogs_id': 3, 'slug': 'ASUS'},
#  {'id': 10, 'catalogs_id': 3, 'slug': 'ACER'}]

# Create your models here.
