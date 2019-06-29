from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
# from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import *
from .utils import *

# Create your views here.

# def Функция просмотра или вид для краткости, это просто функция,
#  которая принимает Python веб - запрос и возвращает веб - ответ.
def catalog_list(request):
    catalogs = Catalog.objects.all()
    context = {
        'catalogs': catalogs,
    }
    return render(request, 'blog/catalog_list.html', context=context)


class CatalogDetail(ObjectDetailMixin, View):
    model = Catalog
    template = 'blog/catalog_detail.html'

    # def get(self, request, slug):
    #     # catalog = Catalog.objects.get(slug__iexact=slug)
    #     catalog = get_object_or_404(Catalog, slug__iexact=slug)
    #     context = {
    #     'catalog': catalog,
    #     }
    #     return render(request, 'blog/catalog_detail.html', context=context)


# def catalog_detail(request, slug):
#     catalog = Catalog.objects.get(slug__iexact=slug)
#     context = {
#         'catalog': catalog,
#     }
#     return render(request, 'blog/catalog_detail.html', context=context)


# ==================================category=================================
# ----------------------------------TV---------------------------------

def category_tvs_list(request):
    category_tvs = Category_TV.objects.all()
    context = {
        'category_tvs': category_tvs,
    }
    return render(request, 'blog/tv/category_tv_list.html', context=context)


class Category_TVDetail(ObjectDetailMixin, View):
    model = Category_TV
    template = 'blog/tv/category_tv_detail.html'

    # def get(self, request, slug):
    #     # category_tv = Category_TV.objects.get(slug__iexact=slug)
    #     category_tv = get_object_or_404(Category_TV, slug__iexact=slug)
    #     context = {
    #     'category_tv': category_tv,
    #     }
    #     return render(request, 'blog/tv/category_tv_detail.html', context=context)

# def category_tv_detail(request, slug):
#     category_tv = Category_TV.objects.get(slug__iexact=slug)
#     context = {
#         'category_tv': category_tv,
#     }
#     return render(request, 'blog/tv/category_tv_detail.html', context=context)

# ---------------------Phone---------------------------------------------------

def category_phones_list(request):
    category_phones = Category_Phone.objects.all()
    context = {
        'category_phones': category_phones,
    }
    return render(request, 'blog/phone/category_phone_list.html', context=context)


class Category_PhoneDetail(ObjectDetailMixin, View):
    model = Category_Phone
    template = 'blog/phone/category_phone_detail.html'
    # def get(self, request, slug):
    #     # category_phone = Category_Phone.objects.get(slug__iexact=slug)
    #     category_phone = get_object_or_404(Category_Phone, slug__iexact=slug)
    #     context = {
    #     'category_phone': category_phone,
    #     }
    #     return render(request, 'blog/phone/category_phone_detail.html', context=context)

# def category_phone_detail(request, slug):
#     category_phone = Category_Phone.objects.get(slug__iexact=slug)
#     context = {
#         'category_phone': category_phone,
#     }
#     return render(request, 'blog/phone/category_phone_detail.html', context=context)

# ---------------------------a_laptop-----------------------------------------------

def category_a_laptops_list(request):
    category_a_laptops = Category_a_laptop.objects.all()
    context = {
        'category_a_laptops': category_a_laptops,
    }
    return render(request, 'blog/a_laptop/category_a_laptop_list.html', context=context)


class Category_a_laptopDetail(ObjectDetailMixin, View):
    model = Category_a_laptop
    template = 'blog/a_laptop/category_a_laptop_detail.html'
    
    # def get(self, request, slug):
        # category_a_laptop = Category_a_laptop.objects.get(slug__iexact=slug)
        # category_a_laptop = get_object_or_404(Category_a_laptop, slug__iexact=slug)
        # context = {
        # 'category_a_laptop': category_a_laptop,
        # }
        # return render(request, 'blog/a_laptop/category_a_laptop_detail.html', context=context)

