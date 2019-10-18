# coding:utf-8
import os,sys
import unittest
import time
sys.path.append("../page")
import HTMLTestRunner
sys.path.append("../../config")
import switch
sys.path.append("../common")
import z_data_default


# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
 
def add_case(rule="auto*.py"):
    """第一步：加载所有测试用例"""
    #case_path = os.path.join(cur_path,"src/case") # 用例文件夹 
    case_path = cur_path # 用例文件夹 
    # 定义discover加载所有测试用例
    # case_path：执行用例的目录；pattern：匹配脚本名称的规则；top_level_dir：默认为None
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    return discover
 
def run_case(all_case):
    """第二步：执行所有的用例，并把结果写入到html测试报告中"""
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,"../../report")
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    print("report path:%s"%report_abspath)
 
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="Teletraan接口自动化测试报告结果：",
                                           description="用例执行情况")
    if switch.time_switch == '1':
        k=1
        while k<2:
            timing=time.strftime('%H_%M',time.localtime(time.time()))
            if timing == switch.timing_ex:
                print u"开始运行脚本:"
                runner.run(all_case)
                print u"运行完成，退出"
                break
            else:
                time.sleep(5)
                print timing
    else:
        runner.run(all_case)
    fp.close()
 
 
 
if __name__ == '__main__':
 
    #data_default.init_data() # 初始化接口测试数据
 
    all_case = add_case() # 加载用例
    run_case(all_case)  # 执行用例输出报告





