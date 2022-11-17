# -*- coding = utf-8 -*-
__author__ = "chenjinli_01@163.com"

"""
每日推荐
"""

from airtest.core.api import *
from demo.common import appTestCase
from demo.config import config
from demo.common import music_Test
import time

auto_setup(__file__)


class musicTest2(appTestCase.appTestCase):
    def setUp(self):
        log("初始化APP成功")

    def test_1_intoDailyRcmd(self):
        log("进每日推荐")
        # startMusic = "am start -n {}/{} --el control_toggle_panel_time 60000".format(config.PACKAGE,
        #                                                                              config.MAINACTIVITY)
        # shell(startMusic)
        #self.music_Test.mobilelogin("14010000028", "555555")
        #time.sleep(5)
        # shell("adb shell am start -a android.intent.action.VIEW -d 'orpheus://songrcmd'")
        # 进入每日推荐
        self.music_Test.intoDiscover(config.dailyRcmd)
        time.sleep(5)

    def test_2_checkDailyRcmd(self):
        print("开始校验-每日推荐页面")
        # 存在播放全部按钮
        assert_equal(self.poco(name="com.netease.cloudmusic:id/playAllTextView").get_text(), "播放全部", "验证存在播放全部按钮")
        # 存在日推评价
        # self.poco(text="日推评价").exists()---判断是否存在
        assert_equal(self.poco(name="android.widget.TextView").get_text(), "日推评价", "验证存在'日推评价'按钮")
        # 存在查看今日运势
        assert_equal(self.poco(name="com.netease.cloudmusic:id/tv_res_title").get_text(), "查看今日运势", "验证存在'查看今日运势'按钮")
        # 存在历史日推
        assert_equal(self.poco(name="com.netease.cloudmusic:id/tv_pendant_historyEntry").get_text(), "历史日推",
                     "验证存在'历史日推'按钮")
        self.poco(text="").click()
        # 存在歌曲信息
        if self.poco(name="com.netease.cloudmusic:id/songNameAndInfoArea").exists():
            print("存在推荐歌曲信息")
            # 存点击的歌曲的信息
            songinfo = self.poco(name="com.netease.cloudmusic:id/songName").get_text()
            # 点击歌曲信息
            self.poco(name="com.netease.cloudmusic:id/songNameAndInfoArea").click()
            time.sleep(5)
            # 进歌曲播放页
            if self.poco(name="com.netease.cloudmusic:id/custom_title").get_text() == songinfo:
                log("进对应播放页成功:{}".format(songinfo))
                print("进对应播放页成功:{}".format(songinfo))
                time.sleep(10)

    # 所有用例执行完会执行一次 必须使用@classmethod 装饰器
    @classmethod
    def tearDownClass(cls):
        try:
            # 清空app缓存
            #clear_app(config.PACKAGE)
            # stop app
            # stop_app(config.PACKAGE)

            log("清空缓存")
        except:
            # 卸载APP
            print("报错就卸载app")
            # uninstall(config.PACKAGE)
            # 清空app缓存
            # clear_app(config.PACKAGE)
        pass
