from rest_framework import serializers

from .models import (Project, Step)


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    steps = serializers.SerializerMethodField()

    def get_id(self, instance):
        return instance.order_num

    def get_steps(self, instance):
        queryset = Step.objects.filter(
            project_id=instance.id).order_by('order_num')
        serializer = StepSerializer(
            instance=queryset, many=True)
        return serializer.data

    class Meta:
        model = Project
        fields = ('id', 'name', 'type', 'description',
                  'inference_name', 'inference_description', 'steps')


class StepSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    def get_id(self, instance):
        return instance.order_num

    def get_url(self, instance):
        project_ins = Project.objects.get(pk=instance.project_id)
        return f'{project_ins.url}{instance.url}'

    class Meta:
        model = Step
        fields = (
            'id',
            'name',
            'url',
        )
