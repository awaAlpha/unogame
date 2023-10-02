# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
compFactory = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()


class unoServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        print "\nunoServerSystem\n"
        self.ListenEvents()

    def ListenEvents(self):
        # 监听事件
        print "==== ListenEvents ===="
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self,
                            self.OnServerChat)  # 监听玩家发送提问用词
        self.ListenForEvent("unoScript", "unoClientSystem", "PlayersListIndex",  self, self.OnBC1)
        self.ListenForEvent("unoScript", "unoClientSystem", "GAME", self, self.OnBC2)

    def OnServerChat(self, args):
        print "==== OnServerChat ==== ", args
        playerId = args["playerId"]
        if args["message"] == "关于":
            args["cancel"] = True
            about = '\n关于：\n\n地图名：Minecraft UNO\n地图版本：1.0\n制作团队：北源TEAM\n团队制作人：阿尔法、一云秋水\n非团队制作人：幼稚羱羊、金苹果闯世界i、小沙馒包\n\n逻辑制作语言：Python 2.7.18\n含有的软件包：math、mc-netease-sdk\n\n如果你喜欢本地图请给一个五星好评！\n请去资源中心给 北源_阿尔法 一个订阅awa！'
            comp = serverApi.GetEngineCompFactory().CreateMsg(playerId)
            comp.NotifyOneMessage(playerId, about)
        elif args["message"] == "简介":
            args["cancel"] = True
            introduction1 = '\n简介：\n\n你知道UNO吗？\n\nUNO是一款广受欢迎的桌游，由美国的Merle Robbins于1971年发明。它被设计成简单易懂、快节奏和充满乐趣。\n\n游戏目标是尽快将手中的牌打完，第一个把所有牌都出完的玩家获得游戏的胜利。'
            introduction2 = '\nUNO适合各个年龄段的玩家，不仅在家庭聚会中受欢迎，也常常作为社交活动或派对游戏。它的简单规则、快节奏和戏剧性的转折使得游戏过程充满乐趣和紧张感。\n\n无论您是游戏新手还是老手，UNO都是一款容易上手、令人愉快的游戏，可以与家人、朋友或任何人一起享受无尽的娱乐时光。'
            introduction3 = '\n那么这个风靡全球50几年的桌游与旷世神作Minecraft摩擦会迸发出怎样的火花呢？就在这张地图当中！\n\n值得一提的是，“UNO”是西班牙语“一”的意思，读作“w∪ no”，而不是“you no”哦！不要被劣质的西翻英翻中读音带跑偏哦！'
            comp = serverApi.GetEngineCompFactory().CreateMsg(playerId)
            comp.NotifyOneMessage(playerId, introduction1)
            comp.NotifyOneMessage(playerId, introduction2)
            comp.NotifyOneMessage(playerId, introduction3)
        elif args["message"] == "规则":
            args["cancel"] = True
            rules1 = '\n规则：\n\n1. 开始游戏：\n- 第一个玩家是持有红色数字1的人（若没有则选有最低点数的红色牌）。\n- 顺时针轮流玩家，每位玩家可以选择出一张与桌上牌颜色或数字相同的牌。出牌后，将牌放在起始牌的上方。\n\n2. 牌的规则：\n- 数字牌：可以与桌上的颜色或数字相同的牌相连出。'
            rules2 = '- 功能牌：\n  与数字牌类似，可以与桌上的颜色相同的牌相连出，但有特殊功能，具体分为：\n  - 跳过牌（Skip Card）：\n    打出此牌后，下一个玩家被跳过，不准出牌。\n  - 反转牌（Reverse Card）：\n    改变当前出牌的方向（顺时针变为逆时针，逆时针变为顺时针）。'
            rules3 = '  - +2牌（Draw Two Card）：\n    打出此牌后，下一个玩家必须罚2张牌，被罚牌玩家一般情况不准出牌。\n  - 任意牌（Wild Card）：\n    可与任何颜色的牌相连出并改变当前游戏颜色。\n  - 任意+4牌（Wild Draw Four Card）：'
            rules4 = '    打出此牌后，改变当前游戏颜色，并且下一个玩家必须罚4张牌，被罚牌玩家一般情况不准出牌。\n- 特殊玩法：\n  - 叠加：\n    在叠加规则中，如果有连续出现的功能牌，玩家可以选择叠加出牌，以增加下一个玩家的惩罚。'
            rules5 = '    例如，如果一位玩家出了一个“+2”牌，下一个玩家可以选择出另一个“+2”牌，使得下一个玩家需摸4张牌。如果下一个玩家也有“+2”牌，该玩家也可以叠加出牌，使得惩罚进一步增加。\n    “任意+4”牌可以在改变颜色并罚下一个玩家4张牌的同时被下一张“任意+4”牌改变颜色并叠加，但是“+2”牌不可以叠加“任意+4”牌。'
            rules6 = '  - 质疑：\n    在质疑规则中，玩家可以质疑其他玩家出的“任意+4”牌是否合规。若被质疑的牌符合规则，则质疑的玩家受到惩罚。否则，出牌有问题的玩家受到惩罚。\n    具体而言，假设当前游戏限制颜色是红色，如果一个玩家打出一张“任意+4”牌，并且下一个玩家认为该玩家仍有红色的牌可出，下一个玩家可以选择提出质疑。'
            rules7 = '    ①如果被质疑的玩家确实有红色牌故意不出，则质疑成功，撤销罚牌下一个玩家，并罚被质疑的玩家6张牌。\n    ②如果被质疑的玩家确实没红色牌可以打出，则质疑失败，罚提出质疑的玩家6张牌。\n    没有把握请不要质疑哦！毕竟被罚4张总比被罚6张好！'
            rules8 = '- 当出牌无法匹配时，玩家必须从牌堆上摸一张牌，若所摸的牌能够出，则立即出牌。\n- 若牌堆上的牌摸完，将已经出过的牌除最后一张外都收回，重新洗牌作为新的牌堆。\n\n4. UNO和胜利：'
            rules9 = '- 当玩家在打出倒数第二张牌之前，必须喊出“UNO”（按下“UNO”按钮）。如果其他玩家在他喊UNO之前抓到该玩家，则该玩家必须摸两张牌作为惩罚。\n- 当一名玩家打出最后一张手牌后，该玩家赢得游戏。他将得到此轮出牌的所有玩家手中的牌的点数之和作为得分并转换为金币（其他玩家手中的牌越多，得分越高）。'
            comp = serverApi.GetEngineCompFactory().CreateMsg(playerId)
            comp.NotifyOneMessage(playerId, rules1)
            comp.NotifyOneMessage(playerId, rules2)
            comp.NotifyOneMessage(playerId, rules3)
            comp.NotifyOneMessage(playerId, rules4)
            comp.NotifyOneMessage(playerId, rules5)
            comp.NotifyOneMessage(playerId, rules6)
            comp.NotifyOneMessage(playerId, rules7)
            comp.NotifyOneMessage(playerId, rules8)
            comp.NotifyOneMessage(playerId, rules9)
        elif args["message"] == "反馈":
            args["cancel"] = True
            feedback = '\n反馈：\n\n嗨！这里是法法（阿尔法）~你有问题想反馈吗？请尝试以下邮箱哦！\n\nalpha5dev@163.com\n\n法法会尽快处理的哈！'
            comp = serverApi.GetEngineCompFactory().CreateMsg(playerId)
            comp.NotifyOneMessage(playerId, feedback)

    R1 = (-4.00, 69.50, -1.50)
    R2 = (-4.00, 69.50, 2.50)
    G1 = (-1.50, 69.50, 5.00)
    G2 = (2.50, 69.50, 5.00)
    B1 = (5.00, 69.50, 2.50)
    B2 = (5.00, 69.50, -1.50)
    Y1 = (2.50, 69.50, -4.00)
    Y2 = (-1.50, 69.50, -4.00)
    def OnBC1(self, pld):
        pl = pld["Data"]
        global pl

    p1 = pl[0]
    p2 = pl[1]
    p3 = pl[2]
    p4 = pl[3]
    p5 = pl[4]
    p6 = pl[5]
    p7 = pl[6]
    p8 = pl[7]
    p9 = pl[8]
    p10 = pl[9]

    def OnBC2(self, pmd):
        pm = pmd["moshi"]
        global pm


    def TpCmd(self, target, (x, y, z)):
        comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
        comp.SetCommand("/tp {} {} {} {}".format(target, x, y, z))
    def SeatSave(self):
        print '==== SeatSave ===='
        if pm == 'classic':
             self.TpCmd((pl[0](-4.00, 69.50, -1.50)),(pl[1](-1.50, 69.50, 5.00)),(pl[2](5.00, 69.50, 2.50)),(pl[3](2.50, 69.50, -4.00)))
        elif pm == 'threemode':
             self.TpCmd((pl[0](-4.00, 69.50, -1.50)),(pl[1](-1.50, 69.50, 5.00)),(pl[2](5.00, 69.50, 2.50)))
        elif pm == 'waiting':
            self.TpCmd((pl[0](-4.00, 69.50, -1.50)), (pl[1](-1.50, 69.50, 5.00)))
        elif pm == 'multi':
            self.TpCmd((pl[0](-4.00, 69.50, -1.50)), (pl[1](-1.50, 69.50, 5.00)), (pl[2](5.00, 69.50, 2.50)),
                       (pl[3](2.50, 69.50, -4.00)), (pl[4](-4.00, 69.50, 2.50)), (pl[5](2.50, 69.50, 5.00)), (pl[6](5.00, 69.50, -1.50)), (pl[7](-1.50, 69.50, -4.00))






