from rest_framework import  serializers
from user.models import advertise

class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = advertise
        fields = '__all__'