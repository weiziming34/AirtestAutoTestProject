# -*- encoding=utf8 -*-
# # Time    :  2020/7/30 22:00
# # Author  : jinLi（chenjinli_01@163.com）
# # File    : test_music_app.py
# # software: PyCharm
# # time: 2020/7/30 22:00
# TODO：在这里执行！！！！！！！！！！

# 使用Airtest + unittest搭建自动化测试框架，抽象常用的路由地址 ,通过config配置化进行使用


import common.HTMLTestRunner
import sys
import unittest

from airtest.core.api import *

# 测试报告存放在result目录下
result = os.path.join(os.path.dirname(__file__), "result/")
# 指定一个testcase文件夹下的case进行执行
casepath = os.path.join(os.path.dirname(__file__), "testcase/music/")


def case_list(casepath):
    # 定义单元测试容器
    suite = unittest.TestSuite()
    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(casepath, pattern='test_*.py', top_level_dir=None)
    # 将discover方法筛选出来的用例，循环添加到测试套件中,打印出的用例信息会递增
    suite.addTests(discover)
    return suite


def CreatSuitePath(testpath, testpaths):
    # 定义单元测试容器
    suite = unittest.TestSuite()
    # 把test_的文件检索出来，写入文件中，分发到执行机
    for caseName in testpaths:
        suite.addTests(unittest.TestLoader().discover(testpath, pattern=caseName,
                                                      top_level_dir=os.path.join(os.path.dirname(__file__))))
    return suite


def CreatSuite(pathlist):
    # 定义单元测试容器
    suite = unittest.TestSuite()
    for i in pathlist:
        suite.addTest(unittest.TestLoader().loadTestsFromName(i))
    return suite


def getTestCaselocal(casepath):
    result = []
    with open(casepath, "r") as f:
        for line in f:
            result.append(line.strip('\n'))
    return result


if __name__ == "__main__":
    # 所有的用例集合
    # 如果有传参，把传参作为报告的命名，如果无，默认把时间戳作为文件名
    if len(sys.argv) > 3:
        job_name = sys.argv[1]
        # testsuit = getTestCaselocal(sys.argv[2])
        connect_device("Android:///{}?cap_method=javacap&touch_method=adb".format(sys.argv[3]))
        set_current(sys.argv[3])
        if len(sys.argv) == 5:
            linename = os.path.join(os.path.dirname(__file__), "testcase/{}/".format(sys.argv[4]))
            all_test_cases = CreatSuitePath(linename, getTestCaselocal(sys.argv[2]))
        else:
            all_test_cases = CreatSuite(getTestCaselocal(sys.argv[2]))
    else:
        job_name = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        # connect_device("Android:///{}?cap_method=javacap&touch_method=adb".format("CUY0219613010913"))
        all_test_cases = case_list(casepath)
    print(all_test_cases.countTestCases())
    # 获取系统当前时间

    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 定义单个测试报告的存放路径，支持相对路径
    tdresult = result + day
    # 创建文件夹
    if not os.path.exists(tdresult):
        os.makedirs(tdresult)
    filename = tdresult + "//" + job_name + "_result.html"
    # 以写文本文件或写二进制文件的模式打开测试报告文件
    fp = open(filename, mode='wb')
    # 先创建短报告文件
    shortpath = open(tdresult + "//" + "short_report_" + job_name + ".txt", "w")
    shortpath.close()
    # 定义测试报告
    runner = common.HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'UI自动化测试报告', description=u'用例执行情况如下：',
                                                  shortreport="short_report_" + job_name, retry=1, save_last_try=True)
    # 运行测试用例
    runner.run(all_test_cases)
    # 关闭报告文件
    fp.close()
