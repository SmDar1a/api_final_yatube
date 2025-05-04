from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Класс модели группы постов."""

    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    """Класс модели поста."""

    text = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        to=Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True,
        verbose_name='Группа',
    )

    def __str__(self) -> str:
        return self.text


class Comment(models.Model):
    """Класс модели комментария к посту."""

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True,
    )

    def __str__(self) -> str:
        return self.text


class Follow(models.Model):
    """Класс модели подписки на пользователя."""

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="follower",
    )
    following = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="following",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"],
                name="unique_follow",
            )
        ]

    def __str__(self) -> str:
        return f"{self.user} follows {self.following}"
