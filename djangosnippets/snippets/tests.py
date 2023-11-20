from django.test import TestCase
from django.urls import resolve
from snippets.views import snippet_new, snippet_edit, snippet_detail


class TopPageViewTestCase(TestCase):
    def test_top_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response = self.client.get('/')
        self.assertEqual(response.content, b'Hello World')


class CreateSnnipetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve('/snippet/new/')
        self.assertEqual(snippet_new, found.func)


class EditSnnipetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve('/snippet/1/edit/')
        self.assertEqual(snippet_edit, found.func)


class DetailSnnipetTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve('/snippet/1/')
        self.assertEqual(snippet_detail, found.func)
