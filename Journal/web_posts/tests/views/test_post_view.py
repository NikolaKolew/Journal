from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Journal.auth_accounts.models import Profile
from Journal.web_posts.models import Post

UserModel = get_user_model()

class TestPostsViews(TestCase):
    VALID_USER_DATA = {
        'email': 'kolev777@gmail.com',
        'password': 'NikolaKU99881',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Nikola',
        'last_name': 'Kolev',
    }

    VALID_POST_DATA = {
        'title': 'Hello',
        'body': 'My new post',
    }

    def __create_post_for_user(self, user):
        post = Post.objects.create(
            **self.VALID_POST_DATA,
            user=user,
        )

        post.save()
        return post

    def __create_user(self, **data):
        user = UserModel.objects.create_user(**data)
        return user

    def __create_profile_and_user(self):
        user = self.__create_user(**self.VALID_USER_DATA)
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=user)
        return user, profile

    def __get_post_details(self, post):
        return self.client.get(reverse('detail-post', kwargs={'pk': post.pk}))

    def __get_all_posts(self):
        return self.client.get(reverse('posts'))

    def test_show_all_post_page(self):
        user, profile = self.__create_profile_and_user()
        self.__create_post_for_user(user)
        self.__get_all_posts()
        self.assertTemplateUsed('posts/posts.html')

    def test_get_post_detail_page(self):
        user, profile = self.__create_profile_and_user()
        post = self.__create_post_for_user(user)
        self.__get_post_details(post)
        self.assertTemplateUsed('posts/post_details.html')

    def test_create_journal_valid_data(self):
        user, profile = self.__create_profile_and_user()
        self.__create_post_for_user(user)
        self.client.post(
            reverse('create-post'),
            data=self.VALID_POST_DATA
        )

        post = Post.objects.first()
        self.assertIsNotNone(post)
        self.assertEqual(self.VALID_POST_DATA['title'], post.title)
        self.assertEqual(self.VALID_POST_DATA['body'], post.body)

    def test_create_valid_post_redirect_posts(self):
        self.__create_profile_and_user()
        response = self.client.post(
            reverse('create-post'),
            data=self.VALID_POST_DATA,
        )
        Profile.objects.first()
        expected_url = reverse('posts')
        self.assertRedirects(response, expected_url)