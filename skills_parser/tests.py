from django.test import TestCase

from .parser import UserParser


class ParserTest(TestCase):
    def test_top_languages(self):
        up = UserParser('Boring-Mind')
        languages = up.get_top_languages('DjangoGirls1')
        self.assertEqual(len(languages), 5)

    def test_top_languages_repo_not_exist(self):
        up = UserParser('Boring-Mind')
        languages = up.get_top_languages('DoesNotExist')
        self.assertEqual(len(languages), 0)
