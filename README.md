
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

