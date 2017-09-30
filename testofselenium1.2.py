#!/usr/bin/env python
# coding=utf-8


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

import achdata
import date_selenium

# from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://ach.efoxconn.com:8080/Index/Index")
# assert "Python" in driver.title

driver.find_element_by_id("loguserid").send_keys("F3233692")

driver.find_element_by_id("password").send_keys("F3233692")


driver.find_element_by_id("login-btn").click()
# click之后登录账号,页面发生跳转,但是没有新标签或新窗口产生,所以无需进行窗口跳转
# 加等待是为了等新页面加载完成
time.sleep(1)
# sreach_window = driver.current_window_handle


try:
    driver.find_element_by_xpath(
        '//*[@id="weekplanlist"]/table/tbody/tr[2]/td[1]').click()
    # 使用'//*[@id="3253727C-CCCF-4CA8-9591-4A3C1D469222"]' 也能定为到该元素,但是通过上面的方法可以定位四条中的任意一条
    # 而无需事先知道该链接的id
except NoSuchElementException as e:
    print e
time.sleep(1.5)
driver.switch_to_window(driver.window_handles[1])


listOfType = ["tr_0", "tr_1", "tr_2"]
listOfline = [2, 3, 5]
num = date_selenium.getWeekNum()
#当天是本月第几周
m = date_selenium.totaldaysofmonth - date_selenium.currentDay - 7
#
for tr in listOfType:
    s = achdata.getResultFromDB('project')
    try:
        driver.find_element_by_xpath("//*[@id='%s']/td[4]" % tr).click()
        # 本程序设计的逻辑只在考虑了星期五运行的情况,所以其他情况下不保证能正常运行
        # 当本周五与本月最后一天的时间差不小于7天,正常填写日期
        if m >= 0:
            driver.find_element_by_xpath(
                '//*[@id="ui-datepicker-div"]/table/tbody/tr[%d]/td[6]' % int(num+1)).click()
        else:
            # 否则,翻到下月
            driver.find_element_by_xpath(
                '//*[@id="ui-datepicker-div"]/div/a[2]').click()
            if date_selenium.weekdayoflast != 4:
                # 最后一天不是周五,则取下月第一周的周五

                driver.find_element_by_xpath(
                    '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[6]').click()
            else:
                # 最后一天是周五,则取下月第二周
                driver.find_element_by_xpath(
                    '//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]').click()
        time.sleep(0.5)
        # 上面弹出的日历会遮盖着下面的日期栏,导致下面的日期无法自动填充.睡下就好
        for line, cont in zip(listOfline, s):
            driver.find_element_by_xpath(
                "//*[@id='%s']/td[%d]/textarea" % (tr, line)).send_keys(cont)
    except NoSuchElementException as e:
        print e
time.sleep(2)
driver.find_element_by_xpath("/html/body/center/div[1]/div/div[2]/div/div[3]/div[3]/div/input[2]").click()
driver.quit()
