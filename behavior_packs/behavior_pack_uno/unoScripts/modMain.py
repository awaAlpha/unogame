# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi


@Mod.Binding(name="unoScripts", version="0.0.1")
class unoScripts(object):

    def __init__(self):
        print "\nunoMod\n"

    @Mod.InitServer()
    def unoScriptsServerInit(self):
        print "\nunoScriptsServerInit\n"
        serverApi.RegisterSystem("unoScripts", "unoServerSystem",
                                 "unoScripts.unoServerSystem.unoServerSystem")

    @Mod.DestroyServer()
    def unoScriptsServerDestroy(self):
        print "\nunoScriptsServerDestroy\n"

    @Mod.InitClient()
    def unoScriptsClientInit(self):
        print "\nunoScriptsClientInit\n"
        clientApi.RegisterSystem("unoScripts", "unoClientSystem",
                                 "unoScripts.unoClientSystem.unoClientSystem")

    @Mod.DestroyClient()
    def unoScriptsClientDestroy(self):
        print "\nunoScriptsClientDestroy\n"
