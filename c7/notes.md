
# Selenium

##  install
```bash
pipens install selenium
```

### chromedriver
```bash
https://chromedriver.storage.googleapis.com/2.9/chromedriver_linux64.zip
解压
sudo mv chromedriver /usr/bin
```

## Use selenium
* 单个节点查找
```python
find_element_by_id(), by_name, by_xpath(), by_css_selector(), by_class_name()
或者
find_element(By.xx, value)
```

* 多个节点选择elements
```python
finf_elements(By.CSS_SELECTOR, '.serviced-bd li')
find_elements_by_id, name ....
```
* 节点交互
```
input = brower.find_element_by_id('kw')    # 通过id 得到输入框的焦点
input.send_keys("python")    # 通过send_keys方法进行输入
```

* 动作链
```
from selenium import webdriver
from selenium.webdriver import ActionChains


brower = webdriver.Firefox()    # 模拟火狐浏览器
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
brower.get(url)
brower.switch_to.frame("iframeResult")
source = brower.find_element_by_css_selector('#draggable')
target = brower.find_element_by_css_selector("#droppable")
action = ActionChains(brower)
action.drag_and_drop(source, target)
action.perform()

```

* 执行javascript脚本
```
brower.execute_script('alert("Hello")')
```

* 获取节点的信息
```
get_attribute()
不需要用bs4 或者xml进行解析, 直接用find_element选中元素，在通过get_attribute()获取值即可
kw = brower.find_element_by_id("kw")
print (kw.get_attribute("class"))    # 获取class的值

text
获取文本的值
kw.text

id, location, tag_name, size
kw.id, kw.location, kw.tag_name, kw.size

```

* 切换Frame(默认是在父frame中)
```

from selenium import webdriver

brower = webdriver.Firefox()
borwer.switch_to.frame("frame_id")
brower.switch_to.parent_frame()    # 回到父frame中

```

* 延时等待
    1. 隐式等待
    ```python
    调用implicitly_wait(time), 在查找节点没有立即出现，会等待在查找dom, 默认时间是0
    ```
    2. 显式等待
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    brower = webdriver.Firefox()
    brower.get(url)
    wait = WebDriverWait(brower, 10)
    input = wait.util(EC.presence_of_element_located((By.ID, 'q')))  # 当id=q的节点出现的时候，返回
    button = wait.util(EC.element_to_be_clickable(By.CSS_SELECTOR, '.btn-search'))    # 当btn按钮可以点击的时候返回
    ```

* 前进后退(当在页面中打开了好几个页面后)
```
brower.back()
brower.froward()
```

* Cookies
```
borwer.add_cookie({})
brower.get_cookies()
borwer.delete_all_cookies()
```

* 选项卡的管理
```
brower.execute_script('window.open()')    # 打开一个新的tab
brower.switch_to_window(brower.window_handler[1])
在做其他的操作
```

* 异常处理
```
from selenium.common.exceptions import TimeoutException, NoSuchElementException
```

