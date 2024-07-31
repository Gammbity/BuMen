from common import models
from django.test import TestCase
import uuid
from common import utils
from common import tasks
from user.models import UserModel
from django.forms.models import model_to_dict 
from django.core.files.uploadedfile import SimpleUploadedFile

class TestUserConCategory(TestCase):

    def test_user_create_contact(self):
        contact_category = models.ContactCategoryModel.objects.create(title='shunchaki')
        user = UserModel.objects.create_user(
            full_name='Ali Aliyev',
            phone='+998999997774',
            email='ali@gmail.com',
            telegram_id=123123,
            balance=20000000000,
            is_pro=1,
            lang='uz'
        )
        contact = models.UserContactAppModel.objects.create(
        source=1,
        user=user,
        email=user.email,
        full_name=user.full_name,
        phone=user.phone,
        message='Men bilan bog\'laning',
        category=contact_category,
        file=SimpleUploadedFile("test.txt", b"This is a test file.")
        )

        respone = self.client.post('/api/v1/common/user-contact-application/create/', data=model_to_dict(contact))

        self.assertEqual(respone.status_code, 201)

# class TaskTest_create_test_image(TestCase):

    # def test_happy(self):
    #     news = models.NewModel.objects.create(
    #         title='New',
    #         banner=utils.create_test_image(),
    #         content='news content',
    #         slug='new'
    #     )

#         news_view = models.NewsViewModel.objects.create(news=news, visitor_id=uuid.uuid4(), ip='127.0.0.1')
#         news_view.created_at = '2021-01-01'
#         news_view.save()

#         tasks.news_views_cleaner()
#         self.assertEqual(models.NewsViewModel.objects.count(), 0)

# class UserContactApp(TestCase):

#     #API
#     def test_create(self):
#         user = {
#             'full_name': 'Ali Aliyev', 
#             'phone': '+998998887766', 
#             'message': 'Helllo world'
#         }
#         response = self.client.post('/api/v1/common/user-contact-application/create/', data=user)
#         self.assertEqual(response.status_code, 201)

#     #model
#     def test_model_create_user_contact_app(self):
#         user_app = models.UserContactAppModel.objects.create(
#             full_name='Ali', phone='+998998887766', message='asdasd'
#         )
#         self.assertEqual(user_app.full_name, 'Ali')

# class TestSettings(TestCase):

#     def test_get(self):
#         response = self.client.get('/api/v1/common/setting/')
#         self.assertEqual(response.status_code, 200)

# class TestPartner(TestCase):

#     def test_get(self):
#         response = self.client.get('/api/v1/common/partners/')
#         self.assertEqual(response.status_code, 200)
    
# class TestNew(TestCase):

#     def test_get(self):
#         response = self.client.get('/api/v1/common/news/')
#         self.assertEqual(response.status_code, 200)

# class TestNew(TestCase):

#     def test_get(self):
#         new = models.NewModel.objects.create(
#         slug='asd-asdasd-asd',
#         title='asdasdasd',
#         content='asdasdasd',
#         top=True,
#         banner='data:image/jpeg;base64,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'
#     )
#         response = self.client.get(f'/api/v1/common/new/{new.slug}/')
#         self.assertEqual(response.status_code, 200)

# class TestQuote(TestCase):

#     def test_get(self):
#         response = self.client.get('/api/v1/common/quote/')
#         self.assertEqual(response.status_code, 200)

# class TestAdvertising(TestCase):

#     def test_get(self):
#         response = self.client.get('/api/v1/common/advertising/')
#         self.assertEqual(response.status_code, 200)
    
# class TestPage(TestCase):

#     def test_get(self):
#         page = models.PageModel.objects.create(slug='asd-asd', title='asdasd', content='asdasdasdasd')
#         response = self.client.get(f'/api/v1/common/page/{page.slug}/')
#         self.assertEqual(response.status_code, 200)
    
# class TestAboutApp(TestCase):

#     #API
#     def test_get(self):
#         response = self.client.get('/api/v1/common/about-app/')
#         self.assertEqual(response.status_code, 200)


#     #model
#     def test_model_save_find_order_auto(self):
#         about1 = models.AboutAppModel.objects.create(
#             caption = 'Nega bu ilovani ishlatishim kerak?',
#             text = 'Nega bo\'lmasin'
#         ) 
#         self.assertEqual(about1.order, 1)

#         about2 = models.AboutAppModel.objects.create(
#             caption = 'Rostan so\'rayapman!!!',
#             text = 'Bo\'ldi qilasammi?!'
#         )
#         self.assertEqual(about2.order, 2)

# class TestFAQ(TestCase):

    #API
    # def test_get(self):
    #     response = self.client.get('/api/v1/common/FAQ/')
    #     self.assertEqual(response.status_code, 200)


    # #model
    # def test_model_save_find_order_auto(self):
    #     faq1 = models.FAQModel.objects.create(
    #         question = 'Nega yer shar shaklida?',
    #         answer = 'Nega bo\'lmasin'
    #     ) 
    #     self.assertEqual(faq1.order, 1)

    #     faq2 = models.FAQModel.objects.create(
    #         question = 'Rostan so\'rayapman!!!',
    #         answer = 'Bo\'ldi qilasammi?!'
    #     )
    #     self.assertEqual(faq2.order, 2)