# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
levelId = clientApi.GetLevelId()


class unoClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        print "\nunoClientSystem\n"
        self.ListenEvents()

    def ListenEvents(self):
        print "==== ListenEvents ===="
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self,
                            self.OnUiInitFinished)  # 监听玩家进入游戏成功（UI法）
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnScriptTickClient", self,
                            self.OnTickClient())

    def OnUiInitFinished(self, args):
        print '==== OnUiInitFinished ===='
        levelId = clientApi.GetLevelId()
        args["levelId"] = levelId
        comp = clientApi.GetEngineCompFactory().CreateTextNotifyClient(levelId)
        comp.SetLeftCornerNotify("§c欢迎来到Minecraft UNO！您可以通过在聊天栏发送【关于】、【简介】、【规则】、【反馈】来了解本地图")

    def OnTickClient(self):
        print '==== OnTickClient ===='
        N = str(len(clientApi.GetPlayerList()))
        comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
        comp.SetTipMessage("在线人数：{}".format(N)