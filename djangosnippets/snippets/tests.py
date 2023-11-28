from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import resolve

from snippets.models import Snippet
from snippets.views import snippet_new, snippet_edit, snippet_detail, top

UserModel = get_user_model()


class TopPageViewTestCase(TestCase):
    def test_top_returns_200_and_expected_title(self):
        response = self.client.get('/')
        self.assertContains(response, 'Djangoスニペット', status_code=200)

    def test_top_returns_expected_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'snippets/top.html')


class TopPageRenderShinppetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='top_secret_pass0001'
        )
        self.Shinppet = Snippet.objects.create(
            title='title1',
            code="print('hello world')",
            description='description1',
            created_by=self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.Shinppet.title)

    def test_should_return_user_name(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)


class CreateSnnipetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve('/snippet/new/')
        self.assertEqual(snippet_new, found.func)


class EditSnnipetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve('/snippet/1/edit/')
        self.assertEqual(snippet_edit, found.func)


class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
        )
        self.snippet = Snippet.objects.create(
            title="タイトル",
            code="コード",
            description="解説",
            created_by=self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(response, "snippets/snippet_detail.html")

    def test_top_page_returns_200_and_expected_heading(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertContains(response, self.snippet.title, status_code=200)
