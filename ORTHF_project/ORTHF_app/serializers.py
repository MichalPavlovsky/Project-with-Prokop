from rest_framework import serializers
from ORTHF_app import models

class WorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.WorkingTime
        fields ='__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Employee
        fields ='__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Patient
        fields ='__all__'

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Actions
        fields ='__all__'

class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Visits
        fields ='__all__'
    
class TypeWorkingSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.TypeWorking
        fields ='__all__'

class RealWorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.RealWorkingTime
        fields ='__all__'

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Config
        fields ='__all__'

class TypeEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.TypeEmployee
        fields ='__all__'
