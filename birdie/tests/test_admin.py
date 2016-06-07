import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer
from .. import admin
from .. import models
pytestmark = pytest.mark.django_db


class TestPostAdmin:
    def test_excerpt(self):
        site = AdminSite()
        post_admin = admin.PostAdmin(models.Post, site)
        obj = mixer.blend('birdie.Post', body='Hello World')

        result = post_admin.excerpt(obj)
        expected = obj.get_excerpt(5)
        assert result == expected, (
            'Should return the result form the .excerpt() function')
