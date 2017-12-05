

import sublime
import sublime_plugin


class OverrideEditSettingsDefaultContentsListener(sublime_plugin.EventListener):
    """
        Disables the default text provided by `edit_settings` to allow the window to be closed
        without the save prompt, when not changes are preformed.
    """

    def on_window_command(self, window, command_name, args):
        # print( "command_name: %s, args: %s" % ( command_name, args ) )

        if command_name == "edit_settings":
            new_default_text = ""

            # Avoid an infinity loop, by rewriting this command again
            if len( args['default'] ) != len( new_default_text ):

                args['default'] = new_default_text
                return ("edit_settings", args)


