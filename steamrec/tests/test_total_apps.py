import unittest
import sys
sys.path.append('../')
import game_crawler, crawlers

crawler = crawlers.SeleniumCrawler()
crawler.open()


class TestTotalApps(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTotalApps, self).__init__(*args, **kwargs)
        self.url_all_apps_by_release = 'https://store.steampowered.com/search/?sort_by=Released_DESC&page={}'

    def test_get_all_apps_urls_on_page(self):
        xpath = "//a[@class='search_result_row ds_collapse_flag app_impression_tracked']"
        crawler.driver.get(self.url_all_apps_by_release.format(1))
        apps_urls = crawler.parse_elems_by_xpath(xpath)
        self.assertEqual(len(apps_urls), 25)

if __name__ == '__main__':
    unittest.main(exit=False)

crawler.close()
