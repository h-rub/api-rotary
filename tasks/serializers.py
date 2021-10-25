from rest_framework import serializers
from tasks.models import Task
from authentication.models import CustomUser

class TaskSerializer(serializers.ModelSerializer):

    user_asigned_to = serializers.SerializerMethodField('get_full_name_asigned_to')

    class Meta:
        model = Task
        fields = ['_id_task', 'title', 'description', 'is_completed', 'due_date', 'user_asigned_to', 'time_date']

    def get_full_name_asigned_to(self, Task):
        _id = Task.asigned_to.pk
        user = CustomUser.objects.get(pk=_id)
        first_name = Task.asigned_to.first_name
        last_name = Task.asigned_to.last_name
        return f"{first_name} {last_name} {_id}"
