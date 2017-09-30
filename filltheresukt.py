#!/usr/bin/env python
# coding=utf-8


from selenium import webdriver
import time
import achdata
import date_selenium

driver = webdriver.Firefox()
driver.get("http://ach.efoxconn.com:8080/Index/Index")


driver.find_element_by_id("loguserid").send_keys("F3233692")

driver.find_element_by_id("password").send_keys("F3233692")


driver.find_element_by_id("login-btn").click()
time.sleep(1)
listOfType = ["tr_0", "tr_1", "tr_2"]
nu = date_selenium.getWeekNum()


if driver.find_element_by_xpath('//*[@id="weekplanlist"]/table/tbody/tr[2]/td[2]').text == u'執行成果':
    driver.find_element_by_xpath(
        '//*[@id="weekplanlist"]/table/tbody/tr[2]/td[1]').click()

    time.sleep(1)
    driver.switch_to_window(driver.window_handles[1])
    
    for tr in listOfType:
        driver.find_element_by_xpath("//*[@id='%s']/td[7]" % tr).click()
        driver.find_element_by_xpath(
            '//*[@id="ui-datepicker-div"]/table/tbody/tr[%d]/td[6]' % int(nu)).click()
        time.sleep(0.5)

        num = achdata.getID(driver.find_element_by_xpath(
            "//*[@id='%s']/td[3]/textarea" % tr).text)
        txt = achdata.getResultFromDB('results', int(num[0]))
        driver.find_element_by_xpath(
            "//*[@id='%s']/td[8]/textarea" % tr).send_keys(txt)


driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
#driver.find_element_by_xpath(
#    "/html/body/center/div[1]/div/div[2]/div/div[3]/div[3]/div/input[2]").click()
driver.find_element_by_xpath(
    '//*[@id="excdraft_unch"]').click()
driver.quit()
