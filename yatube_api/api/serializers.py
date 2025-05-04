from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import (
    Comment,
    Post,
    Group,
    Follow,
)

from typing import Optional


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Класс сериалайзера постов."""

    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Класс сериалайзера комментариев под постами."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ["author", "post"]


class GroupSerializer(serializers.ModelSerializer):
    """Класс сериалайзера групп постов."""

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Класс сериалайзера подписок на пользователей."""

    user = SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=["user", "following"],
                message="You already follow this user",
            )
        ]

    def validate_following(self, value: str) -> Optional[str]:
        """Метод валидации following (нельзя подписаться на самого себя)."""
        if self.context["request"].user == value:
            raise serializers.ValidationError(
                "You cannot follow yourself",
            )
        return value
