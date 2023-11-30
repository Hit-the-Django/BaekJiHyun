from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Post, Comment

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        model=Post
        fields = [
            'id',
            'image',
            'created_at',
            'view_count',
            'writer',
        ]
        # exclude = ['conetnet',]
        depth = 1

class PostModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        depth = 1

class PostRetrieveSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        depth = 1

class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostModelSerializer.Meta):
        model=Post
        fields = [
            'image',
            'content',
            ]


class PostDeleteModelSerializer(PostBaseModelSerializer):
    pass

class PostHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'