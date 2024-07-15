from django.test import TestCase
from common import models


class UserContactApp(TestCase):

    def test_model_create_user_contact_app(self):
        user_app = models.UserContactAppModel.objects.create(
            full_name='Ali', phone='+998998887766', message='asdasd'
        )
        self.assertEqual(user_app.full_name, 'Ali')
    
class TestAboutApp(TestCase):

    def test_model_save_find_order_auto(self):
        about1 = models.AboutAppModel.objects.create(
            caption = 'Nega bu ilovani ishlatishim kerak?',
            text = 'Nega bo\'lmasin'
        ) 
        self.assertEqual(about1.order, 1)

        about2 = models.AboutAppModel.objects.create(
            caption = 'Rostan so\'rayapman!!!',
            text = 'Bo\'ldi qilasammi?!'
        )
        self.assertEqual(about2.order, 2)

class TestFAQ(TestCase):

    def test_model_save_find_order_auto(self):
        faq1 = models.FAQModel.objects.create(
            question = 'Nega yer shar shaklida?',
            answer = 'Nega bo\'lmasin'
        ) 
        self.assertEqual(faq1.order, 1)

        faq2 = models.FAQModel.objects.create(
            question = 'Rostan so\'rayapman!!!',
            answer = 'Bo\'ldi qilasammi?!'
        )
        self.assertEqual(faq2.order, 2)