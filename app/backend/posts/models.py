from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# from utils.rands import slugify_new
# from utils.images import resize_image
from django_summernote.models import AbstractAttachment


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        current_file_name = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        file_changed = False

        # if self.file:
        #     file_changed = current_file_name != self.file.name

        # if file_changed:
        #     resize_image(self.file, 900)
        return super_save

class PostManager(models.Manager):
    def get_is_published(self):
        return self\
            .filter(is_published=True)\
            .order_by('-pk')



class Post(models.Model):
    objects = PostManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    titulo = models.CharField(max_length=65)
    resumo = models.CharField(max_length=155)
    conteudo = models.TextField()
    capa = models.ImageField(upload_to="posts/%Y/%m/", blank=True, default='')
    capa_no_post = models.BooleanField(default=True)
    preco_marketing = models.FloatField(default=0, verbose_name='preço')
    preco_marketing_promocao = models.FloatField(default=0, verbose_name='preço promo')
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='post_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='post_updated_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tags = models.ManyToManyField(Tag, blank=True, default='')
    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.SET_NULL,
    #     default=None,
    #     null=True,
    #     blank=True,
    #     )
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisará estar marcado '
            'para a página ser exibida publicamente.'
        ),
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        default='',
        null=True,
        blank=True
    )

    # def get_absolute_url(self):
    #     if not self.is_published:
    #         return reverse('blog:index')
    #     return reverse('blog:post', args=(self.slug,))

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify_new(self.title)
    #     current_cover_name = str(self.cover.name)
    #     super_save = super().save(*args, **kwargs)
    #     cover_changed = False

    #     if self.cover:
    #         cover_changed = current_cover_name != self.cover.name

    #     if cover_changed:
    #         resize_image(self.cover, 900)
    #     return super_save

    # def __str__(self) -> str:
    #     return self.title
