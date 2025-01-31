from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import ItemEnterEvent, KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

import audtool
from ItemEnterEventListener import ItemEnterEventListener


class AudExtension(Extension):
    def __init__(self):
        super(AudExtension, self).__init__()
        self.logger.info("Inializing Audacious Extension")
        self.subscribe(KeywordQueryEvent, self.render_main_page_event)
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self._status = None
        self._current_song = None

    def render_main_page_event(self, event):
        return self.render_main_page()

    def _update_state(self):
        """Update the cached player state."""
        self._status = audtool.status()
        self._current_song = audtool.get_current_song()

    def render_main_page(self):
        self._update_state()  # Update the cached state
        items = []
        current_song = audtool.get_current_song()
        if self._status == "playing":
            items.append(
                ExtensionResultItem(
                    icon="images/pause.png",
                    name="Pause",
                    on_enter=ExtensionCustomAction(
                        {"action": "playpause"}, keep_app_open=True
                    ),
                    description=self._current_song + " " + "(Paused)",
                )
            )
        else:
            items.append(
                ExtensionResultItem(
                    icon="images/play.png",
                    name="Play",
                    on_enter=ExtensionCustomAction(
                        {"action": "playpause"}, keep_app_open=True
                    ),
                    description=self._current_song + " " + "(Paused)",
                )
            )

        items.append(
            ExtensionResultItem(
                icon="images/next.png",
                name="Next Song",
                description="Skip current song and go to next song",
                on_enter=ExtensionCustomAction({"action": "next"}, keep_app_open=True),
            )
        )
        items.append(
            ExtensionResultItem(
                icon="images/prev.png",
                name="Previus Song",
                description="Return to previus song",
                on_enter=ExtensionCustomAction({"action": "prev"}, keep_app_open=True),
            )
        )

        items.append(
            ExtensionResultItem(
                icon="images/volume_up.png",
                name="Volume UP",
                description="Press enter to increase volume",
                on_enter=ExtensionCustomAction(
                    {"action": "volume_up"}, keep_app_open=True
                ),
            )
        )
        items.append(
            ExtensionResultItem(
                icon="images/volume_down.png",
                name="Volume DOWN",
                description="Press enter to decrease volume",
                on_enter=ExtensionCustomAction(
                    {"action": "volume_down"}, keep_app_open=True
                ),
            )
        )

        return RenderResultListAction(items)


if __name__ == "__main__":
    AudExtension().run()
