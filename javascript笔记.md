# javacripts 笔记

## 1.语法

1. 语句结尾

   ```javascript
   var name;
   ```

2. 函数小括号，大括号

   ```javascript
   function touch() {
       alert("touch my isohode");
   };
   ```

3. 驼峰命名法

   ```javascript
   document.getElementById("keng");
   ```


## 2.数据类型

```javascript
var number=123;
var string="I am string.";
var Boolean=ture;小写t
var function();
undefined;
object;
NaN not a number;
```





## 3.运算

1. 有字符串 + 就是字符串拼接

2. ```
   - * / % 被强制转换为数字计算 
   ```

   ​



## 4.数组

bar arr =[1,2,3,4,]



| 组数操作 | javascript     | python |
| :--- | -------------- | ------ |
| 插入   | insert         | insert |
| 提取   | slice          | join   |
| 删除   | delete         | delete |
| 索引   | index          | index  |
| 删除末尾 | pop            |        |
| 插入末尾 | push           |        |
| 删除头部 | shift          |        |
| 插入头部 | unshift        |        |
| 转换   | join ,tostring |        |
| 排序   |                |        |
| 插入数组 |                |        |
|      |                |        |



## 5.JSON

1. 最后一项不能加逗号结尾

2. 字符串

3. ie 7以下不支持json，去json.org下载源代码导入一个json类

4. var boj = {

   ​	"name":"shuoyar",

   ​	"age": 19

   }

   var obj = new object();

   obj.name = "tuple";

5. json 转化为 object JSON.parse()

6. object 转化为json JSON.stringify()

7. jquery的json方法可以有特别功能





