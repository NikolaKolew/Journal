from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Journal.auth_accounts.models import Profile
from Journal.web_posts.models import Post

UserModel = get_user_model()


class TestProfileDetails(TestCase):
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

    def __get_profile_details(self, profile):
        return self.client.get(reverse('profile-page', kwargs={'pk': profile.pk}))

    def test_shows_correct_profile_detail_page(self):
        _, profile = self.__create_profile_and_user()
        self.__get_profile_details(profile)
        self.assertTemplateUsed('user/profile.html')

    def test_user_profile_total_posts_expects_to_be_one(self):
        user, profile = self.__create_profile_and_user()
        self.__create_post_for_user(user)
        total_posts = Post.objects.filter(user=user).count()

        self.assertEqual(1, total_posts)

    def test_user_profile_total_posts_expects_to_be_zero(self):
        user, profile = self.__create_profile_and_user()
        total_posts = Post.objects.filter(user=user).count()

        self.assertEqual(0, total_posts)
