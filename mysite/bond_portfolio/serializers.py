from rest_framework import serializers
from .models import Bond, SalesRecord

class BondManageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Bond
        fields = "__all__"
    
    def update(self, instance, validated_data):
        print("yogesh")
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        print(instance.name)
        return instance

# class SalesRecordSerializers(serializers.Serializer):
#     bond = serializers.IntegerField()
#     customer = serializers.CharField()
#     sales_person = serializers.

    
#     def create(self, validated_data):
#         return SalesRecord(**validated_data)

