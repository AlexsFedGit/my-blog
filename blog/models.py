from django.db import models


class BlogNote(models.Model):
    body = models.TextField(
        verbose_name='Заметка'
    )
    is_published = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Изменено'
    )


    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-created_at']
