

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
            place_holders = ['default']

            new_default_text = ""
            new_default_text_len = len( new_default_text )

            for place_holder in place_holders:

                # Avoid an infinity loop, by rewriting this command again
                if place_holder in args \
                        and len( args[place_holder] ) != new_default_text_len:

                    args[place_holder] = new_default_text

                    # print( "Returning args: " + str( args ) )
                    return ("edit_settings", args)

