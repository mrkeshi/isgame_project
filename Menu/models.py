from django.db import models


# Create your models here.
class Menu(models.Model):
    class placeMenu(models.TextChoices):
        navar_menu_1 = "MN1", "چایگاه هدر اول"
        navar_menu_2 = "MN2", "جایگاه هدر دوم"
        navar_menu_3 = "MN3", "جایگاه هدر سوم"
        footer_menu_1 = "FN1", "جایگاه فوتر اول"
        footer_menu_2 = "FN2", "جایگاه فوتر دوم"
        social = "SC1", "شبکه های اجتماعی"

        def __str__(self):
            return self.label

    title = models.CharField(max_length=50, verbose_name='عنوان')
    url = models.TextField(max_length=100, verbose_name="آدرس")
    sort = models.IntegerField(verbose_name="فیلد ترتیب")
    is_active = models.BooleanField(default=1, verbose_name="وضعیت نمایش")
    icon_name = models.CharField(max_length=50, blank=False, null=True, verbose_name="نام آیکون")
    icon_color = models.CharField(max_length=50, blank=False, null=True, verbose_name="رنگ ایکون")
    place_menu = models.CharField(max_length=50, choices=placeMenu.choices, verbose_name="جایگاه منو")

    def __str__(self):
        return self.title
