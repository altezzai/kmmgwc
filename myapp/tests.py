from django.test import TestCase, Client
from django.urls import reverse
from .models import Notification

class NotificationInputValidationTests(TestCase):
    def setUp(self):
        self.client = Client()
        session = self.client.session
        session['username'] = 'admin'
        session.save()
        
        self.notification = Notification.objects.create(
            category="General",
            title="Old Title",
            description="Old Description"
        )
        self.url = f'/update_notification/{self.notification.id}/'

    def test_reject_script_tag(self):
        payload = {
            'category': 'General',
            'title': '<script>alert(1)</script>',
            'description': 'Description'
        }
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 200) # Form render with error
        self.assertFormError(response, 'form', 'title', 'HTML content is not allowed.')
        
        # Verify db not updated
        self.notification.refresh_from_db()
        self.assertNotEqual(self.notification.title, payload['title'])

    def test_accept_plain_text(self):
        payload = {
            'category': 'General',
            'title': 'Hello World',
            'description': 'Description'
        }
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 302) # Redirect on success
        
        # Verify db updated
        self.notification.refresh_from_db()
        self.assertEqual(self.notification.title, payload['title'])

    def test_reject_bold_tag(self):
        payload = {
            'category': 'General',
            'title': 'Hello <b>bold</b>',
            'description': 'Description'
        }
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 200) # Form render with error
        self.assertFormError(response, 'form', 'title', 'HTML content is not allowed.')
        
        # Verify db not updated
        self.notification.refresh_from_db()
        self.assertNotEqual(self.notification.title, payload['title'])