# def category_a_laptop_detail(request, slug):
#     category_a_laptop = Category_a_laptop.objects.get(slug__iexact=slug)
#     context = {
#         'category_a_laptop': category_a_laptop,
#     }
#     return render(request, 'blog/a_laptop/category_a_laptop_detail.html', context=context)

# =========================================================================
# =================================== TV ==================================
# -----------------------------------lg-------------------------------------
# def lgs_list(request, slug):
#     lgs = LG.objects.all()
#     lg_catalog = LG.objects.get(slug__iexact=slug)
#     context = {
#         'lgs': lgs,
#         'lg_catalog': lg_catalog,
#     }
#     return render(request, 'blog/tv/lg_list.html', context=context)


# def lg_detail(request, slug):
#     lg = LG.objects.get(slug__iexact=slug)
#     context = {
#         'lg': lg,
#     }
#     return render(request, 'blog/tv/lg_detail.html', context=context)


# ----------------------------------samsung_tv-------------------------------

# def samsung_tvs_list(request):
#     samsung_tvs = Samsung_TV.objects.all()
#     context = {
#         'samsung_tvs': samsung_tvs,
#     }
#     return render(request, 'blog/tv/samsung_tv_list.html', context=context)


# def samsung_tv_detail(request, slug):
#     samsung_tv = Samsung_TV.objects.get(slug__iexact=slug)
#     context = {
#         'samsung_tv': samsung_tv,
#     }
#     return render(request, 'blog/tv/samsung_tv_detail.html', context=context)


# ----------------------------------sony-------------------------------------

# def sonys_list(request):
#     sonys = Sony.objects.all()
#     context = {
#         'sonys': sonys,
#     }
#     return render(request, 'blog/tv/sony_list.html', context=context)


# def sony_detail(request, slug):
#     sony = Sony.objects.get(slug__iexact=slug)
#     context = {
#         'sony': sony,
#     }
#     return render(request, 'blog/tv/sony_detail.html', context=context)

# ----------------------------------panasonic------------------------------

# def panasonics_list(request):
#     panasonics = Panasonic.objects.all()
#     context = {
#         'panasonics': panasonics,
#     }
#     return render(request, 'blog/tv/panasonic_list.html', context=context)


# def panasonic_detail(request, slug):
#     panasonic = Panasonic.objects.get(slug__iexact=slug)
#     context = {
#         'panasonic': panasonic,
#     }
#     return render(request, 'blog/tv/panasonic_detail.html', context=context)

# =================================phone===================================
# --------------------------------samsung-----------------------------------
# def samsungs_list(request):
#     samsungs = Samsung.objects.all()
#     context = {
#         'samsungs': samsungs,
#     }
#     return render(request, 'blog/phone/samsung_list.html', context=context)


# def samsung_detail(request, slug):
#     samsung = Samsung.objects.get(slug__iexact=slug)
#     context = {
#         'samsung': samsung,
#     }
#     return render(request, 'blog/phone/samsung_detail.html', context=context)

# ----------------------------------apple----------------------------------


# def apples_list(request):
#     apples = Apple.objects.all()
#     context = {
#         'apples': apples,
#     }
#     return render(request, 'blog/phone/apple_list.html', context=context)


# def apple_detail(request, slug):
#     apple = Apple.objects.get(slug__iexact=slug)
#     context = {
#         'apple': apple,
#     }
#     return render(request, 'blog/phone/apple_detail.html', context=context)


# ---------------------------------- xiaomi --------------------------------


# def xiaomis_list(request):
#     xiaomis = Xiaomi.objects.all()
#     context = {
#         'xiaomis': xiaomis,
#     }
#     return render(request, 'blog/phone/xiaomi_list.html', context=context)


# def xiaomi_detail(request, slug):
#     xiaomi = xiaomi.objects.get(slug__iexact=slug)
#     context = {
#         'xiaomi': xiaomi,
#     }
#     return render(request, 'blog/phone/xiaomi_detail.html', context=context)


# =============================== a_laptop ==================================
# --------------------------------- mac_os ----------------------------------


