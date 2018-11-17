#!/usr/bin/env python3

import webbrowser

browser = "google-chrome"
web_site_url = "https://www.google.com"

# Open a new browser
webbrowser.get(browser).open_new(web_site_url)
