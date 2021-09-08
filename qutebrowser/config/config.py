## Autogenerated config.py
##
## NOTE: config.py is intended for advanced users who are comfortable
## with manually migrating the config file on qutebrowser upgrades. If
## you prefer, you can also configure qutebrowser using the
## :set/:bind/:config-* commands without having to write a config.py
## file.
##
## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html


## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
config.load_autoconfig(False)

## Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## Type: Dict
c.aliases = {
    'qa'     : 'quit',
    'w'      : 'session-save',
    'wqa'    : 'quit --save',
    'GitHub' : 'open -t https://github.com/EgorTolbaev',}

# Setting dark mode
#config.set("colors.webpage.darkmode.enabled", True)

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'always'

# Setting default page for when opening new tabs or new windows with
# commands like :open -t and :open -w .
c.url.start_pages = 'c:/homepage/html/homepage.html'


# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`).  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {
    'DEFAULT'  : 'https://duckduckgo.com/?q={}',
    'goog'     : 'https://www.google.com/search?q={}',
    'yt'       : 'https://www.youtube.com/results?search_query={}',
    'GitHub'   : 'https://github.com/search?q={}'
}

# For convenience, I split the config into logical scripts

# Loading a color theme
config.source('color_theme.py')

# Loading fronts
config.source('fonts.py')

# Unbind some standard qutebrowser bindings
c.bindings.default = {}
# If you don't want to unbind everything it might be necessary to
# unbind at least the conflicting keybindings like this:
# config.unbind('<Ctrl-x>')

# If you use Emacs in your work, you can connect a key binding similar to what is in it.
# If this does not suit you, just comment out the line below, as well as the line disabling the standard qutebrowser bindings.
config.source('keybindings_emacs.py')

# Bindings for normal mode
config.bind('t',        'set-cmd-text -s :open -t')
config.bind('xb',       'config-cycle statusbar.show always never')
config.bind('xt',       'config-cycle tabs.show always never')
config.bind('xx',       'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
config.bind('i',        'mode-enter insert', mode='normal')
config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave', mode='normal')
config.bind('ii', 'mode-leave', mode='insert')