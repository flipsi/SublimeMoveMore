MoveMore
========

A plugin for Sublime Text to move up or down some lines.



What
----

I noticed that it seems to be impossible to simply move the cursor up or down more than one line with one single keystroke. There are ugly workarounds or slightly different functions.
See [here](http://superuser.com/questions/490095/in-sublime-text-2-how-do-i-make-a-key-mapping-to-move-the-cursor-up-or-down-mul) and [here](http://tonyspiro.com/sublime-text-key-binding-to-move-multiple-lines/).

This plugin implements exactly what I want.



Installation
------------

### Package Control

I did not take care of that yet. Maybe I will.

### Manually

Clone this repository:

`git clone https://github.com/sflip/SublimeMoveMore`

(or download it manually) and place it in your Packages folder.



Usage
-----

I added some default keymaps:

```
[
    { "keys": ["ctrl+alt+down"], "command": "move_more", "args": {"amount": 5 } },
    { "keys": ["ctrl+alt+up"], "command": "move_more", "args": {"amount": -5 } }
]
```

But just define your own, you know how to do that, don't you?



Author
------

Philipp Moers <soziflip@gmail.com>

Please don't hesitate to contact me!

