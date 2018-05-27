# C8 验证码

## 极验滑动验证码的识别(根据geetest网站来说的操作，其他的也是一样的操作)
* 抓到登录的url, 用户名密码不需要，咱们不需要登录进去
* 首先模拟点击(点击验证后出现华东验证的部分), btn.click()
* 在进入到滑动验证部分
    1. 得到验证图片的位置
    2. 通过截屏在截取验证图片(这张图片是没有缺口的)
    3. 点击一下出现缺口，在截屏，截取有缺口的验证码
    4. 对比两张，找到缺口的位置(像素比较即可)
    5. 通过模拟先匀加速，在匀减速拖动, (将每个时间段走的路径保存)
    6. 通过selenium模拟拖动即可


## ChromeDriver对应的Chrome版本
<table>
	<tr>
		<th>chromedriver版本</th>
		<th>支持的Chrome版本</th>
	</tr>
	<tr>
		<td>v2.38</td>
		<td>v65-67</td>
	</tr>
	<tr>
		<td>v2.37</td>
		<td>v64-66</td>
	</tr>
	<tr>
		<td>v2.36</td>
		<td>v63-65</td>
	</tr>
	<tr>
		<td>v2.35</td>
		<td>v62-64</td>
	</tr>
	<tr>
		<td>v2.34</td>
		<td>v61-63</td>
	</tr>
	<tr>
		<td>v2.33</td>
		<td>v60-62</td>
	</tr>
	<tr>
		<td>v2.32</td>
		<td>v59-61</td>
	</tr>
	<tr>
		<td>v2.31</td>
		<td>v58-60</td>
	</tr>
	<tr>
		<td>v2.30</td>
		<td>v58-60</td>
	</tr>
	<tr>
		<td>v2.29</td>
		<td>v56-58</td>
	</tr>
	<tr>
		<td>v2.28</td>
		<td>v55-57</td>
	</tr>
	<tr>
		<td>v2.27</td>
		<td>v54-56</td>
	</tr>
	<tr>
		<td>v2.26</td>
		<td>v53-55</td>
	</tr>
	<tr>
		<td>v2.25</td>
		<td>v53-55</td>
	</tr>
	<tr>
		<td>v2.24</td>
		<td>v52-54</td>
	</tr>
	<tr>
		<td>v2.23</td>
		<td>v51-53</td>
	</tr>
	<tr>
		<td>v2.22</td>
		<td>v49-52</td>
	</tr>
	<tr>
		<td>v2.21</td>
		<td>v46-50</td>
	</tr>
	<tr>
		<td>v2.20</td>
		<td>v43-48</td>
	</tr>
	<tr>
		<td>v2.19</td>
		<td>v43-47</td>
	</tr>
	<tr>
		<td>v2.18</td>
		<td>v43-46</td>
	</tr>
	<tr>
		<td>v2.17</td>
		<td>v42-43</td>
	</tr>
	<tr>
		<td>v2.13</td>
		<td>v42-45</td>
	</tr>
	<tr>
		<td>v2.15</td>
		<td>v40-43</td>
	</tr>
	<tr>
		<td>v2.14</td>
		<td>v39-42</td>
	</tr>
	<tr>
		<td>v2.13</td>
		<td>v38-41</td>
	</tr>
	<tr>
		<td>v2.12</td>
		<td>v36-40</td>
	</tr>
	<tr>
		<td>v2.11</td>
		<td>v36-40</td>
	</tr>
	<tr>
		<td>v2.10</td>
		<td>v33-36</td>
	</tr>
	<tr>
		<td>v2.9</td>
		<td>v31-34</td>
	</tr>
	<tr>
		<td>v2.8</td>
		<td>v30-33</td>
	</tr>
	<tr>
		<td>v2.7</td>
		<td>v30-33</td>
	</tr>
	<tr>
		<td>v2.6</td>
		<td>v29-32</td>
	</tr>
	<tr>
		<td>v2.5</td>
		<td>v29-32</td>
	</tr>
	<tr>
		<td>v2.4</td>
		<td>v29-32</td>
	</tr>
</table>

## 滑动验证码
* 通过验证网站来进行操作

## 宫格验证码
>作者提供的思路是 先模拟登录很多次，将可能的图片都保存下来, 然后登录的时候通过模板匹配

