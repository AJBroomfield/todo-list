import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Tasks

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        sample1 = Tasks(desc="Eat cheese")     
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_read_task(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)
    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)
    def test_update_get(self):
        response = self.client.get(url_for('update', id=1),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_complete_get(self):
        response = self.client.get(url_for('complete',id=1),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_incomplete_get(self):
        response = self.client.get(url_for('incomplete',id=1),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_delete_get(self):
        response = self.client.get(url_for('delete',id=1),follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestRead(TestBase):
    def test_read_task(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'Eat cheese', response.data)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('create'),
            data = dict(desc="Learn french"),
            follow_redirects=True
        )
        self.assertIn(b'Learn french',response.data)

class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
            url_for('update',id=1),
            data = dict(desc="Learn french"),
            follow_redirects=True
        )
        self.assertIn(b'Learn french',response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.get(
            url_for('delete',id=1),
            follow_redirects=True
        )
        self.assertNotIn(b'Eat cheese',response.data)