import addonHandler
import os
import shutil
import globalVars
import json
from logHandler import log

json_file_path = os.path.join(globalVars.appArgs.configPath, "addonStore", "_cachedCompatibleAddons.json")
def deleteAddonStoreCache():
	try:
		with open(json_file_path, 'r') as json_file:
			data = json.load(json_file)
		if "data" in data:
			data = json.loads(data["data"])
			url = data[0]["URL"]
			if isinstance(url, str) and "https://github.mirror.nvdadr.com" not in url:
				shutil.rmtree(os.path.dirname(json_file_path))
	except Exception as e:
		log.error(f"Add-on store cache deletion failed: {e}")

def onInstall():
	deleteAddonStoreCache()
	for addon in addonHandler.getAvailableAddons():
		if addon.name == "viyfMirror":
			addon.requestRemove()
			break

def onUninstall():
	# Delete mirror cache
	try:
		shutil.rmtree(os.path.dirname(json_file_path))
	except Exception as e:
		log.error(f"Add-on store cache deletion failed: {e}")
