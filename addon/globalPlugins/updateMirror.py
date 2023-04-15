# NVDA Update Mirror
# A global plugin for NVDA
# Copyright 2023 好奇的01<zhyx-work@outlook.com>
# Released under GPL.

import globalPluginHandler
import updateCheck
from   logHandler   import   log

MIRROR_CHECK_UPDATE_URL = "https://nvaccess.mirror.nvdadr.com/nvdaUpdateCheck"

PRIVACY_STATEMENT = """VIYF 镜像源更新服务
本镜像源更新服务，旨在加速 NVDA 的更新速度，为 NVDA 中文用户提供更好的使用体验。
请放心使用，我们不会收集或存储您的任何信息。您的更新请求都会按照原样转送给 NV Access 进行处理。
https://www.nvdacn.com/
"""

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		log.info(PRIVACY_STATEMENT)
		self.originalUrl = updateCheck.CHECK_URL
		updateCheck.CHECK_URL = MIRROR_CHECK_UPDATE_URL

	def terminate(self):
		updateCheck.CHECK_URL = self.originalUrl
