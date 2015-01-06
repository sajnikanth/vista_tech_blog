from holmium.core import Page, Element, Locators


class HomePage(Page):

    search_box = Element(Locators.CLASS_NAME, 'header-search-bar-input')
    search_button = Element(Locators.CLASS_NAME, 'header-search-bar-icon-rebrand')

    def search(self, search_text):
        self.search_box.clear()
        self.search_box.send_keys(search_text)
        self.search_button.click()
