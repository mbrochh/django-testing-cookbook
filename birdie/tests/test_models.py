import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestPost:
    def test_init(self):
        obj = mixer.blend('birdie.Post')
        assert obj.pk == 1, 'Should save an instance'

    def test_get_excerpt(self):
        obj = mixer.blend('birdie.Post', body='Hello World!')
        result = obj.get_excerpt(5)
        expected = 'Hello'
        assert result == expected, (
            'Should return the given number of characters')
