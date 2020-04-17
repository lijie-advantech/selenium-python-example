import logging

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def test():

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://portal-ensaas.bm.wise-paas.com.cn/")
    driver.maximize_window()

    driver.find_element_by_id("username").send_keys("li.jie@advantech.com.cn")
    driver.find_element_by_id("password").send_keys("123456Lj/")
    driver.find_element_by_xpath("//div[@id='ant-dropdown']/div[@class='login-wrapper']//button[@type='button']").click()

    meun = driver.find_element_by_xpath("//div[@id='root']/div[@class='App blue']/section[@class='ant-layout']//div[@class='ant-row ant-row-middle']/div[1]/button[@type='button']")
    meun.click()

    plat = driver.find_element_by_xpath("//div[@id='root']//section[@class='ant-layout']//ul[@role='menu']/li[1]/div[@role='button']")
    plat.click()

    sc = driver.find_element_by_xpath("//ul[@id='Platform Management$Menu']//div[@role='button']")
    sc.click()

    ns = driver.find_element_by_link_text("Namespaces")
    ns.click()
    #ActionChains(driver).move_by_offset(1000, 1000)




    #找到下拉框元素
    clBtn = driver.find_element_by_xpath(
        "//div[@id='root']/div[@class='App blue']/section[@class='ant-layout']/main/div[@class='ant-row pr-20']/div[2]/div[@class='ant-col ant-col-sm-24']/div[2]/div[@class='ant-col ant-col-sm-24']/div[@class='ant-row']/div[1]/div[@class='ant-row']/div")
    #点击下拉框元素
    clBtn.click()
    #获取下拉框列表
    clList = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div/div[@class='']/div/div[@class='']/div")
    #遍历下拉框列表
    for cl in clList:
        #每次点击下拉框列表里面一个元素之前，要先点击下拉框元素，让下拉列表出现
        clBtn.click()
        #点击下拉框列表中的某一个元素（为什么使用这种方式进行点击，请查看*****）
        driver.execute_script("(arguments[0]).click()", cl)
        #cl.click()

        #下面的代码是需要循环遍历另一个下拉框，代码类似
        wsBtn = driver.find_element_by_xpath(
            "//div[@id='root']/div[@class='App blue']/section[@class='ant-layout']/main/div[@class='ant-row pr-20']/div[2]/div[@class='ant-col ant-col-sm-24']/div[2]/div[@class='ant-col ant-col-sm-24']/div[@class='ant-row']/div[2]/div[@class='ant-row']/div")
        wsBtn.click()
        list = driver.find_elements_by_xpath('//div[@role="listbox"]')
        wsList = list[len(list) - 1].find_elements_by_xpath('../div[2]/div/div/div')
        print("wslist len is ", len(wsList))
        for ws in wsList:
            wsBtn.click()
            driver.execute_script("arguments[0].click();", ws)
            #ws.click()
            time.sleep(2)
    driver.quit()

    '''
        
    '''
'''
    clBtn = driver.find_element_by_xpath('//*[@id="root"]/div/section/main/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div')
    clBtn.click()
    clList = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div')
    nsBtn = driver.find_element_by_xpath('//*[@id="root"]/div/section/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div')
    nsBtn.click()
    nsList = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div')
    for cl in clList:
        clBtn.click()
        cl.click()
        print("%r done", cl)
        for ns in nsList:
            nsBtn.click()
            ns.click()
            print("%r %r click", cl, ns)
            time.sleep(2)

  
    cl = driver.find_element_by_xpath('//*[@id="root"]/div/section/main/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div')
    cl.click()
    #time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div').click()

    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div').click()
    #time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div/div[3]/div').click()
'''

    #ns = driver.find_element_by_xpath('//*[@id="rc_select_5"]/../..')
    #Select(ns).select_by_visible_text("wanghui")







    #assert "Management" in driver.title
    #driver.quit()


if __name__ == "__main__":
    test()