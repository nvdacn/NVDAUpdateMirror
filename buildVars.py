# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.


# Since some strings in `addon_info` are translatable,
# we need to include them in the .po files.
# Gettext recognizes only strings given as parameters to the `_` function.
# To avoid initializing translations in this module we simply roll our own "fake" `_` function
# which returns whatever is given to it as an argument.
def _(arg):
	return arg


# Add-on information variables
addon_info = {
	# add-on Name/identifier, internal for NVDA
	"addon_name": "NVDACNMirror",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on
	# to be shown on installation and add-on information found in Add-ons Manager.
	"addon_summary": _("NVDA 中文社区更新镜像源"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description": _("""让 NVDA 更新使用 NVDA 中文社区提供的镜像源，加快 NVDA 的更新下载速度。"""),
	# version
	"addon_version": "0.3.0",
	# Author(s)
	"addon_author": "好奇的 01, NVDACN <www.nvdacn.com>",
	# URL for the add-on documentation support
	"addon_url": "https://www.nvdacn.com/",
	# URL for the add-on repository where the source code can be found
	"addon_sourceURL": "https://github.com/nvdacn/NVDAUpdateMirror",
	# Documentation file name
	"addon_docFileName": "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion": "2022.1.0",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion": "2023.1.0",
	# Add-on update channel (default is None, denoting stable releases,
	# and for development releases, use "dev".)
	# Do not change unless you know what you are doing!
	"addon_updateChannel": None,
	# Add-on license such as GPL 2
	"addon_license": "GPL v2",
	# URL for the license document the ad-on is licensed under
	"addon_licenseURL": "https://www.gnu.org/licenses/gpl-2.0.html",
}

# Define the python files that are the sources of your add-on.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions.
# For example to include all files with a ".py" extension from the "globalPlugins" dir of your add-on
# the list can be written as follows:
# pythonSources = ["addon/globalPlugins/*.py"]
# For more information on SCons Glob expressions please take a look at:
# https://scons.org/doc/production/HTML/scons-user/apd.html
pythonSources = ["addon/globalPlugins/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
baseLanguage = "zh_CN"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions = []