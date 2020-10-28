import audtool
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        extension.logger.debug(str(data))
        if data["action"] == "display":
            songs = audtool.display_songs()
            length = len(songs)
            songs = songs[(data["page"]-1)*5:data["page"]*5]
            items = []
            for song in songs:
                items.append(ExtensionResultItem(icon="images/song.png", name=song["name"], description=song["length"], on_enter=ExtensionCustomAction({"action": "jump", "pos": song["pos"]})))
            if not data["page"]*5 >= length:
                items.append(ExtensionResultItem(icon="images/next_page.png", name="Next Page", on_enter=ExtensionCustomAction({"action": "display", "page":data["page"]+1}, keep_app_open=True)))
            return RenderResultListAction(items)
        elif data["action"] == "jump":
            audtool.jump(data["pos"])
        elif data["action"] == "playpause":
            audtool.playpause()
        elif data["action"] == "next":
            audtool.next()
        elif data["action"] == "prev":
            audtool.prev()
        elif data["action"] == "volume_up":
            audtool.volume("+5")
            return extension.render_main_page()
        elif data["action"] == "volume_down":
            audtool.volume("-5")
            return extension.render_main_page()