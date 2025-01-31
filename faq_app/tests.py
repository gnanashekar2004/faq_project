from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    
    def setUp(self):
        """
        Setup test data by creating a FAQ object.
        """
        FAQ.objects.create(
            question="Test?", 
            answer="This is a test."
        )

    def test_translation(self):
        """
        Test if the FAQ translation works as expected.
        """
        faq = FAQ.objects.get(question="Test?")
        self.assertEqual(faq.get_translation('en')['answer'], "This is a test.")

    def test_faq_creation(self):
        """
        Test if a FAQ is correctly created and stored in the database.
        """
        faq = FAQ.objects.create(
            question="Test?", 
            answer="This is a test."
        )
        # Save the FAQ to trigger translation
        faq.save()
        
        self.assertEqual(faq.question, "Test?")
        self.assertEqual(faq.answer, "This is a test.")
        # Ensure translation fields are not None after save
        self.assertIsNotNone(faq.question_hi)
        self.assertIsNotNone(faq.answer_hi)

    def test_translation_hindi(self):
        """
        Test if the translation feature works for Hindi.
        """
        faq = FAQ.objects.get(question="Test?")
        faq.save()  # Save FAQ to trigger translation
        self.assertIsNotNone(faq.question_hi)  # Should now have a Hindi translation
