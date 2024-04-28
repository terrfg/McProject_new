#配置文件
#这行是import到MOD的绑定类Mod，用于绑定类和函数
from mod.common.mod import Mod
#这行import到的是引擎服务端的API模块
import mod.server.extraServerApi as serverApi
#这行import到的是引擎客户端的API模块
import mod.client.extraClientApi as clientApi

ModName = "TutorialMod"
ModVersion = "0.0.1"

# Server System
serverNamespace = serverApi.GetEngineNamespace()
serverSystemName = serverApi.GetEngineSystemName()

# Client System
clientNamespace = clientApi.GetEngineNamespace()
clientSystemName = clientApi.GetEngineSystemName()
 

#UI
UIName = "View"
UIPyClsPath = "tutorialScripts.ui.View.ViewUI"
UIScreenDef = "View.main"