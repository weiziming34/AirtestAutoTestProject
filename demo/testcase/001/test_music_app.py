# -*- encoding=utf8 -*-
__author__ = "chenjinli_01@163.com"
"""
私人FM
"""
from airtest.core.api import *
from demo.common import appTestCase
from demo.config import config
import time

auto_setup(__file__)


class musicTest(appTestCase.appTestCase):

    # # 所有用例执行前会执行一次
    # @classmethod
    # def setUpClass(cls):
    # shell("am start -n com.netease.karaoke.debug/com.netease.karaoke.biz.launchscreen.ui.activity.LaunchActivity --el control_toggle_panel_time 60000")
    # log("登录APP")
    # 修改键盘
    # cls.music_Test.changeIME()
    # 登录操作
    # cls.music_Test.mobilelogin("14010000028", "555555")
    # time.sleep(5)

    # 每条case执行前都会执行一次
    def setUp(self):
        log("初始化APP成功")
        # shell("am start -n com.netease.karaoke.debug/com.netease.karaoke.biz.launchscreen.ui.activity.LaunchActivity --el control_toggle_panel_time 60000")

    # 进入排行榜页
    def test_1_intoPrivate_FM(self):
        """
        登录用户
        :return:
        """
        # 修改键盘
        self.music_Test.changeIME()
        # 登录操作
        self.music_Test.mobilelogin("14010000028", "555555")
        time.sleep(5)

        # 进入私人FM
        self.music_Test.intoDiscover(config.private_FM)

    def test_2_checkPrivate_FM(self):
        """
        私人FM页面，验证页面功能
        :return:
        """
        # self.poco.wait_for_any([
        #     self.poco("com.netease.karaoke:id/realContent"),
        # ], timeout=100)
        # self.poco.wait_for_any([
        #   self.poco("com.netease.karaoke.debug:id/next_btn")
        # ], timeout=360
        time.sleep(4)
        # 验证可进入私人FM

        if self.poco(text="私人FM").exists():
            log("成功进入私人FM")
            print("成功进入私人FM")
        time.sleep(2)
        # 点击歌曲的评论按钮
        self.poco("com.netease.cloudmusic:id/commentBtn").click()
        # 验证跳转进对应详情页
        time.sleep(2)
        self.poco(text="评论区").exists()
        print("私人FM页面存在-评论区")
        self.poco(text="推荐").exists()
        print("私人FM页面评论区存在-推荐tab")
        self.poco(text="最热").exists()
        print("私人FM页面评论区存在-最热tab")
        self.poco(text="最新").exists()
        print("私人FM页面评论区存在-最新tab" + "\n")

        # 测试评论功能
        if self.poco(text="发送").exists():
            print("存在评论条")
            self.poco(name="com.netease.cloudmusic:id/edit").set_text("真不错～")
            # 点击发送
            self.poco(text="发送").click()

        time.sleep(3)
        self.poco(text="真不错～").exists()
        print("发送评论成功")

        # 存在分享按钮
        self.poco(name="分享").exists()
        print("存在分享按钮")
        # 点击分享按钮
        self.poco(name="分享").click()
        # 存在分享浮层
        if self.poco(name="com.netease.cloudmusic:id/scrollView").exists():
            print("可正常打开分享浮层")
        # 存在分享项
        assert_equal(self.poco(text="微信朋友圈").get_text(), "微信朋友圈", "验证存在微信朋友圈")
        self.poco(text="微信好友").exists()
        self.poco(text="QQ空间").exists()
        self.poco(text="QQ好友").exists()

        # 可关闭分享浮层
        self.poco(name="com.netease.cloudmusic:id/closePageButton").click()

    # 所有用例执行完会执行一次 必须使用@classmethod 装饰器
    @classmethod
    def tearDownClass(cls):
        try:
            # 退出登录
            # cls.music_Test.logout()
            # 清空app缓存
            clear_app(config.PACKAGE)
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
        # 进入 设置 - 首页
        # cls.ksong_Test.intoDiscover(config.settingMain)
        # cls.poco.wait_for_any([cls.poco("com.netease.karaoke.debug:id/subText")],timeout=3)
        # #点击 清空缓存
        # cls.poco("com.netease.karaoke.debug:id/subText").click()
        # cls.poco("com.netease.karaoke.debug:id/buttonDefaultPositive").click()
