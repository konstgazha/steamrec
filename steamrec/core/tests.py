from django.test import TestCase
from datetime import datetime, timedelta

from .models import AppType, App, Tag, AppTag

def lists_difference(new_list, old_list):
    old_list = set(old_list)
    return [item for item in new_list if item not in old_list]


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

    def test_filter_and_create_new_apps(self):
        appids = App.objects.all().values_list('appid', flat=True)
        new_appids = [730, 440]
        app_objs = []
        for appid in lists_difference(new_appids, appids):
            app_objs.append(App(appid=appid,
                                name="Test",
                                app_type=AppType.objects.get(name="game"),
                                release_date="2018-01-01",
                                developer="Test",
                                publisher="Test"))
        App.objects.bulk_create(app_objs)
        apps = App.objects.filter(appid__in=new_appids)
        self.assertEqual(len(apps), 2)

    def test_update_app_tags(self):
        app = App.objects.get(appid=730)
        app_tags = AppTag.objects.filter(app=app.id).values_list('tag__name', flat=True)
        new_tags = ["FPS", "Shooter"]
        for tag_name in lists_difference(new_tags, app_tags):
            tag = Tag.objects.create(name=tag_name)
            AppTag.objects.create(app=app, tag=tag)
        self.assertEqual(len(AppTag.objects.filter(app=app)), 3)

    def test_get_apps_for_update(self):
        update_threshold = datetime.now() - timedelta(days=1)
        apps = App.objects.filter(date_modified__gte=update_threshold)
        self.assertEqual(len(apps), 1)

