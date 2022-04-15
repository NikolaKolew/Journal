from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Journal.auth_accounts.models import Profile
from Journal.web_posts.models import Post, Comment

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

    VALID_COMMENT_DATA = {
        'post_id': 1,
        'description': 'New comment',
    }

    def __create_post_for_user(self, user):
        post = Post.objects.create(
            **self.VALID_POST_DATA,
            user=user,
        )

        post.save()
        return post

    def __create_comment_for_user(self, user):
        self.__create_post_for_user(user)
        comment = Comment.objects.create(
            **self.VALID_COMMENT_DATA,
            user=user,
        )

        comment.save()
        return comment

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

    def test_create_post_valid_data(self):
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

    def test_create_comment_valid_data(self):
        user, profile = self.__create_profile_and_user()
        comment = self.__create_comment_for_user(user)
        self.client.post(
            reverse('create-comment', kwargs={'pk': comment.pk}),
            data=self.VALID_COMMENT_DATA
        )

        comment = Comment.objects.first()
        self.assertIsNotNone(comment)
        self.assertEqual(self.VALID_COMMENT_DATA['post_id'], comment.post_id)
        self.assertEqual(self.VALID_COMMENT_DATA['description'], comment.description)

    # post_id = Comment.objects.filter(id=self.kwargs['pk']).get().post_id
    # return reverse_lazy('detail-post', kwargs={'pk': post_id})
    def test_get_success_url_for_edit_comment(self):
        user, profile = self.__create_profile_and_user()
        comment = self.__create_comment_for_user(user)
        post = self.__create_post_for_user(user)

        self.client.force_login(user=user)
        response = self.client.post(reverse('edit-comment', kwargs={
            'pk': comment.pk
        }),
                                    {
                                        'title': 'some tittle for comment',
                                        'description': 'some new description',

                                    })
        post = Post.objects.first()
        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('detail-post', kwargs={'pk': post.pk}))

    def test_get_success_url_for_create_comment(self):
        user, profile = self.__create_profile_and_user()
        comment = self.__create_comment_for_user(user)
        post = self.__create_post_for_user(user)

        self.client.force_login(user=user)
        response = self.client.post(reverse('create-comment', kwargs={
            'pk': comment.pk
        }),
        {
            'title': 'some tittle for comment',
            'description': 'some new description',

        })

        post = Post.objects.first()
        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('detail-post', kwargs={'pk': post.pk}))

    def test_get_success_url_for_delete_comment(self):
        user, profile = self.__create_profile_and_user()
        comment = self.__create_comment_for_user(user)
        post = self.__create_post_for_user(user)

        self.client.force_login(user=user)
        response = self.client.post(reverse('delete-comment', kwargs={
            'pk': comment.pk
        }))

        post = Post.objects.first()
        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('detail-post', kwargs={'pk': post.pk}))
