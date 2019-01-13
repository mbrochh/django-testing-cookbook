import pytest
from django.core import mail
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from mock import patch
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from .. import views


class TestHomeView:
    def test_anonymous(self, rf):
        req = rf.get('/')
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'


class TestAdminView:
    def test_anonymous(self, rf):
        req = rf.get('/')
        req.user = AnonymousUser()
        resp = views.AdminView.as_view()(req)
        assert 'login' in resp.url, 'Should redirect to login'

    def test_superuser(self, rf):
        user = mixer.blend('auth.User', is_superuser=True)
        req = rf.get('/')
        req.user = user
        resp = views.AdminView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by superuser'


class TestPostUpdateView:
    def test_get(self, rf):
        post = mixer.blend('birdie.Post')
        req = rf.get('/')
        req.user = AnonymousUser()
        resp = views.PostUpdateView.as_view()(req, pk=post.pk)
        assert resp.status_code == 200, 'Should be callable by anyone'

    def test_post(self, rf):
        post = mixer.blend('birdie.Post')
        data = {'body': 'New Body Text!'}
        req = rf.post('/', data=data)
        req.user = AnonymousUser()
        resp = views.PostUpdateView.as_view()(req, pk=post.pk)
        assert resp.status_code == 302, 'Should redirect to success view'
        post.refresh_from_db()
        assert post.body == 'New Body Text!', 'Should update the post'

    def test_security(self, rf):
        user = mixer.blend('auth.User', first_name='Martin')
        post = mixer.blend('birdie.Post')
        req = rf.post('/', data={})
        req.user = user
        with pytest.raises(Http404):
            views.PostUpdateView.as_view()(req, pk=post.pk)


class TestPaymentView:
    @patch('birdie.views.stripe')
    def test_payment(self, mock_stripe, rf):
        mock_stripe.Charge.return_value = {'id': '234'}
        req = rf.post('/', data={'token': '123'})
        resp = views.PaymentView.as_view()(req)
        assert resp.status_code == 302, 'Should redirect to success_url'
        assert len(mail.outbox) == 1, 'Should send an email'
