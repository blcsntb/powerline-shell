# Basic theme which only uses colors in 0-15 range

class Color:
    USERNAME_FG = 8
    USERNAME_BG = 15

    HOSTNAME_FG = 8
    HOSTNAME_BG = 7

    PATH_BG = 8 # dark grey
    PATH_FG = 7 # light grey
    CWD_FG = 15 # white
    SEPARATOR_FG = 7

    REPO_CLEAN_BG = 2  # green
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 1  # red
    REPO_DIRTY_FG = 15 # white

    CMD_PASSED_BG = 8
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0