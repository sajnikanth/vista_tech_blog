# Holmium - Page Objects and more

Holmium is a plugin for [nosetests](https://nose.readthedocs.org/en/latest) and helps manage your selenium (python) tests.

Consider the following test case:

    from selenium import webdriver
    import unittest


    class VistaPrintTest(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Firefox()

        def test_search(self):
            self.driver.get('http://vistaprint.com')
            self.driver.find_element_by_class_name('header-search-bar-input').clear()
            self.driver.find_element_by_class_name('header-search-bar-input').send_keys('Business Card')
            self.driver.find_element_by_class_name('header-search-bar-icon-rebrand').click()
            assert 'Business-Card' in self.driver.current_url
            assert 'Business Card' in self.driver.find_elements_by_class_name('category')[0].text

        def tearDown(self):
            self.driver.quit()

    if __name__ == "__main__":
        unittest.main()


Save it as `vista_test.py` and run: `nosetests vista_test.py`, to see the following:

* Firefox is launched
* Vistaprint website is shown
* Search box is cleared and populated with ***Business Card***
* Search button is clicked
* Check if URL contains search-text
* Check if first result contains search-text
* Browser is closed

## Using Holmium

Things can get tricky when the test suite grows and then we notice that the class name has changed. That means every test using the old class name would have to be updated! This is where [Page Objects](https://code.google.com/p/selenium/wiki/PageObjects) help. The upshot is, page objects make it easier to maintain tests and reduces duplicate code.

Holmium helps create page objects quite easily. Here&#39;s how the above test case can be re-written to use holmium page objects:

    from holmium.core import Page, Element, Elements, Locators
    import unittest


    class HomePage(Page):

        search_box = Element(Locators.CLASS_NAME, 'header-search-bar-input')
        search_button = Element(Locators.CLASS_NAME, 'header-search-bar-icon-rebrand')


    class SearchResultsPage(Page):

        search_results = Elements(Locators.CLASS_NAME, 'category')


    class VistaPrintTest(unittest.TestCase):

        def setUp(self):
            self.home_page = HomePage(self.driver, 'http://vistaprint.com')
            self.search_results_page = SearchResultsPage(self.driver)

        def test_search(self):
            self.home_page.search_box.clear()
            self.home_page.search_box.send_keys('Business Card')
            self.home_page.search_button.click()
            assert 'Business-Card' in self.driver.current_url
            assert 'Business Card' in self.search_results_page.search_results[0].text

    if __name__ == "__main__":
        unittest.main()

* Notice that we have 2 page objects for the two pages we used in the test, Vistaprint Home page (`HomePage`) and Search Results page (`SearchResultsPage`)
* We define the elements we want to use in the respective pages
    * So if class name changes in future, we just have to update that in the page object
* `setUp` method instantiates these page objects
    * Notice that, we can directly navigate to Vistaprint Home Page during instantiation
    * The browser name is no longer hard-coded in the test
* `test_search` simply refers to the elements within the page objects; no class names here

We now run the above test like this:


        nosetests vista_test.py --with-holmium --holmium-browser=firefox


## Holmium Config

Next, let&#39;s say this test needs to be run on staging and production environments; hardcoding that url within the test doesn&#39;t help. Luckily, Holmium supports a `config` file and here&#39;s how to do that:


        config = {
        'default': {
            'base_url': '{{holmium.environment}}'
            }
        }

Save the above as `config.py` in the same location as `vista_test.py`. After this, replace the hard-coded URL in the test with `self.config['base_url']` so it's like:


        self.home_page = HomePage(self.driver, self.config['base_url'])

The test can now be run like this:


        nosetests vista_test.py --with-holmium --holmium-browser=firefox --holmium-environment=http://vistaprint.com

And thus, the same test can be used for multiple environments (URL passed as Command Line Option)

## Other Holmium Command Line Options:

Refer to [Holmium Documentation](http://holmiumcore.readthedocs.org/en/latest/unittest.html#command-line-options) for other useful command line options like:

* User Agent
* Capabilities
* Remote Selenium Server URL etc.

## Conclusion

The above example illustrates the simplicity of using Holmium Page Objects and also introduces the various command line options available. If you are someone with very little or no automation test experience, Holmium could be a great place to start. Happy Coding!

## Resources

* Installation - Holmium can be install via pip - `pip install holmium.core`
* [Holmium Documentation](http://holmiumcore.readthedocs.org/)
* [Git Repo for example script](https://github.com/sajnikanth/vista_tech_blog)
