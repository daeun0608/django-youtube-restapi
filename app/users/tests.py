from django.test import TestCase
from django.contrib.auth import get_user_model # 유저 만드는 함수 제공

# Create your tests here.
class UserTestCase(TestCase):
    # 일반 유저 생성 테스트
    def test_create_user(self):
        email='basic@naver.com'
        password='password'

        user=get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)

    # 슈퍼 유저 생성 테스트
    def test_create_superuser(self):
        email='super@naver.com'
        password='password'

        user=get_user_model().objects.create_superuser(email=email,password=password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)