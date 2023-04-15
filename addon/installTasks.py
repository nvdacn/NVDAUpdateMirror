import addonHandler

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.name == "viyfMirror":
			addon.requestRemove()
			break
