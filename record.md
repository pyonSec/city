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
