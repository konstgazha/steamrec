import unittest
import sys
sys.path.append('../')
import crawlers

crawler = crawlers.SeleniumCrawler()
crawler.open()
url = 'https://store.steampowered.com/app/221380/Age_of_Empires_II_HD/'
crawler.driver.get(url)
crawler.wait_loading_by_class('user_reviews')

class TestGameParsingMethods(unittest.TestCase):
    def test_get_reviews_score(self):
        xpath = "//div[@class='user_reviews_summary_row']"
        review_scores = crawler.parse_elems_by_xpath(xpath)
        recent_review_score = ''
        total_review_score = ''
        if review_scores:
            if len(review_scores) == 2:
                recent_review_score = review_scores[0].get_attribute("data-tooltip-text")
                total_review_score = review_scores[1].get_attribute("data-tooltip-text")
            else:
                total_review_score = review_scores[0].get_attribute("data-tooltip-text")
        self.assertTrue(recent_review_score or total_review_score)

    def test_get_release_date(self):
        xpath = "//div[@class='date']"
        try:
            release_date = crawler.parse_elems_by_xpath(xpath)[0].text
        except:
            release_date = ''
        self.assertTrue(release_date)

    def test_get_developers(self):
        xpath = "//div[@id='developers_list']"
        more_btn = "//div[@class='more_btn']"
        try:
            crawler.parse_elems_by_xpath(more_btn)[0].click()
            developers = crawler.parse_elems_by_xpath(xpath)[0].text
        except:
            developers = ''
        self.assertTrue(developers)

if __name__ == '__main__':
    unittest.main(exit=False)

crawler.close()