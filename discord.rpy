# MIT License

# Copyright (c) 2021 Melodic Stream (https://github.com/melodicstream/renpy-discord-integration)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


default persistent.discord_integration = True


init -20 python:
    from __future__ import print_function

    import discord_rpc
    import time

    start_time = time.time()
    discord_initialized = False

    def callback_ready(current_user):
        print("Discord RPC running with user: ", current_user)


    def callback_disconnected(codeno, codemsg):
        print("Disconnected from Discord rich presence RPC. Code {}: {}".format(codeno, codemsg))


    def callback_error(errno, errmsg):
        print("An error occurred! Error {}: {}".format(errno, errmsg))


    def discord_init():
        global discord_initialized

        print("Initializing Discord integration.")

        if not persistent.discord_integration:
            return

        if discord_initialized:
            return

        callbacks = {
            "ready": callback_ready,
            "disconnected": callback_disconnected,
            "error": callback_error,
        }

        discord_rpc.initialize("<YOUR CLIENT ID GOES HERE>", callbacks=callbacks, log=True)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

        discord_initialized = True


    def discord_update(**kwargs):
        """
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
        """
        global discord_initialized
        global start_time

        print("Updating Discord integration.")

        if not persistent.discord_integration:
            if discord_initialized:
                discord_shutdown()
            return

        if not discord_initialized:
            discord_init()

        kwargs["start_timestamp"] = start_time

        discord_rpc.update_presence(**kwargs)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()


    def discord_shutdown():
        global discord_initialized

        print("Shutting down Discord integration.")

        if discord_initialized:
            discord_rpc.shutdown()
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()

        discord_initialized = False
