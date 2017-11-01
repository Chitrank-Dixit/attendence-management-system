from rest_framework import serializers
from attendence.models import Student, Attendence
from attendence.utils import ValidateDate


class StudentSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Student
        fields = ('id', 'user')


class AttendenceListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        attendence = [Attendence(**item) for item in validated_data if ValidateDate(item['date']).validate_date()]
        return Attendence.objects.bulk_create(attendence)


class AttendenceSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Attendence
        list_serializer_class = AttendenceListSerializer
        fields = ('id', 'student', 'date', 'status')



    # def create(self, validated_data):
    #     if not ValidateDate(validated_data['date']).validate_date():
    #         raise serializers.ValidationError({
    #             'date': 'date supplied here is not valid, it should not be ahead of time'
    #          })
    #     return Attendence.objects.create(**validated_data)







