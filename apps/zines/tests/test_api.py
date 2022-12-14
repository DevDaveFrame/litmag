from django.test import TestCase, Client
from django.urls import reverse
import json

from apps.zines.models import Zine, Genre, UserProfile
from django.contrib.auth.models import User


class TestZinesAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email=''
        )
        self.client = Client()
        self.zines_url = reverse('zines-list')
        self.author = UserProfile.objects.create(
            user=self.user,
            name='John Doe',
            role='Author',
            pronouns='he/him',
            birthday='1970-01-01',
        )
        self.genre = Genre.objects.create(
            name='Fantasy',
            description='A fantasy genre is a genre of literature that typically '
                        'consists of imaginative, often magical, fantasy stories.',
        )


class TestGetZines(TestZinesAPI):
    def test_zero_zines_should_return_empty_list(self) -> None:
        response = self.client.get(self.zines_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_zine_should_return_one_zine(self) -> None:
        Zine.objects.create(name='New Yonker')
        response = self.client.get(self.zines_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get('name'), 'New Yonker')


class TestPostZine(TestZinesAPI):
    def test_post_zine_should_return_201(self) -> None:
        response = self.client.post(self.zines_url, {
            'name': 'New Zine',
            'description': 'New Zine description',
            'author': self.author.user.id,
            'genres': [self.genre.id],
        })
        self.assertEqual(response.status_code, 201)

    def test_post_zine_should_return_400_if_missing_name(self) -> None:
        response = self.client.post(self.zines_url, {
            'description': 'New Zine description',
            'author': self.author.user.id,
            'genres': [self.genre.id],
        })
        self.assertEqual(response.status_code, 400)