# def mac_oss_list(request):
#     mac_oss = Mac_OS.objects.all()
#     context = {
#         'mac_oss': mac_oss,
#     }
#     return render(request, 'blog/a_laptop/mac_os_list.html', context=context)


# def mac_os_detail(request, slug):
#     mac_os = Mac_OS.objects.get(slug__iexact=slug)
#     context = {
#         'mac_os': mac_os,
#     }
#     return render(request, 'blog/a_laptop/mac_os_detail.html', context=context)


# ---------------------------------- asus -----------------------------------

# def asuss_list(request):
#     asuss = ASUS.objects.all()
#     context = {
#         'asuss': asuss,
#     }
#     return render(request, 'blog/a_laptop/asus_list.html', context=context)


# def asus_detail(request, slug):
#     asus = ASUS.objects.get(slug__iexact=slug)
#     context = {
#         'asus': asus,
#     }
#     return render(request, 'blog/a_laptop/asus_detail.html', context=context)


# ------------------------------------ acer ---------------------------------


# def acers_list(request):
#     acers = ACER.objects.all()
#     context = {
#         'acers': acers,
#     }
#     return render(request, 'blog/a_laptop/acer_list.html', context=context)


# def acer_detail(request, slug):
#     acer = ACER.objects.get(slug__iexact=slug)
#     context = {
#         'acer': acer,
#     }
#     return render(request, 'blog/a_laptop/acer_detail.html', context=context)


# =============================================================================

# ----------------------------------------------------
# def tvs_list(request):
#     catalogs = Catalog.objects.all()
#     category_tvs = Category_TV.objects.all()
#     lgs = LG.objects.all()
#     samsung_tvs = Samsung_TV.objects.all()
#     sonys = Sony.objects.all()
#     panasonics = Panasonic.objects.all()
#     context = {
#         'catalogs': catalogs,
#         'category_tvs': category_tvs, 
#         'lgs': lgs,
#         'samsung_tvs': samsung_tvs,
#         'sonys': sonys,
#         'panasonics': panasonics,
#     }
#     return render(request, 'blog/tv/tvs_list.html', context=context)


# def tvs_detail(request, slug):
#     catalogs = Catalog.objects.get(slug_iexact=slug)
#     category_tvs = Category_TV.objects.get(slug_iexact=slug)
#     lgs = LG.objects.all()
#     samsung_tvs = Samsung_TV.objects.all()
#     sonys = Sony.objects.all()
#     panasonics = Panasonic.objects.all()
#     context = {
#         'catalogs': catalogs,
#         'category_tvs': category_tvs, 
#         'lgs': lgs,
#         'samsung_tvs': samsung_tvs,
#         'sonys': sonys,
#         'panasonics': panasonics,
#     }
#     return render(request, 'blog/tv/tvs_detail.html', context=context)


# def phones_list(request):
#     catalogs = Catalog.objects.all()
#     category_phones = Category_Phone.objects.all()
#     samsungs = Samsung.objects.all()
#     apples = Apple.objects.all()
#     xiaomis = Xiaomi.objects.all()
#     context = {
#         'catalogs': catalogs,
#         'category_phones': category_phones,
#         'samsungs': samsungs,
#         'apples': apples,
#         'xiaomis': xiaomis,        
#     }
#     return render(request, 'blog/phone/phones_list.html', context=context)


# def a_laptops_list(request):
#     catalogs = Catalog.objects.all()
#     category_a_laptops = Category_a_laptop.objects.all()
#     os_macs = Mac_OS.objects.all()
#     asuss = ASUS.objects.all()
#     acers = ACER.objects.all()
#     context = {
#         'catalogs': catalogs,
#         'category_a_laptops': category_a_laptops,
#         'os_macs': os_macs,
#         'asuss': asuss,
#         'acers': acers,        
#     }
#     return render(request, 'blog/a_laptop/a_laptops_list.html', context=context)


# class Представление - это вызываемый объект, который принимает запрос и возвращает ответ.
