from httprunner import HttpRunner
kwargs = {'failfast': False, 'report_dir': 'E:\\demo\\test'} # 看api.py中__init__方法参数
runner = HttpRunner(**kwargs)
result_runner = runner.run('E:\\autotest\\api_autotest\\testcases\\test_demo.yml') # 执行指定目录下用例
print(result_runner) # 输出报告地址
summary = runner.summary # 获取执行结果，需要在run方法后
print(summary)