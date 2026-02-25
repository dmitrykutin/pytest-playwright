import time

import pytest


# This is our one test file for testing main page (index.html)


@pytest.mark.ui
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


# for this test here we have mark - @pytest.mark.iframe
# it registered in pytest.ini file in the root of the project
# so now we can run only tests with this mark
# by running command like pytest -m iframe
@pytest.mark.iframe
@pytest.mark.ui
def test_text_in_iframe(main_page):
    main_page.click_iframe_button()
    text = main_page.get_text_from_iframe()
    assert text == "Pressed"
