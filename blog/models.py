from django.db import models


class BlogNote(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Заголовок'
    )
    body = models.TextField(
        verbose_name='Заметка'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Изменено'
    )
    hidden = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='Снять с публикации?'
    )

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-created_at']
