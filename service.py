import xbmcaddon
import os

__settings__ = xbmcaddon.Addon(id='plugin.video.xbmb3c')
__cwd__ = __settings__.getAddonInfo('path')
BASE_RESOURCE_PATH = xbmc.translatePath( os.path.join( __cwd__, 'resources', 'lib' ) )
sys.path.append(BASE_RESOURCE_PATH)

from ServiceModule import Monitor

try:
    Monitor().ServiceEntryPoint()
except Exception, msg:
    xbmcgui.Dialog().ok("Error", str(msg))
    raise