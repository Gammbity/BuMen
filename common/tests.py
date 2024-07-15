from common import models
from rest_framework.test import APITestCase

class UserContactApp(APITestCase):

    #API
    def test_create(self):
        user = {
            'full_name': 'Ali Aliyev', 
            'phone': '+998998887766', 
            'message': 'Helllo world'
        }
        response = self.client.post('/api/v1/common/user-contact-application/create/', data=user)
        self.assertEqual(response.status_code, 201)

    #model
    def test_model_create_user_contact_app(self):
        user_app = models.UserContactAppModel.objects.create(
            full_name='Ali', phone='+998998887766', message='asdasd'
        )
        self.assertEqual(user_app.full_name, 'Ali')

class TestSettings(APITestCase):

    def test_get(self):
        response = self.client.get('/api/v1/common/setting/')
        self.assertEqual(response.status_code, 200)

class TestPartner(APITestCase):

    def test_get(self):
        response = self.client.get('/api/v1/common/partners/')
        self.assertEqual(response.status_code, 200)
    
class TestNew(APITestCase):

    def test_get(self):
        response = self.client.get('/api/v1/common/news/')
        self.assertEqual(response.status_code, 200)

class TestQuote(APITestCase):

    def test_get(self):
        response = self.client.get('/api/v1/common/quote/')
        self.assertEqual(response.status_code, 200)

class TestAdvertising(APITestCase):

    def test_get(self):
        response = self.client.get('/api/v1/common/advertising/')
        self.assertEqual(response.status_code, 200)
    
class TestPage(APITestCase):

    def test_get(self):
        page = models.PageModel.objects.create(slug='asd-asd', title='asdasd', content='asdasdasdasd')
        response = self.client.get(f'/api/v1/common/page/{page.id}/')
        self.assertEqual(response.status_code, 200)
    
class TestAboutApp(APITestCase):

    #API
    def test_get(self):
        response = self.client.get('/api/v1/common/about-app/')
        self.assertEqual(response.status_code, 200)


    #model
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

class TestFAQ(APITestCase):

    #API
    def test_get(self):
        response = self.client.get('/api/v1/common/FAQ/')
        self.assertEqual(response.status_code, 200)


    #model
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