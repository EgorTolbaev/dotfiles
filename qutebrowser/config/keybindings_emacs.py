# Reload config
config.bind('<Ctrl-x><Ctrl-l>', 'config-source')

# Move around on the site
config.bind('<Alt-Shift-,>', 'scroll-to-perc 0')
config.bind('<Alt-Shift-.>', 'scroll-to-perc')
config.bind('<Ctrl-n>',      'scroll down')
config.bind('<Ctrl-p>',      'scroll up')
config.bind('<Ctrl-a>',      'back')
config.bind('<Ctrl-e>',      'forward')

# open url
config.bind('<Ctrl-x><Ctrl-f>',         'set-cmd-text -s :open -t')
config.bind('<Ctrl-u><Ctrl-x><Ctrl-f>', 'set-cmd-text -s :open')
config.bind('<Ctrl-x>l',                'reload')

# close qutebrowser
config.bind('<Ctrl-x><Ctrl-c>', 'quit') # warning: closes all windows

# tab management
config.bind('<Ctrl-x>0', 'tab-close')
config.bind('<Ctrl-x>1', 'tab-only')
config.bind('<Alt-a>',   'tab-prev')
config.bind('<Alt-e>',   'tab-next')

# Searching
config.bind('<Ctrl-s>', 'set-cmd-text /', mode='normal')
config.bind('<Ctrl-r>', 'set-cmd-text ?', mode='normal')
config.bind('<Ctrl-s>', 'search-next',    mode='command')
config.bind('<Ctrl-r>', 'search-prev',    mode='command')

# zooming
config.bind('+', 'zoom-in')
config.bind('-', 'zoom-out')

# command mode
config.bind('<Alt-x>',        'set-cmd-text :')
config.bind('<Up>',           'command-history-prev',       mode='command')
config.bind('<Ctrl-p>',       'command-history-prev',       mode='command')
config.bind('<Down>',         'command-history-next',       mode='command')
config.bind('<Ctrl-n>',       'command-history-next',       mode='command')
config.bind('<Escape>',       'mode-leave',                 mode='command')
config.bind('<Ctrl-g>',       'mode-leave',                 mode='command')
config.bind('<Return>',       'command-accept',             mode='command')
config.bind('<Ctrl-m>',       'command-accept',             mode='command')
config.bind('<Shift-Tab>',    'completion-item-focus prev', mode='command')
config.bind('<Ctrl-Shift-i>', 'completion-item-focus prev', mode='command')
config.bind('<Tab>',          'completion-item-focus next', mode='command')
config.bind('<Ctrl-i>',       'completion-item-focus next', mode='command')

# promt mode
config.bind('<Ctrl-p>',       'prompt-item-focus prev', mode='prompt')
config.bind('<Up>',           'prompt-item-focus prev', mode='prompt')
config.bind('<Ctrl-n>',       'prompt-item-focus next', mode='prompt')
config.bind('<Down>',         'prompt-item-focus next', mode='prompt')
config.bind('<Ctrl-g>',       'mode-leave',             mode='prompt')
config.bind('<Escape>',       'mode-leave',             mode='prompt')
config.bind('<Ctrl-m>',       'prompt-accept',          mode='prompt')
config.bind('<Return>',       'prompt-accept',          mode='prompt')
config.bind('<Ctrl-Shift-i>', 'prompt-item-focus prev', mode='prompt')
config.bind('<Shift-Tab>',    'prompt-item-focus prev', mode='prompt')
config.bind('<Ctrl-i>',       'prompt-item-focus next', mode='prompt')
config.bind('<Tab>',          'prompt-item-focus next', mode='prompt')
config.bind('n',              'prompt-accept no',       mode='prompt')
config.bind('y',              'prompt-accept yes',      mode='prompt')

# hinting
config.bind('<Ctrl-Space>',         'hint')
config.bind('<Ctrl-u><Ctrl-Space>', 'hint --rapid links tab-bg')
config.bind('<Escape>',             'mode-leave',  mode='hint')
config.bind('<Ctrl-g>',             'mode-leave',  mode='hint')
config.bind('<Return>',             'hint-follow', mode='hint')
config.bind('<Ctrl-m>',             'hint-follow', mode='hint')

# copy current site (url/title) to clipboard
config.bind('<Alt-w>', 'yank')
config.bind('<Ctrl-u><Alt-w>d', 'yank domain')
config.bind('<Ctrl-u><Alt-w>p', 'yank pretty-url')
config.bind('<Ctrl-u><Alt-w>t', 'yank title')
