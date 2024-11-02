from django.urls import reverse
from playwright.sync_api import Page

def test_display_empty_list_on_first_load(live_server, page: Page):
    url = reverse_url(live_server, "index")

     ## NameError. This is intentional. Please leave it here for now. We are doing this to check our wiring!

    page.goto(url)
    page.wait_for_selector("text=Nothing to see")


def reverse_url(
    live_server, viewname, urlconf=None, args=None, kwargs=None, current_app=None
):
    end = reverse(viewname, urlconf, args, kwargs, current_app)
    return f"{live_server.url}{end}"
