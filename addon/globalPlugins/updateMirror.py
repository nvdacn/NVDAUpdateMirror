# Chinese Community Update Mirror for NVDA
# Copyright 2022-2023 Cary-Rowen <manchen_0528@outlook.com>, zh-yx <zhyx-work@outlook.com>
# released under GPL.

import globalPluginHandler
import updateCheck
import versionInfo

MIRROR_CHECK_UPDATE_URL = "https://nvaccess.mirror.nvdadr.com/nvdaUpdateCheck"
MIRROR_STORE_URL = "https://nvaccess.mirror.nvdadr.com/addonStore/"
REQUIRED_VERSION_YEAR, REQUIRED_VERSION_MAJOR = 2023, 2

current_version_year, current_version_major = versionInfo.version_year, versionInfo.version_major

if (current_version_year, current_version_major) >= (REQUIRED_VERSION_YEAR, REQUIRED_VERSION_MAJOR):
    try:
        import _addonStore.dataManager
        isSupported = True
    except ModuleNotFoundError:
        isSupported = False
else:
    isSupported = False


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()
		self.originalURL = updateCheck.CHECK_URL
		updateCheck.CHECK_URL = MIRROR_CHECK_UPDATE_URL
		if isSupported:
			self.original_BASE_URL = _addonStore.network._BASE_URL
			_addonStore.network._BASE_URL = MIRROR_STORE_URL
			_addonStore.dataManager.initialize()

	def terminate(self):
		updateCheck.CHECK_URL = self.originalURL
		if isSupported:
			_addonStore.network._BASE_URL = self.original_BASE_URL
			_addonStore.dataManager.initialize()
