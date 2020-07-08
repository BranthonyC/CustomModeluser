from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'La cucaracha la cucaracha ya no puede caminar')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='arilda',
            email='arilda@arilda.com',
            password='marisol'
        )
        self.assertEqual(user.username,'arilda')
        self.assertEqual(user.email,'arilda@arilda.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='arilda',
            email="arilda@arilda.com",
            password='testpass123'
        )
        self.assertEqual(admin_user.username,'arilda')
        self.assertEqual(admin_user.email,'arilda@arilda.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
