# django

## 1.创建项目

```shell
cd /[pathtoprojectdir] #定位到创建项目的目录
django-admin stratproject [projectname] #创建项目
python manage.py startapp [appname] #创建app
```

## 2.settings

```python
#设置databases
#设置static_url 和 static_root
#设置INSTALLED_APPS
#创建映射关系
python manage.py makemigrations
python manage.py migrate
```

## 3.urls

```python
#在app下创建新的urls.py
from . import urls.py
from django.conf.urls import url,include
#在项目下的urlpatterns里面include('apps.urls')
#=============
#通过urlpatterns的（）来传入参数
url(r'^linkstart/(\w+)/$',views.Linkstart)
#对应的views里面传入参数
def Linkstart(request,a)
	return HttPresponse('a')
#通过extra_patterns或者include[urls list]简写同样的前缀
urlpatterns = [
    url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/', include([
        url(r'^history/$', views.history),
        url(r'^edit/$', views.edit),
        url(r'^discuss/$', views.discuss),
        url(r'^permissions/$', views.permissions),
    ])),
]
#通过父级urlsconf传入include urls的参数可以被捕获，如果没有使用命名参数，则views函数捕获顺序是优先子urls，然后是父级urls。
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/',include('testapp.urls')),
    url(r'^test(?P<testarg>\w{3})/',include('testapp.urls')),
]
urlpatterns = [
    url(r'^page(\w{3})/$',views.page,name='page'),
]
#可以通过正则表达式使用嵌套捕获参数
url(r'^nested/(?P<title>page-(?P<name>\d+))/$',views.nested)
```

### 关于命名参数

```python
参数捕获：
1、捕获位置参数（可变参数）：在url函数中，第一个正则表达式使用（）括号进行捕获参数.
2、捕获关键字参数：在url函数中，第一个正则表达式使用（?P<keyword>）进行捕获。
注意事项：
参数类型是字符串类型，所以，如果使用，需要使用int函数转换成int类型。
#最好给views函数取一个默认参数
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/$', views.page),
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

# View (in blog/views.py)
def page(request, num="1"):
    # Output the appropriate page of blog entries, according to num.
    ...
```

### 关于可选参数

```python
传递一个Python 字典作为额外的参数传递给视图函数。django.conf.urls.url() 函数可以接收一个可选的第三个参数，它是一个字典，表示想要传递给视图函数的额外关键字参数。
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/',include('books.urls'),{'switch':'true'}),
]
#对应views的函数写法
def index(request,**arg):
    if arg.get('switch') == 'true':
        print(datetime.datetime.now())
    return HttpResponse('<h1>这是首页</h1>')
```

### 关于include

```python
#方便项目管理：
#	一个project有一个总的urls.py，各个app也可以自己建立自己的urls.py，不过都需要使用#include()函数在project的urls.py文件进行注册。#hello_django/urls.py     主url文件
from django.conf.urls import include,url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/',include('books.urls')),
]
	
```

### 关于name

```python
给一个匹配的url地址取名字
一般用于模板
也可以使用reverse进行页面重定向
urlpatterns =[
    url(r'^$',views.index),
    url(r'article/$', views.article,name='books_article'),
    url(r'^(?P<books>\w+)/$',views.book_list,name='books_lists'),
    url(r'^article_new/$', views.article_new,name='books_article_new'),
]
#views重定向
def page(request):
    return HttpResponseRedirect(reverse('page_new'))
```

### 关于render渲染

