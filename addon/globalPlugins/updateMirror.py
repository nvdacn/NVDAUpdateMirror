# NVDA Update Mirror
# A global plugin for NVDA
# Copyright 2023 Cary-Rowen <manchen_0528@outlook.com>, 好奇的01 <zhyx-work@outlook.com>
# Released under GPL.

import globalPluginHandler
import updateCheck
import versionInfo
REQUIRED_VERSION_YEAR, REQUIRED_VERSION_MAJOR= 2023, 2
current_version_year, current_version_major = versionInfo.version_year, versionInfo.version_major

if (current_version_year, current_version_major) >= (REQUIRED_VERSION_YEAR, REQUIRED_VERSION_MAJOR):
    try:
        import _addonStore.dataManager
        isSupported = True
    except ModuleNotFoundError:
        isSupported = False
else:
    isSupported = False

MIRROR_CHECK_UPDATE_URL = "https://nvaccess.mirror.nvdadr.com/nvdaUpdateCheck"
MIRROR_STORE_URL = "https://nvaccess.mirror.nvdadr.com/addonStore/"

def _getAddonStoreURLMirror(channel, lang: str, nvdaApiVersion: str) -> str:
	return MIRROR_STORE_URL + f"{lang}/{channel.value}/{nvdaApiVersion}.json"

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()
		self.originalURL = updateCheck.CHECK_URL
		updateCheck.CHECK_URL = MIRROR_CHECK_UPDATE_URL
		if isSupported:
			self.original_getAddonStoreURL = _addonStore.dataManager._getAddonStoreURL
			_addonStore.dataManager._getAddonStoreURL = _getAddonStoreURLMirror
			_addonStore.dataManager.initialize()

	def terminate(self):
		updateCheck.CHECK_URL = self.originalURL
		if isSupported:
			_addonStore.dataManager._getAddonStoreURL = self.original_getAddonStoreURL
			_addonStore.dataManager.initialize()
