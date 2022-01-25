from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(username='Ala', password='makota')
        # user.save() - not needed, create_user() saves it
        post = Post.objects.create(author=user, title='Covid-19', body='Wiecej zarazonych. Szok')

    def test_post_content(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.author.username, 'Ala')
        self.assertEqual(post.title, 'Covid-19')
        self.assertEqual(post.body, 'Wiecej zarazonych. Szok')