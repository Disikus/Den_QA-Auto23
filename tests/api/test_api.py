import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    user.second_name = ''

@pytest.mark.check
def test_name(user):
    assert user.name == 'Denys'

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Myrhorodskyi'