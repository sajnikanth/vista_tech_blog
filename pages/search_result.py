from holmium.core import Page, Elements, Locators


class SearchResultPage(Page):

    search_results = Elements(Locators.CLASS_NAME, 'category')
