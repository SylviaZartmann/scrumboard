from rest_framework import serializers
from .models import Client, Contact, Contract, Project

    
class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'
        
        
class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        
class ContractSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contract
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'