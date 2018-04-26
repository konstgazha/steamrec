import unittest
import sys
sys.path.append('../')
import crawlers

crawler = crawlers.SeleniumCrawler()
crawler.open()

class TestGameParsingMethods(unittest.TestCase):
    def test_get_recent_reviews_score(self):
        url = 'https://store.steampowered.com/app/221380/Age_of_Empires_II_HD/'
        crawler.driver.get(url)
        review_score_block = crawler.parse_elems_by_xpath("//div[@class='user_reviews']")
        if review_score_block:
            review_scores = crawler.parse_elems_by_xpath("//span[contains(@class, 'game_review_summary')]", review_score_block[0])
        recent_review_score = review_scores[0].text.strip()
        self.assertEqual(recent_review_score, 'Очень положительные')

if __name__ == '__main__':
    unittest.main(exit=False)

crawler.close()