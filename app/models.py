from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    cover = models.ImageField(upload_to="covers", verbose_name="Обложка")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.title} ({self.author}) - {self.price}₸"

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
