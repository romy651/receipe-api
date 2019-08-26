from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = 'pass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email = 'mytest@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@londn.com',
            'vas123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
