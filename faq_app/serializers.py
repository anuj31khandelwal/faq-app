from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']

    def to_representation(self, instance):
        """For representation of FAQ instance"""
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'en') if request else 'en'
        
        translated_content = instance.get_translated_content(lang)
        
        return {
            'id': instance.id,
            'question': translated_content['question'],
            'answer': translated_content['answer'],
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
            'language': lang
        }
