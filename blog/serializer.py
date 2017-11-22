from rest_framework import serializers
from .models import User, Entry


class UserSerializer(serializers.ModelSerializer):
    entry_counts = serializers.PrimaryKeyRelatedField(many=True, required=False, read_only=True)

    class Meta:
        model = User
        fields = ('name', 'mail', 'url', 'entry_counts')


class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author', 'url')