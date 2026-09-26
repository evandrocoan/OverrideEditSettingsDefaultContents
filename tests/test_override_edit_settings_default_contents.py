import importlib.util
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


PLUGIN_PATH = Path(__file__).resolve().parents[1] / "override_edit_settings_default_contents.py"


class EditSettingsTests(unittest.TestCase):
    def setUp(self):
        sublime = types.ModuleType("sublime")
        sublime_plugin = types.ModuleType("sublime_plugin")
        sublime_plugin.EventListener = type("EventListener", (), {})
        self.module_patch = patch.dict(sys.modules, {"sublime": sublime, "sublime_plugin": sublime_plugin})
        self.module_patch.start()
        self.addCleanup(self.module_patch.stop)
        spec = importlib.util.spec_from_file_location("edit_settings_under_test", PLUGIN_PATH)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)
        self.listener = plugin.OverrideEditSettingsDefaultContentsListener()

    def test_non_string_default_is_passed_through(self):
        for value in (None, 42, ["text"]):
            with self.subTest(value=value):
                args = {"default": value}
                self.assertIsNone(self.listener.on_window_command(None, "edit_settings", args))
                self.assertEqual(args["default"], value)

    def test_nonempty_string_is_removed(self):
        args = {"default": "initial contents"}
        self.assertEqual(
            self.listener.on_window_command(None, "edit_settings", args),
            ("edit_settings", {"default": ""}),
        )

    def test_empty_string_and_other_commands_are_unchanged(self):
        self.assertIsNone(self.listener.on_window_command(None, "edit_settings", {"default": ""}))
        self.assertIsNone(self.listener.on_window_command(None, "other", {"default": "text"}))


if __name__ == "__main__":
    unittest.main()
