

# -----------------------------
# BasePage class. All page objects will inherit from this class.
# It contains common methods that can be used on any page, like goto(), click(), is_visible(), etc.
# -----------------------------

class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def is_visible(self, selector):
        return self.page.is_visible(selector)
    
    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")

