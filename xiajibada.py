s = "asdfag"
o = {}
for i in s:
    o[i]=s.count(i)
print(o)








# from airtest.core.api import *
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# auto_setup(__file__)
#
# connect_device("Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP&&ori_method=ADBORI")
# sleep(5)
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# poco("com.mumu.launcher:id/workspace").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.TextView")[2].click()