```python
from django.shortcuts import render
from django.template.loader import get_template,render_to_string
def render_page(request):
  context = {
    'string':'字符串',
    'class_instance':类实例,
    'class_function':类方法,
    'class_attr':类属性,
    'list':列表,
    'dict':字典,
    'function':函数
  }
  return render(request,'render_page.html',context)

#render_page.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    这个变量是字符串对象：{{ string_1}}<br>
    这个变量是函数对象：{{ function_1}}<br>
    这个变量是类方法对象：{{ class_1_function}}<br>
    这个变量是类对象：{{ class_1}}<br>
    这个变量是类对象，访问类对象的属性：{{ class_1.name}}<br>
    这个变量是类对象，访问类对象的方法：{{ class_1.shout}}<br>
    这个变量是列表对象{{ list_1 }}<br>
    这个变量是列表对象,访问列表的元素{{ list_1.1 }}<br>
    这个变量是字典对象{{ dict_1 }}<br>
    这个变量是字典对象,访问字典的键{{ dict_1.key1 }}<br>
</body>
</html>
```



## 4.models

### 4.1创建models

```python
#在books目录下进入models.py
#输入类似下面的代码：

# -*- coding:utf-8 -*-  
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
        def __unicode__(self):
            return self.name
```

### 4.1安装model

**在最初的配置文件settings.py中找到 **

**INSTALLED_APPS**

**加入自己的app名称，比如'books'**

### 4.2创建映射关系

```
#设置databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER':'shuoyar',
        'PASSWORD':'',
        'HOST':'47.94.144.74',
        'PORT':'3306'
    }
}

#创建映射关系
python manage.py makemigrations
python manage.py migrate
#每次更改models文件之后都需要重新建立映射
```

### 4.3操作models的方法

```python
python manage.py shell #打开导入了django的shell
from books.models import Author

##增加
p1 = Publisher(name = 'banana',age = 30,emai= 'eaiejfie@132.com')
p1.save()
######################
p1 = Publisher()
p1.name= ''
p1.age = 
p1.email = 
p1.save()
#########################
Publisher.objects.create(name = ''.age = 30 ,email= '')
Publisher.objects.get_or_create('')

#查询
Publisher.objects.get(name = '')
Publisher.objects.all()[m:n]
Publisher.objects.filter(name ='')
Publisher.objects.filter(name_exact ='')
Publisher.objects.filter(name_iexact ='')#大小写不区分
Publisher.objects.filter(name_contains ='')
Publisher.objects.filter(name_regex ='')
Publisher.objects.filter(name_iregex ='')
Publisher.objects.exclude(name ='')#排除某些条件
Publisher.objects.filter(name ='').exclude(age = 24)

#排序
Publisher.objects.order_by('age')
#修改
Publisher.objects.filter(name = 'banana').update(name = 'banana')
#删除
Publisher.objects.filter().delete()
#更改表名称
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    class Meta:
      db_table = "Publishernew"
        def __unicode__(self):
            return self.name
python manage.py makemigrations
python manage.py migrate

#表关系的操作
from shuoyar.models import Book,Author,Publisher,Book_info
b1= Book.objects.get(title ='魔戒')
a1 = Author.objects.create(name = '托尔金',age=34)
a1 = Author.objects.get(name = '托尔金')

bi1 = Book_info.objects.create(isdn=100001,price = 230)
b1[0].author.add(a1)
b1[0].save()
a1.book_set.all()
b1.author.all()
Article.objects.filter(publications__id=1) #通过关系表列对象查询
b1.book_info.isdn #一对一关系可以直接查询不用all（）
bi1.book #一对一关系可以直接查询不用_set
```



## 4.Views

