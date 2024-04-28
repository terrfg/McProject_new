# 从客户端API中拿到ViewBinder / ViewRequest / ScreenNode
import mod.client.extraClientApi as clientApi

####
import threading
import time
# 配置
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
CompFactory = clientApi.GetEngineCompFactory()
#获取客户端引擎API模块

# 共享的变量

# 检查值变化的函数
# def check_value():
#     global value
#     while True:
#         with value_lock:
#             print(value)
#         time.sleep(1)  # 每秒检查一次
value = 2.0
class ViewUI(ScreenNode):
    def __init__(self, namespace, name,param):
        ScreenNode.__init__(self, namespace, name, param)
    #   
###########################################################
    # # 检查值变化的函数
    def check_value(self):
        
        while True:
                print(value)
                time.sleep(1)  # 每秒检查一次
############################################################
    # def monitor(self):
    #     while True:
    #         print("======拖动条的值是否发生变化======")
    #         if(self.sliderUIControl_2.GetSliderValue()!=self.offset_slider):
    #             print("发生了变化")
    #             print(self.sliderUIControl_2.GetSliderValue())
    #         time.sleep(1)
    # def change_value(self):
    #     global value
    #     while True:
    #         value = self.sliderUIControl_2.GetSliderValue()
    #         time.sleep(1)
###############################################################
    def Create(self):
        print("===================Create=================")
        self.uiNode = clientApi.GetUI("TutorialMod","View")
        global value
        #控制特定对象的节点
        self.buttonControl = self.uiNode.GetBaseUIControl("/panel/button1").asButton()
        self.buttonControl2 = self.uiNode.GetBaseUIControl("/panel/button2").asButton()
        self.sliderUIControl_1 = self.uiNode.GetBaseUIControl("/panel/slider1").asSlider()
        self.sliderUIControl_2 = self.uiNode.GetBaseUIControl("/panel1/slider1").asSlider()
        self.buttonUIControl_1 = self.uiNode.GetBaseUIControl("/panel1/button1").asButton()
        # 使用这个方法设置按钮的回调函数
        self.buttonControl.AddTouchEventParams({"isSwallow":True})
        self.buttonControl.SetButtonTouchUpCallback(self.onButtonPress)
        self.buttonControl2.AddTouchEventParams({"isSwallow":True})
        self.buttonControl2.SetButtonTouchUpCallback(self.onButtonPress2)
        
        ##########################################################
        self.sliderUIControl_2.SetTouchEnable(True)
        self.buttonUIControl_1.AddTouchEventParams({"isSwallow":True})
        self.buttonUIControl_1.SetButtonTouchUpCallback(self.SliderPress)
        value = self.sliderUIControl_2.GetSliderValue()
        self.offset_slider = self.sliderUIControl_2.GetSliderValue()
        # self.check_thread = threading.Thread(target=self.check_value)
        # self.check_thread.start()
        ###################################################
        self.sliderUIControl_1.SetTouchEnable(True)
        self.offset = 5
        
    def onButtonPress(self, args):
        print("================OnButtonPress1==============")
        self.slider_offset = self.sliderUIControl_1.GetSliderValue()
        print(self.slider_offset)
        levelId = clientApi.GetLevelId()
        comp = CompFactory.CreateCamera(levelId)
        comp.SetCameraOffset((0,0,self.offset+self.slider_offset))
        # if(self.offset<=15):
        #     self.offset+=1
        #     print(self.offset)
        #     levelId = clientApi.GetLevelId()
        #     comp = CompFactory.CreateCamera(levelId)
        #     comp.SetCameraOffset((0,0,self.offset))
    
    def onButtonPress2(self, *args):
        print("=================onButtonPress2====================")
        if(self.offset>5):
            self.offset-=1
            print(self.offset)
            levelId = clientApi.GetLevelId()
            comp = CompFactory.CreateCamera(levelId)
            comp.SetCameraOffset((0,0,self.offset))
            
    
    def SliderPress(self, args):
        print("=================SliderPress=======================")
        global value
        value = self.sliderUIControl_2.GetSliderValue()*10
        self.slider_offset = self.sliderUIControl_2.GetSliderValue()
        print(self.slider_offset)
        levelId = clientApi.GetLevelId()
        comp = CompFactory.CreateCamera(levelId)
        comp.SetCameraOffset((0,0,self.offset+self.slider_offset*10))
