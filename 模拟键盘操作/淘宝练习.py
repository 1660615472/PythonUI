from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
#设置页面最大化
driver.maximize_window()
#设置全局隐式等待
driver.implicitly_wait(10)

driver.find_element_by_css_selector("#kw").send_keys("天猫")
driver.find_element_by_css_selector("#su").click()
sleep(3)
driver.find_element_by_partial_link_text("tmall").click()
sleep(4)
#跳转到新页面做句柄判断
#获取当前窗口句柄
current_window_handle = driver.current_window_handle
#获取所有句柄
all_handles = driver.window_handles
for handle in all_handles:
    if handle != current_window_handle:
        # 执行切换窗口语句
        driver.switch_to.window(handle)

        driver.find_element_by_partial_link_text("请登录").click()
        sleep(2)
        # 切换到J_loginIframe表单
        driver.switch_to.frame("J_loginIframe")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[4]/div/div[5]/a[1]").click()
        driver.find_element_by_css_selector("#TPL_username_1").send_keys("长叼欧巴")
        driver.find_element_by_css_selector("#TPL_password_1").send_keys("zhangjie7040300/")
        # #拖动滑块
        # button = driver.find_element_by_css_selector("#nc_1_n1z")
        # #实例化鼠标操作对象
        # action = ActionChains(driver)
        # # perform()用来执行ActionChains中存储的行为
        # action.click_and_hold(button).perform()
        # # 清空所有准备好的Action
        # action.reset_actions()
        # #移动滑块,模拟拖动
        # action.move_by_offset(258,0).perform()
        # #构造移动轨迹
        # def get_track(distance):
        #
        #     track = []
        #
        #     current = 0
        #
        #     mid = distance * 3 / 4
        #
        #     t = 0.2
        #
        #     v = 0
        #
        #     while current < distance:
        #
        #         if current < mid:
        #
        #             a = 2
        #
        #         else:
        #
        #             a = -3
        #
        #         v0 = v
        #
        #         v = v0 + a * t
        #
        #         move = v0 * t + 1 / 2 * a * t * t
        #
        #         current += move
        #
        #         track.append(round(move))
        #
        #         return track
        # driver.find_element_by_css_selector("#J_SubmitStatic").click()
        # sleep(3)
        # driver.find_element_by_partial_link_text("首页").click()
        # sleep(3)
        # driver.find_element_by_css_selector("#J_SiteNavHome > div:nth-child(1) > a:nth-child(1)").click()


