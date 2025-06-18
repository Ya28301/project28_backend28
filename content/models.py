from django.db import models
from core.models import SiteSection

class ContentItem(models.Model):
    title = models.CharField("العنوان", max_length=200)
    body = models.TextField("المحتوى")
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    section = models.ForeignKey(SiteSection, verbose_name="القسم", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "عنصر محتوى"
        verbose_name_plural = "عناصر المحتوى"

    def __str__(self):
        return self.title
