from src.pages.base_page import BasePage


# -----------------------------
# MainPage class. This is our page object for the main page of our app.
# It is inherited from BasePage class, so it has all the common methods like goto(), click(), is_visible(), etc.
# It also has its own methods specific to the main page, like open_modal(), close_modal() etc.
# -----------------------------


class MainPage(BasePage):
    # URL of the page for this page object
    URL = "http://localhost:8000/index.html"

    # Selectors for elements on the page
    def __init__(self, page):
        super().__init__(page)
        self.MODAL_OPEN_BTN = "#open-modal"
        self.MODAL_CLOSE_BTN = "#close-modal"
        self.MODAL = "#modal"
        self.TABLE_ADD_ROW_BTN = "#add-row"
        self.TABLE_BODY = "#data-table tbody"

    # Method to open the page (inherited from BasePage class (base_page.py))
    # but it uses the URL that defined in this class befre
    def goto(self):
        super().goto(self.URL)

    # -----------------------------
    # Methods to interact with the page
    # -----------------------------
    def open_modal(self):
        self.click(self.MODAL_OPEN_BTN)

    def close_modal(self):
        self.click(self.MODAL_CLOSE_BTN)

    def is_modal_visible(self):
        return self.is_visible(self.MODAL)

    def add_table_row(self):
        self.click(self.TABLE_ADD_ROW_BTN)

    def table_rows_count(self):
        return len(self.page.query_selector_all(f"{self.TABLE_BODY} tr"))
