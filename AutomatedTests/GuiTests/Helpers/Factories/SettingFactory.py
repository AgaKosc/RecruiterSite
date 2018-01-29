from AutomatedTests.GuiTests.Settings.DevSettings import DevSettings


class SettingsFactory:
    """
    Klasa obsługująca wybór środowiska. Polecam poczytać trochę o wzorcu projektowym Fabryka.
    """

    @staticmethod
    def getSettings(env):
        if env == 'dev':
            return DevSettings()
        raise Exception("No such '{0}' env exists".format(env))