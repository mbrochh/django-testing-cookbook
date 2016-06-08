from .. import forms


class TestPostForm:
    def test_form(self):
        form = forms.PostForm(data={})
        assert form.is_valid() is False, (
            'Should be invalid if no data is given')

        data = {'body': 'Hello'}
        form = forms.PostForm(data=data)
        assert form.is_valid() is False, (
            'Should be invalid if body text is less than 10 characters')
        assert 'body' in form.errors, 'Should return field error for `body`'

        data = {'body': 'Hello World!'}
        form = forms.PostForm(data=data)
        assert form.is_valid() is True, 'Should be valid all data is given'
