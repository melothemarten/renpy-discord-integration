label splashscreen:
    # This label runs when the game is launched. We need to run the init code here.
    $ discord_init()


label before_main_menu:
    # This label runs just before the main menu loads. We can use this to set the
    # Discord status to say that the player's in the main menu.
    $ discord_update(details="Main Menu", state="Main Screen")
    return


label after_load:
    # This label runs right after a save is loaded. In this case, we want to run
    # a Discord update with no parameters so that the Rich Presence gets updated
    # with the game's state in the current loaded save.
    $ discord_update()
    return


label quit:
    # This label runs when the user closes the game. We need to shutdown the
    # integrations beforehand.
    $ discord_shutdown()
    return