```python
from shuoyar.models import Auther,Book,Publisher #引入models
#标准过程：通过models获取数据库数据，通过字典构建contenx上下文，渲染模板，
第一种方法：通过Template和Context来构建template实例，在通过t.render(),Httpresponse（t.render()）
第二种方法：render_to_string('html',context)
第三种方法：render
#不要忘记404error的Http404
return Httpresponse() #
return render(request,'template.html',content_type)#最常用的渲染模板
#===========================redirect()
重定向
#==========================content_type 不同的格式文件，返回的content_type不同
text/html ： HTML格式
    text/plain ：纯文本格式      
    text/xml ：  XML格式
    image/gif ：gif图片格式    
    image/jpeg ：jpg图片格式 
    image/png：png图片格式
   以application开头的媒体格式类型：
   application/xhtml+xml ：XHTML格式
   application/xml     ： XML数据格式
   application/atom+xml  ：Atom XML聚合格式    
   application/json    ： JSON数据格式
   application/pdf       ：pdf格式  
   application/msword  ： Word文档格式
   application/octet-stream ： 二进制流数据（如常见的文件下载）
   application/x-www-form-urlencoded ： <form encType=””>中默认的encType，form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）
   另外一种常见的媒体格式是上传文件之时使用的：
    multipart/form-data ： 需要在表单中进行文件上传时，就需要使用该格式
     以上就是我们在日常的开发中，经常会用到的若干content-type的内容格式
#==========
```

python manage.py runserver

## 5.templates

```python
{%%} #代表语法
{{paramaters}} #代表变量 变量可以是字符串、类、函数、字典、函数属性和方法、列表、
#par变量可以用.进行查找。字典查找key的值，类查找方法和属性，列表查找索引，字符串同列表
#模板过滤器
{{parameters|function:paramater}}
{{parameters|default:paramater}}#默认值
{{parameters|add:paramater}} 
{{parameters|join:''}}#字符串拼接
{{parameters|slice:'切片'}}
{{ html|safe }}<br> #关掉自动转义，使字符串中html标签生效
{{ float|floatformat:'2' }}<br> #浮点数格式化，小数点位数
{{ now|date:'Y/m/d/H:i:s ' }}<br>#格式化日期
{{ now|time:'h:i:s ' }}<br> #格式化时间
{{ test|truncatechars:7 }}<br> #字符串只显示7位字符，其余显示为...
{{ test|truncatewords:7 }}<br> #字符串只显示7位单词，其余显示为...
{{ test|length }}<br> #获取长度的方法
```

### templates的标签语句

```Python
{% tagname %}
{% endtage %}
{% for foo in list %}
	{% if foo.counter0 <= 5%}#这里的逻辑运算符必须空格
	<h1 class="name" style = "display:inline-block">foo</h1>
   		{% if foo.last == True 5%}
    {% endif %}
{% endtage %}
'''
forloop.counter：当前迭代的次数，下标从1开始。
forloop.counter0：当前迭代的次数，下标从0开始。
forloop.revcounter：跟forloop.counter一样，下标从大到小。
forloop.revcounter0：跟forloop.counter0一样，下标从大到小。
forloop.first：返回bool类型，如果是第一次迭代，返回true,否则返回false。
forloop.last：返回bool类型，如果是最后一次迭代，返回True，否则返回False。
forloop.parentloop：如果发生多层for循环嵌套，那么这个变量返回的是上一层的for
（3）for…in…empty…：如果没有数据，跳转到empty中。
（4）load：加载第三方标签。最常用的是{%load static%}
（5）url：返回一个命名了的URL的绝对路径。
（6）with：缓存一个变量。
（7）autoescape：开启和关闭自动转义。等同于过滤器里面的{{url_safe|safe}},但是可以把语句块里面的所有参数都转义'''
============================================
{% with globalagr=paramter %}
#可以调用globalagr作为全局变量
{% endwith %}
=============================================
#模板的继承和引用
#父模板里
{% block blockname%}
#中间是子模板需要修改的部分,外面是子模板可以继承的部分
{% endblock %}
#子模板里
{% extends 'temp.html'%}
{% block blockname%}
{% endblock %}
```

### 模板继承

```python
#父级的html模板
{% block name%}
父级模板的内容
{% endblock %}
#子级的html模板


```

### 模板路径

```
'DIRS': [os.path.join(BASE_DIR, 'templates'),'List']
```



## 6.Form表单

```python
#在app下建立一个form.py 
from django import forms
class Add_form(forms.Form):
  a = forms.IntegerField()
  b = forms.IntergerField() 
```







