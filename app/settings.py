from .models import SettingsModel

def get(setting):
    model = SettingsModel.get()
    return getattr(model, setting)