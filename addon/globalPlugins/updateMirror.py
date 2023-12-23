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

MIRROR_CHECK_UPDATE_URL = "https://nvaccess.mirror.nvdadr.com/nvdaUpdateCheck"
MIRROR_STORE_URL = "https://nvaccess.mirror.nvdadr.com/addonStore/"
REQUIRED_PRIVATE_API_VERSION = (2023, 2)
REQUIRED_API_VERSION = (2004, 1)

current_api_version = (versionInfo.version_year, versionInfo.version_major)
json_file_path = os.path.join(NVDAState.WritePaths.addonStoreDir, "_cachedCompatibleAddons.json")


def deleteAddonStoreCache():
	if os.path.exists(json_file_path):
		try:
			with open(json_file_path, 'r') as json_file:
				data = json.load(json_file)
			if "data" in data:
				data = json.loads(data["data"])
				url = data[0]["URL"]
				if isinstance(url, str) and "https://github.mirror.nvdadr.com" not in url:
					log.info("Delete old add-on store cache.")
					shutil.rmtree(os.path.dirname(json_file_path))
		except Exception as e:
			log.error(f"Add-on store cache deletion failed: {e}")


def swapURL(URL):
	originalURL = ""
	if current_api_version >= REQUIRED_API_VERSION:
		from addonStore import dataManager, network
		originalURL = network.BASE_URL
		network.BASE_URL = URL
		dataManager.initialize()
		deleteAddonStoreCache()
		return originalURL
	elif current_api_version >= REQUIRED_PRIVATE_API_VERSION:
		from _addonStore import dataManager, network
		originalURL = network._BASE_URL
		network._BASE_URL = URL
		dataManager.initialize()
		deleteAddonStoreCache()
		return originalURL


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()
		log.info(f"Set the NVDA update mirror to: {MIRROR_CHECK_UPDATE_URL}")
		self.originalURL = updateCheck.CHECK_URL
		updateCheck.CHECK_URL = MIRROR_CHECK_UPDATE_URL
		if current_api_version >= REQUIRED_PRIVATE_API_VERSION:
			log.info(f"Set the Add-on store mirror to: {MIRROR_STORE_URL}")
			self.original_BASE_URL = swapURL(MIRROR_STORE_URL)

	def terminate(self):
		log.info(f"Restore NVDA update URL to: {self.originalURL}")
		updateCheck.CHECK_URL = self.originalURL
		if current_api_version >= REQUIRED_PRIVATE_API_VERSION:
			log.info(f"Restore the Add-on store URL to: {self.original_BASE_URL}")
			swapURL(self.original_BASE_URL)
			# Delete mirror cache
			if os.path.exists(json_file_path):
				try:
					log.info("Delete old add-on store cache.")
					shutil.rmtree(os.path.dirname(json_file_path))
				except Exception as e:
					log.error(f"Add-on store cache deletion failed: {e}")
