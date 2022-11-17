#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    :  2020/7/30 22:00
# Author  : LiBin（libin09@corp.netease.com）
# File    : ksongtestcase.py
# software: PyCharm
# time: 2020/7/30 22:00


import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from demo.config import config
from demo.common import ksong_Test, music_Test
from airtest.core.api import *
from airtest.core.android.adb import *

if __name__ == '__main__':
    # 正式包地址
    # PACKAGE = "com.netease.karaoke"

    # 从配置文件中读取包名
    PACKAGE = config.PACKAGE
    # debug包地址
    PACKAGE_DEBUG = config.PACKAGE_DEBUG
    # PACKAGE_DEBUG = "com.eg.android.AlipayGphone.AlipayLogin"


class appTestCase(unittest.TestCase):

    # 必须使用@classmethod 装饰器,  所有case运行之前只运行一次
    @classmethod
    def setUpClass(cls):
        # 初始化poco(UI控件实例化对象)
        cls.poco = AndroidUiautomationPoco(force_restart=False, screenshot_each_action=False)
        # 初始化通用工具类 (将poco传入该类进行实例化)---ksong音街
        #cls.ksong_Test = ksong_Test.Base(cls.poco)
        # TODO：初始化通用工具类 (将poco传入该类进行实例化)---music云音乐
        cls.music_Test = music_Test.Base(cls.poco, music_Test)
        if not os.path.exists(os.path.join(config.ROOT_DIR, 'result', config.DAY)):
            os.makedirs(os.path.join(config.ROOT_DIR, 'result', config.DAY))

    # 每条case执行前都会执行一次
    def setUp(self):
        log("初始化unittest成功")
        pass

    # 每条case执行后 都会执行一次
    def tearDown(self):
        log("用例执行完毕")

    # 所有用例执行完会执行一次
    @classmethod
    def tearDownClass(cls):
        # 关闭APP
        #stop_app(config.PACKAGE)
        # 清空手机数据
        try:
            clear_app(config.PACKAGE)
        except:
            # 卸载APP
            print("报错就卸载app")
            uninstall(PACKAGE)
        pass
