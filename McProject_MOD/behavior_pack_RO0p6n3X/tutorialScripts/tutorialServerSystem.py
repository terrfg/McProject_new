# 获取引擎服务器API的模块
import mod.server.extraServerApi as serverApi
# 获取引擎服务器system的基类，system都要继承ServerSystem来调用相关函数
ServerSystem = serverApi.GetServerSystemCls()
# 获取组件工厂，用来创建组件
compFactory = serverApi.GetEngineCompFactory()


# 在modMain中注册的ServerSystem类
class TutorialServerSystem(ServerSystem):

    #ServerSystem的初始化函数
    def __init__(self, namespace, systemName):
        super(TutorialServerSystem,self).__init__(namespace, systemName)
        print ("================= TutorialClientSystem init ===============")
        ServerSystem.__init__(self, namespace, systemName)
        #初始化调用监听函数的监听事件
        self.ListenEvent()
    #监听函数，用于定义和监听函数
    def ListenEvent(self):
        print ("=================== ServerListenEvent ========================")
        #在自定义的ServerSystem中监听引擎的事件AddServerPlayerEvent，玩家加入游戏触发的事件
    #     self.ListenForEvent(serverApi.GetEngineNamespace(),serverApi.GetEngineSystemName(),"AddServerPlayerEvent",self,self.JoinGame)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
							self, self.OnServerChatEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
							self, self.OnAddServerPlayerEvent)
    
    ###
    def OnAddServerPlayerEvent(self, args):
		# 玩家进入世界时创建自定义生物
        print ("===================== 自定义生物 ====================")
        comp = compFactory.CreateGame(serverApi.GetLevelId())
        comp.AddTimer(3.0, self.createEntity, args['id'])
		
    ###
    def createEntity(self, playerId):
        comp = compFactory.CreatePos(playerId)
        pos = comp.GetPos()
        pos = (pos[0] + 1, pos[1], pos[2] + 1)
        comp = compFactory.CreateRot(playerId)
        rot = comp.GetRot()
        
        result = self.CreateEngineEntityByTypeStr("netease:jawgiant", pos, rot)
    ###
    def OnServerChatEvent(self, args):
        print ("==================== 打开聊天栏 ===================")
        if args['message'] == 'summon':
			# 测试创建自定义生物实体
            self.createEntity(args['playerId'])
        # else:
        #     print("====================================")
        # if args['message'] == 'move':
        #     print ("=======================move=============")
        #     self.queryIsMoving = 'query.mod.is_moving'
        #     comp = compFactory.CreateQueryVariable(serverApi.GetLevelId())
        #     result = comp.Reg(self.queryIsMoving, 1.0)
        # if args['message'] == 'stop':
        #     print ("=======================stop=============")
        #     self.queryIsMoving = 'query.mod.is_moving'
        #     comp = compFactory.CreateQueryVariable(serverApi.GetLevelId())
        #     result = comp.Register(self.queryIsMoving, 0.0)

    # def testNotifyClient(self):
    #     print ("===========NotifyToClient==========")
    #     player = {}
    #     player['uid'] = 123
    #     player['name'] = 'nickname'
    #     playerId = '456'
    #     self.NotifyToClient(playerId, "PlayerJoinOKEvent", player)
    
    # #玩家进入游戏，向客户端发送信息
    # def JoinGame(self, args):
    #     print ("========== hello world ==============")
    #     argsDict = self.CreateEventData()
    #     playerId = args["id"]
    #     argsDict["entityId"] = playerId
    #     self.NotifyToClient(playerId, "Function_1", argsDict)

        