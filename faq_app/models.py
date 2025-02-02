from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from googletrans import Translator
import json

class FAQ(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    question = models.TextField(verbose_name='Question (English)')
    answer = RichTextField(verbose_name='Answer (English)')
    
    # Hindi translations
    question_hi = models.TextField(verbose_name='Question (Hindi)', blank=True)
    answer_hi = RichTextField(verbose_name='Answer (Hindi)', blank=True)
    
    # Bengali translations
    question_bn = models.TextField(verbose_name='Question (Bengali)', blank=True)
    answer_bn = RichTextField(verbose_name='Answer (Bengali)', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['-created_at']

    def __str__(self):
        return self.question[:100]

    def get_translated_content(self, lang='en'):
        """
        Getting translated content with caching
        """
        cache_key = f'faq_{self.id}_{lang}'
        cached_content = cache.get(cache_key)
        
        if cached_content:
            try:
                return json.loads(cached_content)
            except json.JSONDecodeError:
                cache.delete(cache_key)
        
        content = self._get_language_content(lang)
        cache.set(cache_key, json.dumps(content), timeout=3600)  # Cache for 1 hour
        return content

    def _get_language_content(self, lang):
        """
        fetching content for specified language
        """
        if lang == 'en':
            return {
                'question': self.question,
                'answer': self.answer
            }
        
        question_field = f'question_{lang}'
        answer_field = f'answer_{lang}'
        
        question = getattr(self, question_field, '') or self._translate_text(self.question, lang)
        answer = getattr(self, answer_field, '') or self._translate_text(self.answer, lang)
        
        return {
            'question': question,
            'answer': answer
        }

    def _translate_text(self, text, lang):
        """
        Translating text using Google Translate
        """
        try:
            translator = Translator()
            translated = translator.translate(text, dest=lang)
            return translated.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text  # Fallback to original text

    def save(self, *args, **kwargs):
        """
        Overriding save to handle translations
        """
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            # Generate translations for new entries
            for lang_code, _ in self.LANGUAGES[1:]:  # Skip English
                if not getattr(self, f'question_{lang_code}'):
                    translated_question = self._translate_text(self.question, lang_code)
                    setattr(self, f'question_{lang_code}', translated_question)
                
                if not getattr(self, f'answer_{lang_code}'):
                    translated_answer = self._translate_text(self.answer, lang_code)
                    setattr(self, f'answer_{lang_code}', translated_answer)
            
            super().save(*args, **kwargs)