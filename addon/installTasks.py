# Chinese Community Update Mirror for NVDA
# Copyright 2022-2023 Cary-Rowen <manchen_0528@outlook.com>, zh-yx <zhyx-work@outlook.com>
# released under GPL.

import addonHandler


def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.name == "viyfMirror":
			addon.requestRemove()
			break
