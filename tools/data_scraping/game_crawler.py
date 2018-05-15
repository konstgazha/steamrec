import sys
from crawlers import SeleniumCrawler


class GameCrawler(SeleniumCrawler):
    def __init__(self):
        super().__init__()

    def redirect(self, url):
        self.driver.get(url)

    def get_reviews_score(self):
        xpath = "//div[@class='user_reviews_summary_row']"
        review_scores = self.parse_elems_by_xpath(xpath)
        recent_review_score = ''
        total_review_score = ''
        if review_scores:
            if len(review_scores) == 2:
                recent_review_score = review_scores[0].get_attribute("data-tooltip-text")
                total_review_score = review_scores[1].get_attribute("data-tooltip-text")
            else:
                total_review_score = review_scores[0].get_attribute("data-tooltip-text")
        return (total_review_score, recent_review_score)

    def get_release_date(self):
        xpath = "//div[@class='date']"
        try:
            release_date = self.parse_elems_by_xpath(xpath)[0].text
        except:
            release_date = ''
        return release_date

    def get_developers(self):
        xpath = "//div[@id='developers_list']"
        more_btn = "//div[@class='more_btn']"
        try:
            self.parse_elems_by_xpath(more_btn)[0].click()
            developers = self.parse_elems_by_xpath(xpath)[0].text
        except:
            developers = ''
        return developers

    def get_list_tags(self):
        xpath = "//div[@class='app_tag_control popular']/a[@class='app_tag']"
        more_btn = "//div[@class='app_tag add_button']"
        try:
            self.parse_elems_by_xpath(more_btn)[0].click()
            tag_elems = self.parse_elems_by_xpath(xpath)
        except:
            tag_elems = ''
        tags = []
        for tag in tag_elems:
            tags.append(tag.text)
        return tags

    def get_list_details_specs(self):
        xpath = "//div[@class='game_area_details_specs']"
        try:
            details_specs_elems = self.parse_elems_by_xpath(xpath)
        except:
            details_specs_elems = ''
        details_specs = []
        for elem in details_specs_elems:
            details_specs.append(elem.text)
        return details_specs

url = 'https://store.steampowered.com/app/221380/Age_of_Empires_II_HD/'
gc = GameCrawler()
gc.open()
gc.redirect(url)
gc.get_list_details_specs()
gc.close()