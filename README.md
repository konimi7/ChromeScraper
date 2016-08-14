# What?

A proof of concept to scrape web pages using Chrome.

# Why?

In my (very) limited experience, scraping websites beyond logins can be very difficult in Python, particularly where client side code execution is required for authentication where tools such as [ghost.py](http://jeanphix.me/Ghost.py/) are required to effectively emulate a full browser.

The approach of using Chrome means that the only ways you could be detected as a bot server-side would be: frequency of page requests exceeding human capability; pattern of page requests being non-human-like; IP address if run from a cloud.

# How?

This proof of concept uses a Chrome Extension containing a content script and a background script, together with a Python localhost server to control access to the database. The flow is as follows:

* The content script does the scraping and passes the data to the background script
* The background script sends the data to the Python server
* The Python server persists the data in the database (this bit hasn't actually been implemented)
* The Python server retrieves the next page from the database (this bit hasn't actually been implemented)
* The Python server returns the next page to the background script
* The background script communicates the next page to the content script
* The content script causes the next page to be loaded

## Why this structure?

Scrapers typically do a couple of things: they go to multiple pages, and they extract data from those pages. The pages to be scraped may be pre-set, or may be extracted from what's scraped (which is a how a web crawler works).

For anything non-trivial it is generally better to store extracted data in a database. As far as I'm aware there's no way of communicating directly with a database from a Chrome Extension, so the intermediate Python server is required (this could obviously be written in any language - Python just makes it so easy).

In addition to storing the data obtained in the database it is often the case that the set of pages to be scraped will also be stored there (although there are use cases where this is more efficiently stored in the scraping code).

# Installation

To run this you will need the Google Chrome browser and a Python installation. The extension is added via Chrome's extensions page via the *Load unpacked extension* button.

# Initiation

There is very little implemented in the way of initiation for this proof of concept, partly because it will depend on the exact usage requirements. Potential implementation solutions are:

For regular (e.g. daily) scraping:

* Cron job to launch Chrome, the background script has the necessary code to kick off the process. But how to kill Chrome once it's finished?
* Chrome is left always running, the background script uses timers to initiate the scraping

For ad-hoc / user-initiated scraping:

* It would be easiest to initiate this via the Extension's pop-up, with a *go* button
