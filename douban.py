from selenium import  webdriver
import  time
#框架内容
url="https://accounts.douban.com/passport/login_popup?login_source=anony"
driver_path=r'D:\tool\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(executable_path=driver_path)
driver.get(url)
driver.implicitly_wait(5)
css_one=driver.find_element_by_css_selector

密码登录=css_one('body > div.account-body.login-wrap.login-start.account-anonymous > div.account-body-tabs > ul.tab-start > li.account-tab-account')
密码登录.click()

account=css_one('#username')
account.send_keys('请填写用户名')
paasword=css_one('#password')
paasword.send_keys('请填写密码')
login=css_one('body > div.account-body.login-wrap.login-start.account-anonymous > div.account-tabcon-start > div.account-form > div.account-form-field-submit > a')
login.click()
time.sleep(2)


new_url='https://www.douban.com/mine/'
driver.execute_script('window.open("' + new_url + '")')
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
个签=css_one('#display').text
if 个签=="":
    interacter=css_one('#edi > a')
    interacter.click()
else :
    driver.execute_script("$('#edi > a').click()")
input=css_one('#edit_signature > form > input[type=text]:nth-child(2)')
input.clear()
input.send_keys('哈哈哈小豆瓣')
# submit=css_one('#edit_signature > form > input.submit')
# submit.click()
driver.execute_script("$('#edit_signature > form').submit()")
driver.quit()