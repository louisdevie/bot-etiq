import config


def split_command(cmd):
    # remove prefix
    without_prefix = cmd.split(config.PREFIX, 1)[1]
    # split at whitespaces
    parts = without_prefix.split(" ")
    # remove empty parts (to ignore multiple spaces in a command)
    return [p for p in parts if p]
