# NVDA Update Mirror
# A global plugin for NVDA
# Copyright 2023 好奇的01<zhyx-work@outlook.com>
# Released under GPL.

import globalPluginHandler
import updateCheck
from   logHandler   import   log

MIRROR_CHECK_UPDATE_URL = "https://nvaccess.mirror.viyf.org/nvdaUpdateCheck"

PRIVACY_STATEMENT = """VIYF 镜像源更新服务
加速 NVDA 更新下载速度，改善您的体验。
我们不收集和存储您的任何信息，您的更新请求都会按原样转送给 NVAccess 处理。
https://www.viyf.org/
"""

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		log.info(PRIVACY_STATEMENT)
		self.originalUrl = updateCheck.CHECK_URL
		updateCheck.CHECK_URL = MIRROR_CHECK_UPDATE_URL

	def terminate(self):
		updateCheck.CHECK_URL = self.originalUrl
