# 城市数据可视化与分析系统
## 系统
DWF
+ 后端设计包括
    - 组织模型: 用户管理
    - 数据模型：数据库表
+ postgresql只是存储 时序数据库的链接,时序那边的元数据由iotdb产生

## 表设计的计划
### 用户管理
+ admin:
+ user
+ guest
### 数据表
+ 城市

|city|Position|Name|Intro|
|-|-|-|-|
|Peking|0|北京|北京|

+ 变化量(考虑使用timeseries)

|time|gdp|finacial|population|employee|income|education|house|
|-|-|-|-|-|-|-|-|
|2012|8888|0|88|60%|33|78%|1.3|

**变化量数据库中存储oid？Name.删除后是否删除该数据库字段**
+ 删除：增加负担
+ 不删除：再次增加，oid需要重新更新，是否需要加入name
参数调整：需要表单，可选中数据进行计算
评分更新：导入数据后自动依赖更新

经济：
+ gdp, 城镇居民消费水平,城镇居民消费水平指数(CPI),财政收入 
+ 物价

金融
+ 储蓄年末余额，
+ 地方公共预算收入与支出
+ 上市公司数量，社会融资规模

科技：

教育：
+ 高等教育学校，中等教育学校，
### 数据来源调研
[知乎](https://zhuanlan.zhihu.com/p/25130679)
[上海统计年鉴](http://tongji.cnki.net/kns55/navi/YearBook.aspx?id=N2017120310&floor=1###)
[北京统计年鉴](http://tongji.cnki.net/kns55/navi/YearBook.aspx?id=N2019010235&floor=1)
[中国统计信息网](http://www.tjcn.org/)
### 中国统计局Api调研
数据地图:
http://data.stats.gov.cn/mapdata.htm?m=mapDataHandle&dbcode=fsyddt&wd=reg&zbId=&sjval=
http://data.stats.gov.cn/mapdata.htm?m=dateHandle&dbcode=fsyddt&wd=sj&sjval=last1000
dbcode=fsyddt&wd=reg&zbId=A0201&sjval=201506

[简书http爬取](https://www.jianshu.com/p/9827a052da91)
[github爬取](https://zuzhaoye.github.io/blog/scrap_javascript/)

查询按钮:http://data.stats.gov.cn/adv.htm?cn=E0101:292

http://data.stats.gov.cn/adv.htm?m=advquery&cn=E0101

找到查询按钮和easyquery之间跳转与参数传递关系

调研状况：
+ http://www.mytju.com/classcode/tools/messyCodeRecover.asp
+ windows-1252	UTF-8编码的中文

模拟提交的表单中json

[{"wd":"zb","zb":["A0101"],"name":["国内生产总值"]},{"wd":"reg","zb":["110000","310000","340100","350200"],"name":["北京","上海","合肥","厦门"]}]

表单做post操作

<form id="advQueryForm" action="/adv.htm?m=advquery&amp;cn=E0105" method="post">
    
document.getElementById("c").value = jsonStr;
document.getElementById("advQueryForm").action = url;

直接fetch疑似有跨域问题，无法得到正确的返回值
```js
fetch("http://data.stats.gov.cn/adv.htm?m=advquery&cn=E0105", {method: 'POST', mode:'cors', headers:{'Content-Type': 'application/json'},redirect:'follow',referrerPolicy:'no-referrer',body:JSON.stringify([{"wd":"zb","zb":["A0101"],"name":["国内生产总值"]},{"wd":"reg","zb":["110000","310000","340100","350200"],"name":["北京","上海","合肥","厦门"]}])}).then(data=>{console.log(data)})
```
在`http://data.stats.gov.cn/`下执行可以获得`ReadableStream`
```
url="http://data.stats.gov.cn/adv.htm?m=advquery&cn=E0105"
param=[{"wd":"zb","zb":["A0101"],"name":["国内生产总值"]},{"wd":"reg","zb":["110000","310000","340100","350200"],"name":["北京","上海","合肥","厦门"]}]
function Post(URL, PARAMTERS) {
         var temp_form = document.createElement("form");
         temp_form.action = URL;
         temp_form.method = "post";
         temp_form.style.display = "none";
         var opt = document.createElement("textarea");
         opt.name = "c";
         opt.value = PARAMTERS;
         document.body.appendChild(temp_form);
         temp_form.submit();
     }
Post(url, param)
```
