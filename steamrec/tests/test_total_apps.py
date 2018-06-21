import unittest
import sys
sys.path.append('../')
import game_crawler


class TestTotalApps(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTotalApps, self).__init__(*args, **kwargs)
        self.url_all_apps_by_release = 'https://store.steampowered.com/search/?sort_by=Released_DESC&page={}'

    def test_get_all_apps_urls_on_page(self):
        total_apps = game_crawler.TotalApps()
        total_apps.open()
        apps_urls = total_apps.test_get_all_apps_urls_on_page(self.url_all_apps_by_release.format(1))
        total_apps.close()
        self.assertEqual(len(apps_urls), 25)

if __name__ == '__main__':
    unittest.main(exit=False)
