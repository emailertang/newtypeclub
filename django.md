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
#创建映射关系
python manage.py makemigrations
python manage.py migrate
```



## 3.models

### 2.1创建models

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

### 3.1安装model

**在最初的配置文件settings.py中找到 **

**INSTALLED_APPS**

**加入自己的app名称，比如'books'**

### 3.2创建映射关系

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

### 3.3操作models的方法

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
```

python manage.py runserver

## 3.templates

```
{%%} 代表语法
{{}} 代表变量 科学的不科学方法验证， create the sigle plate
```

