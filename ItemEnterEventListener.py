from ulauncher.api.client.EventListener import EventListener

import audtool


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        extension.logger.debug(str(data))
        if data["action"] == "playpause":
            audtool.playpause()
            return extension.render_main_page()
        elif data["action"] == "next":
            audtool.next()
            return extension.render_main_page()
        elif data["action"] == "prev":
            audtool.prev()
            return extension.render_main_page()
        elif data["action"] == "volume_up":
            audtool.volume("+5")
            return extension.render_main_page()
        elif data["action"] == "volume_down":
            audtool.volume("-5")
            return extension.render_main_page()