{"key":"json","name":"shuoyar','shoose','going'}

## 6.定时器（timer）

1. 延时定时器 

   ```javascript
   setTimeout(funchtion(不加括号),time(ms))
   ```

   ​

2. 循环定时器

   ```javascript
   setInterval(function,time(ms))
   ```

3. 清除定时器

   ```javascript
   clearInterval()
   ```

## 7.时间对象

```javascript
var date =new Date();
var date = Date();
```

## 8.获取元素

1. 获取所有子节点

```javascript
var nodename = document.getElementById("nodename");
console.log([nodename].children);
console.log([nodename].firstchild);
console.log([nodename].childNodes);
```

2. 获取同级下一个节点

```javascript
function nextElement (dom) {
	return dom.nextElemetSibling === undifined ? dom.nextSibling : dom.nextElementSibling;
};
alert(nextElement([nodename]).nodeName);
```

3. 获取同级上一个节点

```javascript
function previousElement (dom) {
  return dom.previousElementSibling === undifined ? dom.reviousElementSibling :dom.previousSibling;
};
alert(reviousElement([nodename].nodeName));
```

4. 获取父节点

```javascript
alert([nodename].parentNode);
```

5. 移除节点

```javascript
var [fathernode] = [nodename].parentNode;
fathernode.removeChild([nodename]);
```

6. 创建元素

```javascript
var nodename = document.createElement("tagname");
nodename.className = "";
nodename.id = "";
nodename.innerHTML = "";
nodename.name = "";
fathernode.appendChild(nodename);
```

7. 插入元素

```javascript
fathernode.insertBefore(nodename,childnodename);
```



## 9.事件

window代表全局，window.event

1. 获取事件的对象

   ```javascript
   <div id = "box1">
     获取事件对象的方法1
   </div>
   <div onmouseup="click1()" id = "box1">
     获取事件对象的方法2
   </div>

   document.getElementById("box1");
   box1.onmouseup = click1;
   function click1(e) {
       e = e || event;
     	for (var i in e ) {
           console(i + "===" + e[i]);
       }
   }
   ```

   ​

2. 冒泡事件

3. 拖拽

4. 注册事件和注销事件

5. 键盘事件


2. 捕获事件



## 10.ajax

## 11.实例

幻灯片

```javascript
var slideIndex=1;
var time =1;
showSlide(slideIndex);
function currentSlide(n) {
	showSlide(slideIndex = n);
}
function plusSlide (n) {
	showSlide(slideIndex += n);
}
function showSlide (n) {
	var i;
	var slides = document.getElementsByClassName("myslides");
	var dots = document.getElementsByClassName("header_dot");
	 	if (n < 1) {
	 		slideIndex = slides.length;
	 	}
	 	if (n >slides.length) {
	 		slideIndex = 1;
	 	}
		for (i = 0; i < slides.length; i++) {
			if (i == slideIndex-1) {
				slides[i].style.display = "block";
				dots[i].className = "header_dot active";

			}else {
				slides[i].style.display = "none";	
				dots[i].className = "header_dot";
			}
		} 
}
function showSlideByTime() {
	slideIndex++;
	showSlide(slideIndex);
}
```

按钮划出

```javascript
var comment_btn = document.getElementsByClassName("comment_btn");
var comment_content = document.getElementsByClassName("mainsc_content_comment");
for (var i=0; i < comment_btn.length; i++) {
	comment_btn[i].onclick = function(){
		var comment_content=this.parentNode.parentNode.parentNode.nextSibling.nextSibling;
		if (comment_content.style.maxHeight) {
			comment_content.style.maxHeight = null;
		}
		else {
			comment_content.style.maxHeight = comment_content.scrollHeight+'px';
		}
	}
}
```

登录框点击外部消失

```javascript
var closeLogin = document.getElementById("login1");
window.onclick = function(e) {
	e = e || event ;
	if (e.target == closeLogin) {
		closeLogin.style.display = "none";
	}
}
```



## 11.jquery语法和实例

按钮划出

```js
$(".comment_btn").each(function(i,el) { 
	$(el).click(function(event) {
		console.log($(".mainsc_content_comment").eq(i));
		$(".mainsc_content_comment").eq(i).slideToggle(300);
	});
});
```

登录框点击外部消失

```javascript
$(document).click(function(event) {
		if (event.target == $("#login1").get(0)) {
		$("#login1").css('display','none');
	}
});
```

### 元素方法

```javascript
#=========== 选取元素 =================
$("div:first")  #第一个元素是div的元素
$("div:last")	#最后一个元素是div的元素
$("div:even") #div中的偶数元素
$("div:odd") 	#div中的奇数元素
$("div:fist-child")	#第一个子元素是div的元素
$("div ul")	
$("div>img")
$("div+div")
$("div~a") #同级的a
$("div:eq(n)") #所有元素集合中的index=n
$("div:gt(n)") #大于
$("div:lt(n)") #小于

#=========== 遍历元素 =================
$("filter").add().add().add() #向集合里添加新元素	
$("filter").first()	#符合filter的第一个元素
$("filter").children("#id")	#符合filter的所有子元素
$("filter").contents()	#符合filter的所有内容，包括text节点
$("filter").eq()	#符合filter的index=n的元素
$("filter").each(function) #对符合filter的所有元素执行function
$("filter").filter("#id",function(){}) #符合filter的元素集合里筛选符合filter的子元素
$("filter").find("") #符合filter的元素集合里寻找符合filter的元素
$("filter").has("") #符合filter中返回拥有filter的元素集合
$("filter").is("") #判断 返回true
$("filter").next()	#符合filter的同级下一个元素
$("filter").nextAll()	#符合filter的同级后面的所有元素，可以增加filter
$("filter").nextUntil("filter") #符合filter的后面的所有元素，直到filter
$("filter").not("")	#符合filter中移除filter
$("filter").offsetParent()	#符合filter的元素集合中返回定位的父级元素
$("filter").parent()
$("filter").parents()
$("filter").parentsUntil("filter")
$("filter").prev()
$("filter").prevAll()
$("filter").prevUntil()
$("filter").siblings() #符合filter的所有同级元素
$("filter").slice() #符合filter的从n到m之间切片的元素。
# ==================== 元素操作 ===================
.html() ## innerHTML
.css() ##.style
.addClass() ## 
.after()  #在节点后增加元素
.before() #在节点前增加元素
.append() .appendTo()#在节点内的结尾增加
.prepend() .prependTo() 
.attr() #设置节点属性
.clone() #复制得到一个节点
.detach()
.prop()
.empty()
$('').insertAfter('')  #在所选节点之后插入内容
$('').insertBefore('')  #在所选节点之后插入内容
$("filter").remove()
$("filter").removeClass()
$("filter").toggleClass()
$("filter").removeAttr()
$("filter").removeProp()
$("filter").replaceAll('filter')
$("filter").replaceWith()
$("filter").text()
$("filter").val()
$("filter").get()
$("filter").index()

# =============== jquery 效果 ====================
$("filter").animate({style},'slow','linear',function(){})
$("filter").fadeIn()
$("filter").fadeOut()
$("filter").fadeToggle()
$("filter").slideDown()
$("filter").slideUp()
$("filter").slideToggle()
$("filter").toggle()
```



1. 中文文档：jquery.cuishifeng.cn
2. 使用jquery需要引用jquery方法，在头部引用，link cdn.code.baidu.com
3. ​


