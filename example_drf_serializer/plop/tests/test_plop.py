import pytest
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient

from example_drf_serializer.plop.models import Plop


@pytest.fixture
def plop():
    instance = Plop.objects.create(name='test plop')

    instance.children.create(name='child 1')
    instance.children.create(name='child 2')
    instance.children.create(name='child 3')

    return instance


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_get(plop, client):
    response = client.get(reverse('plop-detail', args=[plop.pk]))

    assert response.status_code == 200
    assert response.data['name'] == 'test plop'
    assert len(response.data['children']) == 3


@pytest.mark.django_db
def test_patch(plop, client):
    response = client.patch(
        reverse('plop-detail', args=[plop.pk]),
        data={
            'name': 'plop',
        },
    )

    assert response.status_code == 200
    assert response.data['name'] == 'plop'
