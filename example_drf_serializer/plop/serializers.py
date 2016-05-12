from rest_framework import serializers

from example_drf_serializer.plop.models import Plop, Child


class ChildSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = Child
        fields = ('name',)


class PlopSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = Plop
        fields = ('name', 'children')

    children = ChildSerializer(many=True, required=True)

    def create(self, validated_data):
        children = validated_data.pop('children')

        instance = super(PlopSerializer, self).create(validated_data)

        for c in children:
            instance.children.create(
                name=c['name'],
            )

        return instance
