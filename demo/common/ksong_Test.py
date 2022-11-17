# -*- encoding=utf8 -*-
__author__ = "libin"

from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *

# debug包地址
# PACKAGE_DEBUG = "com.eg.android.AlipayGphone"
# debug包地址
PACKAGE_DEBUG = "com.netease.karaoke.debug"


# 正式包地址
#PACKAGE = "com.netease.karaoke"

PACKAGE = PACKAGE_DEBUG
# APP启动activity
MAINACTIVITY = "com.netease.karaoke.debug.login.LoginActivity"
# APP包安装地址
# INSTALL_PATH = "D:/test.apk"
auto_setup(__file__)


class Base(object):
    def __init__(self, poco):
        self.poco = poco
        # 实例化安卓对象
        self.android = Android(serialno=self.poco.device.uuid)
        try:
            self.android.check_app(PACKAGE)
        except AirtestError:
            start_app(PACKAGE)
            # 安装应用，是否同意覆盖安装，默认否
            # self.android.install_app(INSTALL_PATH, False)
            # 覆盖安装
            # android.install_app(INSTALL_PATH,True)
        start_app(PACKAGE)

    # def logout(self):
    #     #shell("am broadcast -a tv.douyu.mock.logout")
    #     print("退出登录")

    # 进入某个activity(带两个参数)
    def intoActivityWithTwo(self, euterpe, value1, value2):
        '''
        :param euterpe: 路由地址
        :param value1: 路由动态参数
        :param value2: 路由动态参数
        :return:
        '''
        shell("am start -n {}/{} --el control_toggle_panel_time 60000".format(PACKAGE, MAINACTIVITY))
        sleep(3)
        euterpe = euterpe.format(value1, value2)
        shell(" am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))
        self.poco.wait_for_any([self.poco("com.netease.karaoke.debug:id/loadingAnimView")], timeout=60)
        log("进入路由： am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))
        print("进入路由： am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))

    # 进入某个activity(带一个参数)
    def intoActivityWithOne(self, euterpe, value):
        '''
        :param euterpe:
        :param value:
        :return:
        '''
        # 先返回APP首页
        shell("am start -n {}/{} --el control_toggle_panel_time 60000".format(PACKAGE, MAINACTIVITY))
        sleep(3)
        euterpe = euterpe.format(value)
        """adb shell命令进路由：
        #TODO：可终端测试是否正常跳转
        adb shell am start -a android.intent.action.VIEW -d 'euterpe://nk/accompaniment/detail?accompanyId=5DC14367928EEDA517D0EE41CD6E38E5'
        """
        shell("am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))
        log("进入路由：am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))
        print("进入路由：am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))
        sleep(5)


    # 进入某个activity(不带参数)
    def intoDiscover(self, euterpe):
        shell("am start -n {}/{} --el control_toggle_panel_time 60000".format(PACKAGE, MAINACTIVITY))
        sleep(3)
        shell("am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))
        log("进入路由：am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))
        print("进入路由：am start -a android.intent.action.VIEW -d 'euterpe://{}'".format(euterpe))

    # 手机号登录
    def mobilelogin(self, phone, verificationCode):
        """
        explain:手机验证码登录
        author:libin09@corp.netease.com
        """
        listCode = list(verificationCode)
        # remix动效是否出现,出现则跳过
        sleep(2)

        #⚠注意：包名的区别 com.netease.karaoke.debug
        if (self.poco("com.netease.karaoke.debug:id/skip").exists()):
            self.poco("com.netease.karaoke.debug:id/skip").click()
        #勾选用户协议


        self.poco("com.netease.karaoke.debug:id/agreeCheck").click()
        #点击手机号登录按钮
        sleep(2)
        self.poco("com.netease.karaoke.debug:id/phoneLogin").click()
        # 系统弹窗是否出现,出现则关闭
        if (self.poco("com.android.permissioncontroller:id/content_container").exists()):
            self.poco("com.android.permissioncontroller:id/permission_allow_button").click()
        self.poco("com.netease.karaoke.debug:id/numText").set_text(phone)
        self.poco("com.netease.karaoke.debug:id/nextBtn").click()
        self.poco("com.netease.karaoke.debug:id/captcha").click();
        #使用键盘输入验证码
        for index in range(0, len(listCode)):
            keyevent('KEYCODE_{}'.format(str(listCode[index])))
        log("登录成功验证码为:{}".format(verificationCode))

    # 切换输入法，使用Airtest会默认使用yosemite输入法  可能会造成测试障碍
    def changeIME(self):
        ime_list = shell('ime list -s')
        for i in ime_list.splitlines():
            # for i in ime_list:
            if i.find("yosemite") == -1:
                shell("ime set {}".format(i))
                break

    # keyevent为键盘操作，keyevent为返回键
    def back(self):
        keyevent("4")

    # keyevent为键盘操作，keyevent为进入键
    def enter(self):
        keyevent("66")

    # 回到主页
    def backToHome(self):
        shell("am start -n {}/{} -W".format(PACKAGE, MAINACTIVITY))
        sleep(3)

    # 打印logcat日志
    def logcat(self, grep):
        """
        Perform `logcat`operations
        Args:
            *args: optional arguments
            **kwargs: optional arguments
        Returns:
            `logcat` output
        """
        logmsg = self.android.logcat(grep_str=grep, extra_args="-d", read_timeout=10)
        for i in logmsg:
            if i:
                return True
                break
            else:
                return False
