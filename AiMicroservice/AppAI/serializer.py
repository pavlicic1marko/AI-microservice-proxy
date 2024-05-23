from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Prompt
        fields = ['user_id','createdAt','question','answer']