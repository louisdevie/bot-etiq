import unittest

import utils, config


class TestsUtils(unittest.TestCase):
    def test_split_command(self):
        self.assertListEqual(
            utils.split_command(f"{config.PREFIX} cmd a b c"), ["cmd", "a", "b", "c"]
        )

        self.assertListEqual(utils.split_command(f"{config.PREFIX} cmd"), ["cmd"])

        self.assertListEqual(utils.split_command(f"{config.PREFIX}"), [])

        self.assertListEqual(
            utils.split_command(f"{config.PREFIX}      cmd   abc  def     ghi"),
            ["cmd", "abc", "def", "ghi"],
        )
