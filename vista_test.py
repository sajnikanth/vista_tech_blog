import unittest
import pages


class VistaPrintTest(unittest.TestCase):

    def setUp(self):
        self.home_page = pages.home.HomePage(self.driver, self.config['base_url'])
        self.search_results_page = pages.search_result.SearchResultPage(self.driver)

    def test_search(self):
        self.home_page.search('Business Card')
        assert 'Business-Card' in self.driver.current_url
        assert 'Business Card' in self.search_results_page.search_results[0].text

if __name__ == "__main__":
    unittest.main()
