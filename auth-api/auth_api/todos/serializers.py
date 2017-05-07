from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Deck
        fields = ('url', 'id', 'created', 'name', 'user')
        extra_kwargs = {
            'url': {
                'view_name': todos: todo-detail',
            }
        }
