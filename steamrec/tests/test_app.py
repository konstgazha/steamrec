import unittest
import sys
sys.path.append('../')
from game_crawler import GameCrawler

gc = GameCrawler()
gc.open()
url = 'https://store.steampowered.com/app/221380/Age_of_Empires_II_HD/'
gc.redirect(url)

class TestGameParsingMethods(unittest.TestCase):
    def test_get_recent_review_score(self):
        recent_review_score = gc.get_recent_review_score()
        self.assertEqual(recent_review_score, (92, 824))

    def test_get_total_review_score(self):
        total_review_score = gc.get_total_review_score()
        self.assertEqual(total_review_score, (94, 39534))

    def test_get_release_date(self):
        release_date = gc.get_release_date()
        self.assertEqual(release_date, '9 апр. 2013')

    def test_get_developers(self):
        developers = gc.get_developers()
        self.assertEqual(developers, 'Skybox Labs, Hidden Path Entertainment, Ensemble Studios')

    def test_get_tags(self):
        tags = gc.get_list_tags()
        self.assertNotEqual(tags, [])

    def test_details_specs(self):
        details_specs = gc.get_list_details_specs()
        self.assertNotEqual(details_specs, [])

if __name__ == '__main__':
    unittest.main(exit=False)

gc.close()