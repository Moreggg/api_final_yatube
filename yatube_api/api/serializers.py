from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username',)
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        if Follow.objects.filter(
            user=user,
            following=following
        ):
            raise serializers.ValidationError(
                'Такая подписка уже есть!'
            )
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)
