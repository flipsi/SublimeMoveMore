MoveMore
========

A plugin for Sublime Text to move up or down some lines.



Description
-----------

I noticed that it seems to be impossible to simply move the cursor up or down more than one line with one single keystroke. There are cumbersome workarounds or ideas with a slightly different effect (see [here](http://superuser.com/questions/490095/in-sublime-text-2-how-do-i-make-a-key-mapping-to-move-the-cursor-up-or-down-mul) and [here](http://tonyspiro.com/sublime-text-key-binding-to-move-multiple-lines/)).

This plugin implements exactly the desired cursor movement.



Installation
------------

### Package Control

Use the `Install Package` command of [Package Control](https://packagecontrol.io/) and search for `MoveMore`.

### Manually

Clone this repository:

`git clone https://github.com/sflip/SublimeMoveMore`

(or download it manually) and place it in your Sublime Packages folder.



Usage
-----

I added some default key bindings you can use right away:

```
{ "keys": ["ctrl+alt+down"], "command": "move_more", "args": { "amount": 5 } },
{ "keys": ["ctrl+alt+up"], "command": "move_more", "args": { "amount": 5, "forward": false } },

```

But feel free to define your own. You know how to do that, don't you?



Author
------

Philipp Moers <soziflip@gmail.com>

Please do not hesitate to contact me!

