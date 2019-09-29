
# Override Edit Settings Default Contents

Usually the packages add the text same text when opening their setting for the first time:
```javascript
[

]
```

However, most times you do not edit or want to save this empty file, then when closing the
settings windows, Sublime Text will prompt you wheter you want to save your changes to the
unsaved file.

This package disables the default text provided by `edit_settings` to allow the window to
be closed without the save prompt, when no changes are preformed on the view.


## Installation

### By Package Control

1. Download & Install `Sublime Text 3` (https://www.sublimetext.com/3)
1. Go to the menu `Tools -> Install Package Control`, then,
   wait few seconds until the `Package Control` installation finishes
1. Go to the menu `Preferences -> Package Control`
1. Type `Package Control Add Channel` on the opened quick panel and press <kbd>Enter</kbd>
1. Then, input the following address and press <kbd>Enter</kbd>
   ```
   https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json
   ```
1. Now, go again to the menu `Preferences -> Package Control`
1. This time type `Package Control Install Package` on the opened quick panel and press <kbd>Enter</kbd>
1. Then, search for `OverrideEditSettingsDefaultContents` and press <kbd>Enter</kbd>

See also:
1. [ITE - Integrated Toolset Environment](https://github.com/evandrocoan/ITE)
1. [Package control docs](https://packagecontrol.io/docs/usage) for details.


### License

See the [LICENSE](LICENSE) file.

