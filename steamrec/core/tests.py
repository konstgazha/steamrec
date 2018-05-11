from django.test import TestCase
from datetime import datetime

from .models import AppType, App, Tag, AppTag


class GameModelTest(TestCase):
    def setUp(self):
        tag = Tag.objects.create(name="action")
        app_type = AppType.objects.create(name="game", display_name="Game")
        app = App.objects.create(appid=730,
                                 name="Counter-Strike: Global Offensive",
                                 app_type=app_type,
                                 release_date="2012-08-21",
                                 developer="Valve",
                                 publisher="Valve")
        AppTag.objects.create(app=app, tag=tag)

    def test_select_tag_by_name(self):
        tag = Tag.objects.get(name="action")
        self.assertEqual(tag.name, "action")

    def test_select_app_type_by_name(self):
        app_type = AppType.objects.get(name="game")
        self.assertEqual(app_type.name, "game")

    def test_get_app_by_appid(self):
        app = App.objects.get(appid=730)
        self.assertEqual(app.appid, 730)

    def test_select_apps_by_tag(self):
        app_ids = AppTag.objects.filter(tag__name="action").values_list('app', flat=True)
        apps = [App.objects.get(id=app_id) for app_id in app_ids]
        self.assertEqual(len(apps), 1)
