#获取客户端引擎API模块
import mod.client.extraClientApi as clientApi
#获取客户端system的基类ClientSystem
ClientSystem = clientApi.GetClientSystemCls()
#获取组件
compFactory = clientApi.GetEngineCompFactory()
#获取配置
import modConfig as config
# 在modMain中注册的client system类
class TutorialClientSystem(ClientSystem):

    #客户端system的初始化函数
    def __init__(self, namespace, systemName):
        super(TutorialClientSystem,self).__init__(namespace, systemName)
        print ("===== TutorialClientSystem init ====")
        self.mRotatingDict = {} # entityId:boolean
        self.mUseCustomMaterialDict = {} # entityId:boolean
		# 控制玩家材质切换的变量
        # self.queryIsCustomMaterial = 'query.mod.is_custom_material'
        comp = compFactory.CreateQueryVariable(clientApi.GetLevelId())
        # result = comp.Register(self.queryIsCustomMaterial, 0.0)
		# # 控制松鼠动画切换的变量
        self.queryIsMoving = 'query.mod.is_moving'
        result = comp.Register(self.queryIsMoving, 0.0)
        comp1 = compFactory.CreateQueryVariable("netease:jawgiant")
        comp1.Set(self.queryIsMoving,1.0)
		# # 控制松鼠渲染控制器变化的变量
        # self.queryIsEnchanted = 'query.mod.is_enchanted'
        # result = comp.Register(self.queryIsEnchanted, 0.0)
		# 注册玩家move.legs和move.arms动作控制变量
        # self.PlayerSetting()
        self.ListenEvent()


    #     self.ListenForEvent("TutorialMod","TutorialServerSystem", 'PlayerJoinOKEvent', self, self.OnPlayerJoinOK)

    # def OnPlayerJoinOK(self, args):
    #     #args的结果为：{'uid':123, 'name':'nickname'}
    #     print ('OnPlayerJoinOK', args)    

    # 监听函数，用于定义和监听函数
    def ListenEvent(self): 
        print ("============ ClientListenEvent =============")
        
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUIInitFinished)

    #     # 在自定义的ServerSystem中监听引擎的事件
    #     self.ListenForEvent(config.serverNamespace,config.serverSystemName,"Function_1",self,self.PlayerSetting)
    def OnUIInitFinished(self, *args):
        clientApi.RegisterUI(config.ModName, config.UIName, config.UIPyClsPath, config.UIScreenDef)
        clientApi.CreateUI(config.ModName, config.UIName,{"isHud": 1})

    def Animation(self):
        PlayerId = clientApi.GetLocalPlayerId()
        comp = clientApi.GetEngineCompFactory().CreateActorRender(PlayerId)
        comp.AddPlayerAnimationController()
    # 玩家加入游戏后对玩家的设置
    def PlayerSetting(self):
        print ("============== PlayerSetting Success! ===============")
        PlayerId = clientApi.GetLocalPlayerId()
        levelId = clientApi.GetLevelId()
        compView = compFactory.CreatePlayerView(PlayerId)
        compView.SetPerspective(1)
        
        # entityFoootPos = compFactory.CreatePos(PlayerId)
        comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
        # comp.SetCameraAnchor(entityFoootPos)
        comp.DepartCamera()
        comp.LockModCameraYaw(1) # 锁定左右视角
        comp.LockModCameraPitch(1) # 锁定上下视角
        comp.SetCameraOffset((0, 0, 5))
        comp.SetCameraRotation((45.0, 0.0, 0.0))
        # comp = compFactory.CreateCamera(levelId)
        # comp.SetCameraOffset(entityFoootPos)


    def Destroy(self):
        pass