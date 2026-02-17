import time


# This is our one test file for testing main page (index.html)

def test_open_modal(main_page):
    main_page.open_modal()
    assert main_page.is_modal_visible()
    main_page.close_modal()
    assert not main_page.is_visible("#modal")
    main_page.scroll_to_bottom()
    # Let's wait a bit to see the scroll effect before scrolling back to top
    time.sleep(3)
    main_page.scroll_to_top()

