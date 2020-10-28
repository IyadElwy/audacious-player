import audtool
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

class KeywordQueryEventListener(EventListener):
	def on_event(self, event, extension):
		if not audtool.is_playing():
			return RenderResultListAction([ExtensionResultItem(icon="images/icon.png", name="Audacious not installed or not playing", on_enter=HideWindowAction())])
		args = event.get_argument()
		if args is not None:
			extension.logger.debug(args)
			songs = audtool.display_songs()
			songs = [s for s in songs if args.lower() in s["name"].lower()]
			songs = songs[:5]
			items = []
			if len(songs) < 1:
				return RenderResultListAction([ExtensionResultItem(icon="images/playlist.png", name="Not found", description="Can't find a music with that name in your playlist.", on_enter=extension.render_main_page())])
			for song in songs:
				items.append(ExtensionResultItem(icon="images/song.png", name=song["name"], description="Press enter to play this song", on_enter=ExtensionCustomAction({"action": "jump", "pos": song["pos"]})))
			return RenderResultListAction(items)

		return extension.render_main_page()