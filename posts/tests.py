from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostsModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Isto é um teste.')


    def test_test_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Isto é um teste.')
    

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Este é outro teste.')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
