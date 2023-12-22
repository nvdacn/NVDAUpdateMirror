# Chinese Community Update Mirror for NVDA
# Copyright 2022-2023 Cary-Rowen <manchen_0528@outlook.com>, zh-yx <zhyx-work@outlook.com>
# released under GPL.

import globalPluginHandler
import updateCheck
import versionInfo

MIRROR_CHECK_UPDATE_URL = "https://nvaccess.mirror.nvdadr.com/nvdaUpdateCheck"
MIRROR_STORE_URL = "https://nvaccess.mirror.nvdadr.com/addonStore/"
REQUIRED_PRIVATE_API_VERSION = (2023, 2)
REQUIRED_API_VERSION = (2004, 1)

current_api_version = (versionInfo.version_year, versionInfo.version_major)

if current_api_version >= REQUIRED_API_VERSION:
	try:
		from addonStore import dataManager
		from addonStore.network import BASE_URL
		isSupported = True
	except ModuleNotFoundError:
		isSupported = False
elif current_api_version >= REQUIRED_PRIVATE_API_VERSION:
	try:
		from _addonStore import dataManager
		from _addonStore.network import _BASE_URL as BASE_URL
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
			global BASE_URL
			self.original_BASE_URL = BASE_URL
			BASE_URL = MIRROR_STORE_URL
			dataManager.initialize()

	def terminate(self):
		updateCheck.CHECK_URL = self.originalURL
		if isSupported:
			global BASE_URL
			BASE_URL = self.original_BASE_URL
			dataManager.initialize()
