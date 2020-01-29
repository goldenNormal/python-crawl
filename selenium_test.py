from selenium import  webdriver
import  time

driver_path=r'D:\tool\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.lagou.com/')
driver.implicitly_wait(5)
css_one=driver.find_element_by_css_selector
close=driver.find_element_by_id('cboxClose')
close.click()
time.sleep(2)
input=driver.find_element_by_id('search_input')
input.send_keys('python')
submit=driver.find_element_by_id('search_button')
submit.click()
close=css_one('body > div.body-container.showData > div > div.body-btn')
close.click()
# items=driver.find_elements_by_css_selector('div#s_position_list > ul > li')
items=driver.find_elements_by_css_selector('#s_position_list > ul > li.con_list_item> div.list_item_top > div.position > div.p_top > a')
hrefs=[]
for item in items:
    if(item.get_attribute('href')):
        hrefs.append(item.get_attribute('href'))
        # print('='*40)
#一共爬几页
pages=2
i=1
for href in hrefs[:pages]:

    driver.execute_script('window.open("'+href+'")')
    driver.switch_to.window(driver.window_handles[i])
    time.sleep(2)
    title=css_one('body > .position-head > div > .position-content-l > div').get_attribute('title')
    job_request=css_one('body > .position-head > div > .position-content-l > dd > h3').text
    job_advantage=css_one('#job_detail > dd.job-advantage').text
    details=css_one('#job_detail > dd.job_bt > div').text
    address=css_one('#job_detail > dd.job-address.clearfix > .work_addr').text
    print("职位名称：",title)
    print('职位要求：',job_request)
    print('职位优势',job_advantage)
    print('详细',details)
    print('地址',address)
    print('='*50)
    i+=1



