import time


# This is our one test file for testing main page (index.html)


def test_open_modal(main_page):
    main_page.open_modal()

    # it checks if the modal is visible.
    # if main_page.is_modal_visible() returns True, the assertion will pass
    assert main_page.is_modal_visible()
    main_page.close_modal()
    assert not main_page.is_visible("#modal")
    main_page.scroll_to_bottom()
    # Added sleeps here to show that it works really,
    # because it is too fast to see
    time.sleep(3)
    main_page.scroll_to_top()
    time.sleep(3)
