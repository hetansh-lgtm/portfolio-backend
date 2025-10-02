import pytest
from django.urls import reverse
from api.models import Project, Technology

@pytest.mark.django_db
def test_projects_list(client):
    t1 = Technology.objects.create(name="React")
    p = Project.objects.create(title="Site", description="demo")
    p.technologies.add(t1)

    url = reverse('projects-list')
    resp = client.get(f"/api/v1/{url.split('/')[-2]}/")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert data[0]['title'] == 'Site'
    assert data[0]['technologies'][0]['name'] == 'React'

@pytest.mark.django_db
def test_contact_create(client):
    url = reverse('contact-create')
    payload = {"name": "Jane", "email": "jane@example.com", "message": "Hello"}
    resp = client.post(f"/api/v1/{url.split('/')[-2]}/", payload, content_type='application/json')
    assert resp.status_code == 201
    assert resp.json()['name'] == 'Jane'