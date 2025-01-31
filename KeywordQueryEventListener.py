from ulauncher.api.client.EventListener import EventListener


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        return extension.render_main_page()
