from django.db import models
from content.models import ContentItem

class Message(models.Model):
    content_item = models.ForeignKey(
        ContentItem,
        verbose_name="العنصر المرتبط",
        on_delete=models.CASCADE
    )
    sender_name = models.CharField("اسم المرسل", max_length=100)
    message = models.TextField("نص الرسالة")
    sent_at = models.DateTimeField("تاريخ الإرسال", auto_now_add=True)

    class Meta:
        verbose_name = "رسالة"
        verbose_name_plural = "الرسائل"

    def __str__(self):
        return f"من {self.sender_name} على {self.content_item}"
