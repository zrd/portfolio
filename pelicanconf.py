AUTHOR = 'The Author'
SITENAME = f"{AUTHOR}'s Portfolio"
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Theme related settings
THEME = 'pelican-themes/pelican-blue'
SIDEBAR_DIGEST = 'Student, Athlete, National Merit Scholar'
FAVICON = 'favicon.ico'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = "the_authors_fake_twitter_url"
MENUITEMS = (('Home', SITEURL),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/'),
    ('github', 'https://github.com/zrd'),
    ("twitter", f"https://x.com/{TWITTER_USERNAME}")
)

DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
