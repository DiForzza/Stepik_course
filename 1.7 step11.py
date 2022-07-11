class AppStore:
    def __init__(self):
        self.list_app = {}
        self.blocked = False
        self.count_apps = 0

    def add_application(self, app):
        self.list_app[id(app)] = app
        print(self.list_app[id(app)])

    def remove_application(self, app):
        self.list_app.pop(id(app))

    def block_application(self, app):
        obj = self.list_app.get(id(app), False)
        if not obj:
            return False
        obj.blocked = True
        return True

    def total_apps(self):
        return len(self.list_app)


class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


store = AppStore()
app_tatata = Application("Tatata")
store.add_application(app_tatata)