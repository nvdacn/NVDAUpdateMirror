# Chinese Community Update Mirror for NVDA
# Copyright 2022-2023 Cary-Rowen <manchen_0528@outlook.com>, zh-yx <zhyx-work@outlook.com>
# released under GPL.

import json
import os.path
import shutil

import globalPluginHandler
import NVDAState
import updateCheck
import versionInfo
from logHandler import log

MIRROR_CHECK_UPDATE_URL: str = "https://nvaccess.mirror.nvdadr.com/nvdaUpdateCheck"
MIRROR_STORE_URL: str = "https://nvaccess.mirror.nvdadr.com/addonStore/"
REQUIRED_PRIVATE_API_VERSION: tuple = (2023, 2)
REQUIRED_API_VERSION: tuple = (2004, 1)

CURRENT_API_VERSION: tuple = (versionInfo.version_year, versionInfo.version_major)
JSON_FILE_PATH: str = os.path.join(NVDAState.WritePaths.addonStoreDir, "_cachedCompatibleAddons.json")


def deleteAddonStoreCache(check_mirror: bool = True) -> None:
	if os.path.exists(JSON_FILE_PATH):
		try:
			if check_mirror:
				with open(JSON_FILE_PATH, 'r') as json_file:
					data = json.load(json_file)
				if "data" in data:
					data = json.loads(data["data"])
					url = data[0]["URL"]
					if isinstance(url, str) and "https://github.mirror.nvdadr.com" in url:
						return
			log.info("Delete old add-on store cache.")
			shutil.rmtree(NVDAState.WritePaths.addonStoreDir)
		except Exception as e:
			log.error(f"Add-on store cache deletion failed: {e}")


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		log.info(f"Set the NVDA update mirror to: {MIRROR_CHECK_UPDATE_URL}")
		self.originalURL = updateCheck.CHECK_URL
		updateCheck.CHECK_URL = MIRROR_CHECK_UPDATE_URL
		if CURRENT_API_VERSION >= REQUIRED_PRIVATE_API_VERSION:
			log.info(f"Set the Add-on store mirror to: {MIRROR_STORE_URL}")
			self.original_BASE_URL = self.swapNetworkBaseURL(MIRROR_STORE_URL)

	def swapNetworkBaseURL(self, URL: str) -> str:
		# The original URL is used to restore the original network base URL.
		originalURL: str = ""

		if CURRENT_API_VERSION >= REQUIRED_API_VERSION:
			from addonStore import dataManager, network
			originalURL = network.BASE_URL
			network.BASE_URL = URL
		else:
			from _addonStore import dataManager, network
			originalURL = network._BASE_URL
			network._BASE_URL = URL

		dataManager.initialize()
		deleteAddonStoreCache()
		return originalURL

	def terminate(self):
		log.info(f"Restore NVDA update URL to: {self.originalURL}")
		updateCheck.CHECK_URL = self.originalURL
		if CURRENT_API_VERSION >= REQUIRED_PRIVATE_API_VERSION:
			log.info(f"Restore the Add-on store URL to: {self.original_BASE_URL}")
			self.swapNetworkBaseURL(self.original_BASE_URL)
			# Delete mirror cache
			deleteAddonStoreCache(check_mirror=False)
