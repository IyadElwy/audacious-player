import audtool
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from KeywordQueryEventListener import KeywordQueryEventListener
from ItemEnterEventListener import ItemEnterEventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

class AudExtension(Extension):
    def __init__(self):
        super(AudExtension, self).__init__()
        self.logger.info("Inializing Audacious Extension")
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

    def render_main_page(self):
        status = audtool.status()
        items = []
        current_song = audtool.get_current_song()
        items.append(ExtensionResultItem(icon="images/song.png",name="Current Playing", description=current_song, on_enter=DoNothingAction()))

        if status == "playing":
            items.append(ExtensionResultItem(icon="images/pause.png", name="Pause", on_enter=ExtensionCustomAction({"action": "playpause"})))
        else:
            items.append(ExtensionResultItem(icon="images/play.png", name="Play", on_enter=ExtensionCustomAction({"action": "playpause"})))

        items.append(ExtensionResultItem(icon="images/playlist.png", name="Display Songs", description="Display all songs in current playlist", on_enter=ExtensionCustomAction({"action": "display", "page": 1}, keep_app_open=True)))

        items.append(ExtensionResultItem(icon="images/next.png", name="Next Song", description="Skip current song and go to next song", on_enter=ExtensionCustomAction({"action": "next"})))
        items.append(ExtensionResultItem(icon="images/prev.png", name="Previus Song", description="Return to previus song", on_enter=ExtensionCustomAction({"action": "prev"})))

        items.append(ExtensionResultItem(icon="images/volume_up.png", name="Volume UP", description="Press enter to increase volume", on_enter=ExtensionCustomAction({"action": "volume_up"}, keep_app_open=True)))
        items.append(ExtensionResultItem(icon="images/volume_down.png", name="Volume DOWN", description="Press enter to decrease volume", on_enter=ExtensionCustomAction({"action": "volume_down"}, keep_app_open=True)))

        return RenderResultListAction(items)

if __name__ == '__main__':
    AudExtension().run()