# -*- encoding=utf8 -*-
__author__ = "chenjinli_01@163.com"

from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *
from demo.config import config

# 从配置文件读取 包地址
# debug包地址
PACKAGE_DEBUG = config.PACKAGE_DEBUG

# 正式包地址
# PACKAGE = "com.netease.cloudmusic"

PACKAGE = "com.netease.cloudmusic"
# APP启动activity
MAINACTIVITY = "com.netease.cloudmusic.module.login.LoginActivity"
# APP包安装地址
# INSTALL_PATH = "D:/test.apk"
auto_setup(__file__)


class Base(object):
    def __init__(self, poco, music_Test):
        self.music_Test = music_Test
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

        # 在设备上启动目标应用程序
        start_app(PACKAGE)

    def logout(self):
        """
        退出登录
        :return:
        """
        # 回到发现页
        self.music_Test.intoDiscover(config.discovery)
        sleep(5)
        # 进入账号设置
        self.poco("com.netease.cloudmusic:id/menu_icon").click()

        """
        assert_exists 断言存在
        assert_not_exists 断言不存在
        assert_equal 断言相等
        assert_not_equal 断言不相等
        """
        # 判断 nickname不为"立即登录"
        # nickname = self.poco("com.netease.cloudmusic:id/nickname").get_text()
        # # 判断是否有登录账号
        # if assert_equal(nickname, "立即登录", "text"):----os:不支持这样判断
        if self.poco(text="立即登录").exists():
            log("无登录账号")
            return

        for i in range(15):
            self.poco("com.netease.cloudmusic:id/accountRecyclerView").swipe('up')
            if self.poco(text="退出登录/关闭").exists():
                break
            sleep(1)  # 等待设备的响应

        # shell("am broadcast -a tv.douyu.mock.logout")
        print("退出登录")
        # r存在"退出登录/退出"按钮，则点击
        self.poco("com.netease.cloudmusic:id/logout").click()
        # 点击"退出云音乐登录"按钮
        self.poco(text="退出云音乐登录").click()
        # self.poco("com.netease.cloudmusic:id/bs_list_title").click()
        self.poco("com.netease.cloudmusic:id/buttonDefaultPositive").click()

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
        shell(" am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))
        self.poco.wait_for_any([self.poco("com.netease.cloudmusic:id/loadingAnimView")], timeout=60)
        log("进入路由： am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))
        print("进入路由： am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))

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
        adb shell am start -a android.intent.action.VIEW -d 'orpheus://nm/account/about'
        """
        shell("am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))
        log("进入路由：am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))
        print("进入路由：am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))
        sleep(5)

    # 进入某个activity(不带参数)
    def intoDiscover(self, euterpe):
        # shell("am start -n {}/{} --el control_toggle_panel_time 60000".format(PACKAGE, MAINACTIVITY))
        sleep(3)
        shell("am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))
        log("成功进入路由1：am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))
        print("成功进入路由2：am start -a android.intent.action.VIEW -d 'orpheus://{}'".format(euterpe))

    # 手机号登录
    def mobilelogin(self, phone, verificationCode):
        """
        explain:手机验证码登录
        author:libin09@corp.netease.com
        ⚠注意：包名的区别 com.netease.cloudmusic
        """
        listCode = list(verificationCode)

        sleep(2)

        # 用户条款和隐私政策提示弹窗是否出现
        if self.poco("android.view.ViewGroup").exists():
            self.poco("com.netease.cloudmusic:id/agree").click()

        # 系统弹窗 出现则关闭
        if self.poco("com.android.permissioncontroller:id/grant_dialog_container").exists():
            self.poco("com.android.permissioncontroller:id/permission_allow_button").click()

        # 推广图是否出现,出现则跳过
        if self.poco("ccom.netease.cloudmusic:id/skip").exists():
            self.poco("com.netease.cloudmusic:id/skip").click()

        # 勾选用户协议
        self.poco("com.netease.cloudmusic:id/agreeCheckbox").click()
        # 点击手机号登录按钮
        sleep(2)
        self.poco("com.netease.cloudmusic:id/login").click()
        # 系统弹窗是否出现,出现则关闭 android.view.ViewGroup
        if (self.poco("com.android.permissioncontroller:id/content_container").exists()):
            self.poco("com.netease.cloudmusic:id/positiveBtn").click()
        self.poco("com.netease.cloudmusic:id/cellphone").set_text(phone)
        self.poco("com.netease.cloudmusic:id/next").click()
        self.poco("com.netease.cloudmusic:id/captcha").click();
        # 使用键盘输入验证码
        for index in range(0, len(listCode)):
            keyevent('KEYCODE_{}'.format(str(listCode[index])))
        log("登录成功验证码为:{}".format(verificationCode))

    def pwdlogin(self, phone, pwd):
        """
        explain:账号&密码登录
        author:chenjinli_01@163.com
        """
        #
        # 系统弹窗是否出现,出现则跳过
        # ⚠注意：包名的区别 com.netease.cloudmusic
        if (self.poco("ccom.netease.cloudmusic:id/skip").exists()):
            self.poco("com.netease.cloudmusic:id/skip").click()
        # 等广告过去
        sleep(10)
        # 勾选用户协议
        self.poco("com.netease.cloudmusic:id/agreeCheckbox").click()
        # 点击手机号登录按钮
        sleep(2)
        self.poco("com.netease.cloudmusic:id/login").click()
        # 系统弹窗是否出现,出现则关闭 android.view.ViewGroup
        if (self.poco("com.android.permissioncontroller:id/content_container").exists()):
            self.poco("com.netease.cloudmusic:id/positiveBtn").click()
        self.poco("com.netease.cloudmusic:id/cellphone").set_text(phone)
        self.poco("com.netease.cloudmusic:id/next").click()
        # 点击密码登录按钮
        self.poco("com.netease.cloudmusic:id/passwordLoginBtn ").click()
        self.poco("com.netease.cloudmusic:id/password").set_text(pwd)
        # 点击登录
        self.poco("com.netease.cloudmusic:id/login").click()

    # 切换输入法，使用Airtest会默认使用yosemite输入法  可能会造成测试障碍
    def changeIME(self):
        ime_list = shell('ime list -s')
        for i in ime_list.splitlines():
            # for i in ime_list:
            if i.find("yosemite") == -1:
                shell("ime set {}".format(i))
                break

    # keyevent为键盘操作，keyevent为返回键
    """
    回车：input keyevent 66   // KEYCODE_ENTER  回车
    主页：input keyevent 3    //KEYCODE_HOME 主页
    返回：input keyevent 4    //KEYCODE_BACK  返回
    最近应用：input keyevent 187  //KEYCODE_APP_SWITCH  最近应用
    """

    # keyevent为键盘操作，keyevent为返回键
    def back(self):
        keyevent("4")

    # keyevent为键盘操作，keyevent为 ENTER  回车
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
