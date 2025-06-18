from django.db import models

class SiteSection(models.Model):
    name = models.CharField("اسم القسم", max_length=100)
    description = models.TextField("وصف القسم", blank=True)

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        return self.name
