# renpy-discord-integration
Tutorial and files for Discord Integration within Ren'py games.


## How to set up

For the Ren'py part:

1. Copy the `discord.rpy` file into your Ren'py project's `game` folder.
2. Copy the labels in the `script.rpy` file into your own `script.rpy` file.
3. Alternatively, if you already have those labels in your code, just copy the contents of the labels in the `script.rpy` file into your labels.
4. Download and install the latest version of Python from https://www.python.org/ . Make sure to enable the "Add to PATH" option, and feel free to make the path limit longer as well.
5. Open a Powershell shell in the location of your project's game folder.
   1. You can do that by holding down the SHIFT key and right clicking an empty space within the folder and then clicking "Open Powershell window here", or by SHIFT-right clicking the `game` folder itself and clicking the same option.
   2. The Powershell prompt should show the current path displayed in the last line. Make sure you're in the `game` folder!
6. Run the command:

        python -m pip install --target python-packages discord-rpc.py
7. If you're running Renpy below version 7.4, then run the command:

        python -m pip install --target python-packages requests


For the Discord part:

1. Go to https://discord.com/developers
2. Create a new application. The name of your app needs to be the name of your game, since it will show in the Rich Presence embed.
3. Go to the `General Information` tab and copy the Client ID
4. Open the `discord.rpy` file and paste the Client ID in the right place inside the `discord_init()` function


## How to use

Whenever you want to change the Discord Rich Presence embed of the player, call the function `discord_update()`.

This function updates the Rich Presence status of the player playing the game. You can
provide the following parameters:

    (optional) state            : string
    (optional) details          : string
    (optional) large_image_key  : string, lowercase
    (optional) large_image_text : string
    (optional) small_image_key  : string, lowercase
    (optional) small_image_text : string

For example:

    $ discord_update(details="Main Menu", state="Main Screen", large_image_key="logo")

The "image keys" can be set in https://discord.com/developers, under your application's
"Rich Presence" tab. In the "Art Assets" subtab, you can upload images as "Rich Presence
Assets" along with a name. That's the name you need to put in the `image_key` parameters.

Additionally, you can use the Visualizer in your application's page to preview how the Rich presence is going to look.


## Make it toggleable

Some people might not want to show what they're playing on Discord. For that, you should add an option to disable the
Discord integration feature. There are multiple creative ways to do it, but here's a simple one to get started.

In the `screens.rpy` file, around the line 720, there should be a Preferences screen. That's the screen that shows up
when you go into the options menu inside the game. Inside that screen, and keeping in mind the proper indentation levels,
add the following:

    vbox:
        style_prefix "radio"
        label _("Discord Integration")
        textbutton _("On") action SetField(persistent, "discord_integration", True)
        textbutton _("Off") action SetField(persistent, "discord_integration", False)


## Support

If you have any difficulties following the tutorial, or have any questions, feel free to open a Github issue on this repository!


## Licensing

This repository, as well as the code, is licensed under the MIT licence. Make sure to include the MIT license somewhere
readable. For that, I recommend creating a `licenses` folder inside your project's `game` folder and copying the `LICENCE`
file of this repository to there. It should automatically get included in the builds of your game.
