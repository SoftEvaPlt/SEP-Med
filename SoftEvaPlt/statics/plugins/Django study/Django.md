# Django web开发 Day1

## 1. Django的安装

和之前python一样，通过pip来安装即可

```
pip install django
```

django和其他第三方Python模块一样，会在当前python环境下的`lib>site-package`中，只是django是比较大的那种模块。

But，django这个包呢同时会生成`django-admin.exe`在`Scripts`文件夹中，这个exe可执行文件是帮助我们操作django项目的。目录情况大体如下：

```
python环境路径
	- ...
	- scripts
		- pip.exe
		- django-admin.exe	【工具、创建django项目的文件和文件夹】
	- lib
		- 内置模块
		- site-package		【安装的第三方模块】
			- flask
			- ...
			- django		【框架的源码】
			- ...
	- python.exe
	- ...
```

## 2. 创建项目

django项目会有一些默认的文件和默认的文件夹，所以我们先得通过前面提到的`django-admin.exe`来进行一些准备操作。

### 2.1 通过终端创建

1. 打开终端

2. 进入某个目录（项目放在哪就去哪，最好不要出现中文，防止编码问题）

3. 执行命令来创建项目

   ```shell
   "python环境路径\scripts\django-admin.exe" startproject django项目名
   # 如果python环境路径配置到了电脑的环境变量中就可以这么写了
   django-admin.exe startproject django项目名
   ```

   比如我们创建项目名为`track_chart_web`的django项目，输入`django-admin startproject track_chart_web`，即可看到自动生成的目录结构，此时django项目就创建成功了：

   ![image-20220129183226031](Django.assets/image-20220129183226031.png)

### 2.2 通过Pycharm创建

> PS：这里的 Pycharm得是专业版，社区版没有此功能。

菜单栏点击`File`，选择`New Project...`，就可以开始创建项目了。

![image-20220129183929766](Django.assets/image-20220129183929766.png)

点开上图两个红箭头所指的位置，环境我们选`Existing interpreter`，其中的`Interpreter`就默认即可。其他的都默认即可。

> 关于 Python环境选择：
>
> 可以看到这里的界面两个选项：一个是 `New environment using`，一个是 `Existing interpreter`。前者呢，是为项目创建一个新的 Python环境，然后单独进行管理；后者呢，是使用电脑上已有的 Python环境，如果你的电脑上存在多个 Python环境，那你点开 `Existing interpreter`其中的 `Interpreter`就可以看到所有的已有环境，接着进行选择。
>
> 以普遍理性而言，写项目嘛，考虑移植性等长远目标，一个项目最好得有自己的独立 Python环境，如果多个项目同时使用一个 Python环境，那环境就不好管理了（eg：是某些项目需要用到的第三方模块是一个，但版本不同，可能就会导致项目跑不起来）。
>
> But，我个人也不习惯用 `New environment using`来创建项目的单独环境（因为很容易导致报错），而是用 Python的一个第三方模块—— `virtualenv`、`virtualenvwrapper-win`。详细操作见链接：[Django独立环境配置](待更新)
>
> ```shell
> pip install virtualenv
> pip install virtualenvwrapper-win
> ```

![image-20220129184549328](Django.assets/image-20220129184549328.png)

好啦，最后我们点create就可以得到`2.1 通过终端创建`一模一样的目录结构咯（只是会多一个templates空文件夹）。

### 2.3 对比差异

在终端的命令行方式创建项目是标准的方法；Pycharm的话，会在标准的基础上，多一些东西。

- 多创建了一个templates目录，我们删除，后面前端的模板文件不放在这里
- 项目文件`settings.py`中的`TEAMPLATES`的字典下键为`'DIRS'`对应的值不同，我们也不用它，值改成空列表`[]`即可

项目文件介绍：

```shell
django_study_demo
│─ manage.py			【项目管理的脚本，不要修改，eg：启动、创建app、数据库管理等】
└─django_study_demo		【与项目同名的文件夹】
     │─ asgi.py			【和wsgi.py一起，接收网络请求的】【不用修改】【Django接收异步的】
     │─ settings.py		【项目的配置文件，eg：数据库连接信息、注册app等】【常操作】
     │─ urls.py			【全部的URL和函数的对应关系】【常操作】
     │─ wsgi.py			【和asgi.py一起，接收网络请求的】【不用修改】【Django接收同步的】
     │─ __init__.py
```

> Django的异步问题解决方案不是很成熟，所以 asgi.py和 wsgi.py不用过多了解。

## 3. 创建APP

这里的APP不是手机应用那个APP，而是一部分功能的意思。一个Django项目可能需要处理多个业务，我们将业务拆解，一部分一部分分开来管理代码会比较有条理，所以可以通过创建多个app来分别实现多个业务功能。

举栗来说，一个项目分别对用户管理、订单管理、后台管理等业务都创建相应的app去实现。这样每个app的表结构、函数、HTML模板、css等都可以分开管理，不会混乱。

But，app是为了分开实现那些大功能的，像增加用户信息和删除用户信息这两个小功能就大可不必分成两个app来写。所以，我们自己个人开发的时候，就可以只创建一个app来实现项目功能。

用Pycharm打开命令行界面（通过cmd打开也行，不过每次打开都要切换到当前项目路径下，很麻烦，所以最好直接用Pycharm的命令行界面直接打开），然后输入指令`python manage.py startapp app名`（通过manage.py来创建app）。

![image-20220129204355056](Django.assets/image-20220129204355056.png)

app目录结构介绍（Line 1~8前面说了，这里就不再提了）：

```shell
django_study_demo
│  manage.py
├─django_study_demo
│     asgi.py
│     settings.py
│     urls.py
│     wsgi.py
│     __init__.py
└─index						【app名命名的文件夹】
    │  admin.py				【固定的不用动】django默认提供的后台管理，但实际开发不常用
    │  apps.py				【固定的不用动】app启动相关
    │  models.py			【☆很重要，对数据库进行操作】这里不用SQL写了，Django封装了ORM供调用
    │  tests.py				【固定的不用动】用来单元功能测试的，个人小项目可以不用管
    │  views.py				【☆很重要，撰写视图函数（得我们自己写的）】
    │  __init__.py
    └─migrations			【固定的不用动】数据库变更记录，会自动生成文件，我们不用动
            __init__.py
```

## 4. 快速上手

想要让Django项目快速运行起来，我们还得按顺序操作以下步骤

### 4.1 确保app已注册

在前面`3. 创建APP`中，我们只是创建的app，但是这样还是不能正常跑起来app中的功能的，我们还得让Django知道，我们写了一个新app，这个声明的过程就是app的注册。==此过程需要修改settings.py==，过程如下：

1. 找到settings.py，在列表变量INSTALLED_APPS中，添加一个`''`，准备添加新app（我这里app名为index，大家不同app名需要相应的替换一些代码）

   ![image-20220129210505282](Django.assets/image-20220129210505282.png)

2. 我们打开新app目录，查看其apps.py内容

   ![image-20220129211451102](Django.assets/image-20220129211451102.png)

3. 我们需要调用这个类，所以用到我们导入模块的知识点通过`.`来找到相应文件中的类，所以在第一步写的`''`中应该写上`index.apps.IndexConfig`

   > PS：Django项目中默认从项目的根目录（项目的根目录 ≠电脑的根目录）所以路径默认从项目根目录写。

4. 结束。

### 4.2 URL和函数的映射

大家使用网站时，在网站内的页面跳转都会改变URL，不同的URL就需要后台调用不同的功能给用户使用。所以每个URL都得有函数来执行相应的代码。==此过程需要修改urls.py==，过程如下：

1. 找到urls.py中列表变量urlpatterns，添加一行`path('', )`

   ![image-20220129212535807](Django.assets/image-20220129212535807.png)

2. `path()`需要两个参数，前者是字符串，规定URL，后者是触发的函数名。规定的URL可以随便写，因为是我们自己规定哪个URL跳转哪个函数，我这就写`'index/'`

3. 前面说过，每个app都有个`views.py`，里面是写函数的，所以我们第二个参数位导入相应函数即可（还是模块导入的知识点，通过`.`来导入）

   ![image-20220129215931988](Django.assets/image-20220129215931988.png)

4. `path('index/', views.index)`这句的映射关系即为访问`http://www.xxxx.com/index`时，触发的函数是名为index的app下的`views.py`中的index函数。

5. 结束。

### 4.3 视图函数的撰写

好了，既然设置好了映射，但是这个函数我们还是没有写的（所以上面的截图中，index会被标黄的原因【没找到该函数】）。==这个过程需修改相应app下的views.py==，这个写就完了，函数大家都会写，这里就汇总一下小点即可。

![image-20220129223217894](Django.assets/image-20220129223217894.png)

注意点：

1. django中的视图函数必须带request这个参数
2. 视图函数必须return，一般返回的都是要传给前端的数据

> 以后会经常见到 request和 response这两个单词，可以简单理解为 request是前端给后端发的数据，response是后端给前端传的数据；所以函数必须带 request就可以理解了，这里的 HttpResponse()先简单理解为给前端发简单数据的，后面是得传 html文件给前端的，不怎么用 HttpResponse()的。

### 4.4 运行Django

命令行启动django项目：

```shell
python manage.py runserver
```

Pycharm启动django项目：

如果你是按我们创建项目的步骤一步一步来的，这里直接点绿三角即可运行django项目

![image-20220202112134770](Django.assets/image-20220202112134770.png)

点击这个按钮运行时，其实也就是让pycharm帮我们运行runserver这个命令。

![image-20220202112633489](Django.assets/image-20220202112633489.png)

这一行和我们刚才的`python manage.py runserver`很像，原理都是一样的。

好啦，运行起来项目到现在也没有什么报错，我们就可以访问本地8000端口（django占用端口默认是8000）的服务（`localhost:8000`和`127.0.0.1:8000`是一样的），来测试我们Django项目了。

好，点击访问`http://127.0.0.1:8000/`，出现是这样的画面

![image-20220202113147634](Django.assets/image-20220202113147634.png)

`Page not found`，就表示我们配置的URL有问题，这个空的URL没有函数对应。确实，我们找到我们当时写的urls.py，我们只写了一条`index/`的URL所对应的函数。

所以，我们访问`http://127.0.0.1:8000/index/`即可，页面显示的东西也是我们通过`HttpResponse()`上传的字符串。

![image-20220202113413289](Django.assets/image-20220202113413289.png)

至此，我们这个快速搭建django的步骤已经完毕，已经可以正常访问网址，看到结果了。

### 4.5 创建页面

上面的过程中，包含了创建index界面的步骤。那我们现在如果还要创建新的页面，只需要两个步骤：

1. views.py中撰写相应函数
2. urls.py中定义URL和函数的对应关系

```python
# 增加部分
# urls.py
path('user/add/', views.user_add),
path('user/delete/', views.user_del),

# views.py
def user_add(request):
    return HttpResponse("用户添加")

def user_del(request):
    return HttpResponse("用户删除")
```

上面这段代码加到项目代码中，再重新运行，这样就可以正常访问`user/add/`和`user/del/`两个URL。

![image-20220202124521910](Django.assets/image-20220202124521910.png)

![image-20220202124534089](Django.assets/image-20220202124534089.png)

### 4.6 模板文件&静态文件

#### 4.6.1 render()使用

But，正常应用中，网页都得是html那些文件，我们这现在还是就单纯返回字符串，太单调了。

那我们return后面就不用`HttpResponse()`了，而是用`render()`。`render()`的用法是这样。

```python
# 导入render，一般django默认
from django.shortcuts import render
def user_list(request):
    # 第一个位子是视图函数的request参数，第二个参数位是html文件路径
    return render(request, "user_list.html")
```

那么问题来了，这个模板文件的路径是从哪里开始呢？

#### 4.6.2 模板路径问题

一开始我们改过了`settings.py`中`TEMPLATES`字典的`DIRS`的值为空列表，所以默认的模板路径是当前app文件夹下的templates文件夹中的文件。所以我们在app下创建名为`templates`的文件夹（==必须得为templates，不要拼写错误！==），并在`templates`文件夹下创建html文件。

![image-20220202135633757](Django.assets/image-20220202135633757.png)

和4.5说的一样，设置函数和URL对应关系，就可以测试是否可以正常渲染模板文件。

![image-20220202141927243](Django.assets/image-20220202141927243.png)

然后我们运行django项目，然后访问我们设置的URL：`http://127.0.0.1:8000/user/list/`，就可以看到我们html文件被成功渲染到了前端。

![image-20220203151318494](Django.assets/image-20220203151318494.png)

同样的，我们想把`user_add()`那个函数也改写成模板文件渲染，我们就可以按图索骥，一步步操作了（这里就不放截图演示了）。

#### 4.6.3 静态文件static

开发过程中，像图片、css、js这些文件都称为静态文件，而这些静态文件，在django项目中也是必须放在规定文件夹中的，这个文件夹必须得叫`static`，和`templates`一样不能出现拼写错误。为了方便查找，static中，我们再分img、css、js、plugins来分类存放不同的东西。

![image-20220203161241323](Django.assets/image-20220203161241323.png)

比如我们引入一个图片作为示范（会发现src那个属性值Pycharm标黄了，暂时这么写，我们后面再说）：

```python
# user_list.html中增加一行代码
<img src="/static/img/default.png" alt="">
```

实现效果：

![image-20220203161113258](Django.assets/image-20220203161113258.png)

#### 4.6.4 static路径问题

django中呢，不推荐上面的那种路径写法（所以Pycharm标黄了），而是用下面的这种语法格式。

![image-20220203161718634](Django.assets/image-20220203161718634.png)

`{% ... %}`这个格式是django的模板语法，`load`是占位符（django的模板语法，不止load一个，我们用到就提一个，很简单，对于常用的有个印象即可，这个没有固定的语法规范），`{% load static %}`可以理解为加载static路径；然后后面`{% static 'img/default.png' %}`就是通过static调用路径，然后后面跟着的字符串就是static中相应文件的路径。

> P.S. django的模板语法要注意空格（有空格的地方必须得有空格），和 Linux的 shell很像。

下面我们示范一下，如何引入一下js和bootstrap插件：

1. 先把文件放到相应文件夹中（相应文件：[jquery-3.6.0.min.js和bootstrap-3.4.1-dist都在这个文件夹中](Django.assets)） 

   ![image-20220203163231737](Django.assets/image-20220203163231737.png)

2. html中导入。

   ![image-20220203164805300](Django.assets/image-20220203164805300.png)

3. 接着我们运行测试，看看booststrap的样式是不是可以正常出来。

   ![image-20220203164814614](Django.assets/image-20220203164814614.png)

4. 成功。

注意点总结：

- 声明static语法：`{% load static %}`要写在顶部，==写在html文件开头==
- 声明static的原理：
  1. 声明static会从`settings.py`中的`STATIC_URL`去找
  2. 后面还会说更多的`settings.py`中static的配置，肯定不止一个`STATIC_URL`的
- 调用语法：`{% static '...' %}`，其中`...`是静态文件的路径
- 用`{% ... %}`的优点：
  1. 比较规范（符合Django模板开发规范）
  2. 修改static文件路径时，方便修改（只需要改`settings.py`即可，不需要一个个去修改）

## 5. Django模板语法

本质：在html中写一些占位符，然后由数据对这些占位符进行替换和处理。

> P.S. 上面提到的占位符 static就是和 `/static/`（`settings.py`中`STATIC_URL`的值）做了替换。

我们先单独搞一个界面学习模板语法。

```html
<!-- templates_learn.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>模板语法学习</title>
</head>
<body>
    <h1>模板语法学习</h1>

</body>
</html>
```

```python
# views.py
def temp_learn(request):
    return render(request, "templates_learn.html")

# urls.py
path('temp_learn/', views.temp_learn),
```

然后运行并访问`http://localhost:8000/temp_learn/`即可。

### 5.1 调用后端数据

首先，`render()`函数第三个参数位可以提供给视图函数传递数据，不过==第三个参数必须是字典==！

![image-20220204160915789](Django.assets/image-20220204160915789.png)

然后我们在`templates_learn.html`中就可以通过`{{ ... }}`的语法根据键名来调用相应的数据。

![image-20220204161217443](Django.assets/image-20220204161217443.png)

然后我们刷新项目，再看浏览器页面，即可看到前端可以成功调用后端数据了。

![image-20220204161226500](Django.assets/image-20220204161226500.png)

### 5.2 索引

从上面的例子中可以看出，`{{ ... }}`的语法对于列表数据有些不适合，模板语法是否也提供了取其中元素的方法呢？

有的，通过`.`运算调用（和python不同，python是通过`[]`）

![image-20220204161649598](Django.assets/image-20220204161649598.png)

![image-20220204161546050](Django.assets/image-20220204161546050.png)

### 5.3 循环语句

不过，上面是4个元素的列表，如果有n个就得使用循环了，循环的模板语法为：

```django
{% for i in ... %}
	...
{% endfor %}
```

以我们上面`stu_list`为例：

![image-20220204163457751](Django.assets/image-20220204163457751.png)

效果：

![image-20220204163512432](Django.assets/image-20220204163512432.png)

> P.S. 是产生了四个 span标签的哦，因为模板循环语法中的 html语句会循环执行。
>
> ![image-20220204163639972](Django.assets/image-20220204163639972.png)

上面说了列表，字典也一样。

测试数据：

```python
# views.py
user_info = {
    "name": "zm",
    "salary": 100000,
    "role": "CTO",
}
return render(..., ..., {..., ..., "user_info": user_info})
```

html中调用：

![image-20220204164309778](Django.assets/image-20220204164309778.png)

效果：

![image-20220204164333651](Django.assets/image-20220204164333651.png)

> P.S. 元组那些数据结构和列表都差不多使用方法，最常用的就列表和字典。
>
> 如果是嵌套数据，也是一样，大家可以通过python一样的逻辑来处理，记得几个不同点即可：
>
> 1. python通过索引调用元素是`[]`，模板语法是用`.`。eg：`stu_list[0]["name"]`=>`stu_list.0.name`
> 2. 嵌套循环也一样，记得一个`{% for ... in ... %}`就得与一个`{% endfor %}`对应，不要少了！

### 5.4 条件语句

类比循环语句，条件语句语法也类似：

```django
{% if name == "XXX" %}
	...
{% elif name == "XX" %}
	...
{% else %}
	...
{% endif %}
```

和python一样，就是不用加`:`，结束必须带个`{% endif %}`，其他都一样。

eg：在html文件中简单写一个判断逻辑

![image-20220204165720231](Django.assets/image-20220204165720231.png)

观察结果，zm被加粗了。

![image-20220204165816704](Django.assets/image-20220204165816704.png)

### 5.5 模板语法原理

原理：

1. render()读取带有模板语法的html文件
2. django内部进行渲染（模板语法执行并替换成数据）
3. 最终得到只包含html标签的字符串
4. 将渲染完成的字符串传给用户浏览器。

所以，浏览器拿到的永远都是纯正的HTML文件中内容的字符串，不带任何django模板语法。我们刚才上面写的那些语句，我们从浏览器看看是什么（右击网页空白处=>检查），可以看到是纯正的HTML代码。

![image-20220204170539245](Django.assets/image-20220204170539245.png)

## 6. Request&Response

即请求和响应。这部分会介绍请求和响应的一些常用方法。

我们单独创建一个something界面（这里不赘述过程了）来单独聊聊这个知识点。

### 6.1 Request

request就是一个对象，封装了用户通过浏览器（爬虫等许多途径，不止通过浏览器一种）发送过来的所有请求相关的数据，常用的有：

- `request.method`：获取用户请求提交方式（GET/POST）
- `request.GET`：获取通过URL传递的参数
- `request.POST`：通过请求体中获得数据

![image-20220204184636609](Django.assets/image-20220204184636609.png)

如果想体验获取URL传递的数据，就在网址后面加上`?`，后面跟着键值对（`k=v`），以`&`隔开。如下图：

![image-20220204190733089](Django.assets/image-20220204190733089.png)

### 6.2 Response

视图函数中return所返回的，就是我们要写的response，常用的有：

- `HttpResponse()`：返回内容字符串给请求者；

- `render()`：读取HTML，并渲染，最终以字符串的格式返回给用户浏览器；

- `redirect()`：让浏览器重定向到其他页面，返回的是网址。

  > Q：重定向这个过程是怎么样的？
  >
  > ① 浏览器提交请求给Django，Django收到请求并提交请求给重定向的网址，Django获取到该网址返回的响应数据时，Django再返回给浏览器这个响应数据；
  >
  > ② 浏览器提交请求给Django，Django收到请求并直接返回给浏览器重定向的网址，浏览器重新去新的网址那里提交请求，然后新的网址给浏览器返回响应数据。
  >
  > A：②是对的。

### 6.3 练习

这里做一个简单的登录功能：

1. 先简单的做一个登录界面（login.html）

   ![image-20220204192043166](Django.assets/image-20220204192043166.png)

2. 设置路由、视图函数、以及映射关系，访问相应URL测试

   ![image-20220204192320336](Django.assets/image-20220204192320336.png)

3. 设置form表单的提交地址还是触发视图函数login()，而且采用post请求

   ![image-20220204192633786](Django.assets/image-20220204192633786.png)

4. 撰写login()中的代码逻辑

   ![image-20220204192950376](Django.assets/image-20220204192950376.png)

   > P.S. 这个逻辑还是很常用的，浏览器一开始访问 login.html（GET请求），视图函数login()就render渲染login.html；填写完 form表单点击提交，再次访问就是POST请求了，从而触发不同的代码逻辑。

5. 然后保存，刷新，去浏览器测试一下功能，这时我们就可以看到一个经典报错。

   ![image-20220204193056141](Django.assets/image-20220204193056141.png)

这段代码如果复刻到flask是没有问题的，但是django会报错，因为django自带了一个csrf，可以理解为是一个安全机制。解决方法大家也得记住，很简单，在form表单中，添加一行占位符：`{% csrf_token %}`。

![image-20220204193320744](Django.assets/image-20220204193320744.png)

再测试登录功能（记得刷新页面，重新输入，不然可能还是报错）

![image-20220204193411445](Django.assets/image-20220204193411445.png)

此时，我们在终端也可以看到后端接收到的数据

![image-20220204193652063](Django.assets/image-20220204193652063.png)

> P.S. 这个`'csrf....'`参数就是我们刚才加的`{% csrf_token %}`产生的。它的目的是检测该请求是否是网页传来的，防止黑客通过脚本，伪造请求攻击网站。简单说，csrf是一个安全机制。

然后我们就可以再写一个校验密码：

![image-20220204195532916](Django.assets/image-20220204195532916.png)

But，一般网站登录无论成功失败，都会返回一个页面的，肯定不是`HttpResponse()`这样只返回一个字符串。所以我们现在要改写成成功就跳转其他界面，失败就在原页面上显示登陆失败。

增加一个span标签，然后默认是空字符，登录失败时就传入值给tip，即可实现。

![image-20220205001706593](Django.assets/image-20220205001706593.png)

![image-20220205001729794](Django.assets/image-20220205001729794.png)

这里因为主页面没做，所以重定向到百度，道理都是一样的，就是网址不同罢了。

## 7. 数据库操作 ORM

上面的登录功能和实际应用中的登录功能还是差一些的，比如账号密码写死了，正常一个连接数据库的。所以这里我们来说说django连接数据库所采用的ORM。

之前学习数据库时，用的是MySQL数据库+pymysql。

```python
# 导入
import pymysql

# 连接
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123" charset="utf-8", db="test")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 发送指令
sql = "insert into admin(username,password,moblie) values('zm', '123', '13345512345')"
cursor.execute(sql)

# 关闭
cursor.close()
conn.close()
```

可在Django开发中，我们不需要在手动去写了，django给我们封装好了，并且增加了安全机制，让用户更简单更安全的操作数据库。这个封装好的东西就是ORM。

![image-20220205124503289](Django.assets/image-20220205124503289.png)

使用了ORM，我们直接可以通过方法来调用数据库，而不用再去写SQL语句了，ORM可以帮助我们翻译。

### 7.1 安装第三方模块

因为新版本的django默认采用的是mysqlclient这个库，而不是pymysql，所以我们先pip安装mysqlclient。

```shell
pip install mysqlclient
```

windows可能会安装失败，百度`mysqlclient wheel`，下载相应版本的wheel文件，然后pip本地安装即可。

> P.S. 如果想用pymysql也是可以的，只是可能编码有些问题。
>
> 修改的方式是在`__init__.py`中增加代码即可，然后后续操作就和 mysqlclient一样了。
>
> ![image-20220205125135006](Django.assets/image-20220205125135006.png)

### 7.2 ORM

ORM可以帮助我们做两件事：

- 增删改查数据库中的表（不用写SQL语句）【但数据库你得自己建】
- 操作表中数据，即增删改查表中记录（不用写SQL语句）

#### 7.2.1 创建数据库

- 启动MySQL服务（默认都是开的）

- 创建数据库（命令行create语句创建或Navicat Premium创建）

  ![image-20220205142951933](Django.assets/image-20220205142951933.png)

#### 7.2.2 django连接数据库

django连接数据库只需要在`settings.py`文件中配置连接参数即可。

1. 找到`DATABASES`字典（Django默认配置的是sqlite）

   ![image-20220205141553020](Django.assets/image-20220205141553020.png)

2. 我们按以下参数格式配置MySQL连接

   ```python
   'default': {
       'ENGINE': 'django.db.backends.mysql',	# Django的引擎，还可以用Oracle等
       'NAME': 'dbname',	# 数据库名
       'USER': 'root',		# 用户名
       'PASSWORD': 'xxx',	# 密码
       'HOST': '',			# 数据库服务器地址
       'PORT': 3306,		# 端口号（MySQL默认3306）
   }
   ```

3. 我们连接的是本地的MySQL，所以`HOST`是`localhost`或者`127.0.0.1`；数据库名和密码大家各自填自己的即可。

#### 7.2.3 django操作表

- 创建表
- 删除表
- 修改表

##### 增加表

在相应app中的models.py中写一个类就是创建一张表。

```python
# 在MySQL中创建对应的一个表
class UserInfo(models.Model):
    # 创建字段
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
```

ORM会帮我们把这个面向对象的代码转化成SQL（表名是`app名称_类名`），与上面代码对应的SQL大致为：

```mysql
create table index_userinfo(
    id bigint auto_increment primary key,		【django创建表自带自增字段】
    name varchar(32),
    password varchar(64),
    age int,
);
```

到terminal界面下执行命令，通过`manage.py`来让ORM读取我们写好的models.py中的代码。

```shell
python manage.py makemigrations
python manage.py migrate
```

注意：

1. 要确保当前python的环境下有mysqlclient（pymysql的话，记得在`__init__.py`那个文件加两行代码）
2. 执行命令要在manage.py所在文件位置执行
3. app必须提前注册好

刷新一下数据库，就可以看到很多django创建出来的表了。

![image-20220205205913503](Django.assets/image-20220205205913503.png)

生成表的原理是django去所有app的`models.py`中找需要创建的表，在`settings.py`中可以看到，有很多django默认自带的app，所以除了`index_userinfo`表，其他表都是django自带生成的表，我们暂先不用管。

![image-20220206130605391](Django.assets/image-20220206130605391.png)

如果还想新建表，就再在models.py里写类，然后执行那两个指令即可。然后刷新数据库就可以看到了。我们新建两个。

```python
class StudentInfo(models.Model):
    name = models.CharField(max_length=32)

class TeacherInfo(models.Model):
    name = models.CharField(max_length=32)
```

执行那两个命令。

![image-20220206135705174](Django.assets/image-20220206135705174.png)

可以看到数据库中已有新的表了。

![image-20220206135858507](Django.assets/image-20220206135858507.png)

##### 删除表

把`models.py`中类注释掉，然后再执行那两个指令即可删除表。我们删除`index_teacherinfo`表。

注释`index_teacherinfo`表对应的类

![image-20220206141614768](Django.assets/image-20220206141614768.png)

执行两条命令

![image-20220206141840155](Django.assets/image-20220206141840155.png)

查看表是否删除

![image-20220206142604967](Django.assets/image-20220206142604967.png)

##### 修改表

###### 增加字段

> 我们得先知道增加列的一些点：
>
> 1. 增加新列时，因为已存在列可能已有数据了，所以必须要给新列一个默认的值，不给的话django会提示信息
>    1. 在models.py中增加新列时，就声明默认值。（就是后面的选项 2）
>    2. 操作manage.py时，再设置。（就是后面的选项 1）
> 2. 如果在models.py中声明新列可以为空，那么django就不会提示信息了，会直接操作成功。
>
> 所以，我们下面会介绍==三种修改表的方法==。

修改表就是增删表中的字段，我们删除就直接注释，增加就直接加。比如我们对`index_userinfo`表进行操作。

首先先确认有几个字段

![image-20220206155927256](Django.assets/image-20220206155927256.png)

然后我们加一个`sex`字段，写好代码，然后执行两个指令。

![image-20220206160115103](Django.assets/image-20220206160115103.png)

可以看到，django给我们了两个选项，1是给一个默认值为增加的列赋值，2是取消这次操作，我们手动给新增加的列设置默认值。

![image-20220206163634569](Django.assets/image-20220206163634569.png)

这时，表中就会增加一个新列，并且默认值都是1。

![image-20220206164641588](Django.assets/image-20220206164641588.png)

接下来说选项2，我们再增加字段`nickname`

![image-20220206172145030](Django.assets/image-20220206172145030.png)

选2就会直接退出了，接下来我们手动设置默认值

![image-20220206172625613](Django.assets/image-20220206172625613.png)

操作成功，再看看数据库表

![image-20220206172707715](Django.assets/image-20220206172707715.png)

再来，我们直接声明可以为空就行。再增加字段`data`。

![image-20220206173353210](Django.assets/image-20220206173353210.png)

再看看表

![image-20220206173417360](Django.assets/image-20220206173417360.png)

###### 删除字段

删除字段就很简单了，不像增加字段会有限制，而是和删除表一样，注释掉，两条指令执行一下就行了。

![image-20220206174846120](Django.assets/image-20220206174846120.png)

![image-20220206174900799](Django.assets/image-20220206174900799.png)

###### 修改字段

直接改变量名即可，然后django会问你是否真的改，输入`y`即可。

![image-20220206175800709](Django.assets/image-20220206175800709.png)

##### 表内增删改查

前面说了，我们可以通过操作对象的方式，免去一大堆SQL语句，从而通过用django来操作表的结构。同样的，django还给我们提供了方法来操作表中的数据。这些方法是写在视图函数中的，调用相应`models.py`中的类即可，最后我们演示。

###### 增

语法：`类名.objects.create()`

```python
# insert into index_studentinfo(title) values("zm");
StudentInfo.objects.create(title="zm")
# insert into index_userinfo(name,password,age) values("gzh","123",18);
UserInfo.objects.create(name="gzh", password="123", age=18)
```

###### 删

语法：

- `类名.objects.filter().delete()`：筛选内容，再删除
- `类名.objects.all().delete()`：删除表内全部内容

```python
UserInfo.objects.filter(id=2).delete()	# 删除表中id为2的删除
StudentInfo.objects.all().delete()		# 删除表中所有内容
```

###### 改

语法：

- `类型.objects().all().update()`：修改全部
- `类型.objects().filter().update()`：筛选内容，再修改

```python
UserInfo.objects().all().update(password="123")		# 把表中password全改成123
UserInfo.objects().filter(id=2).update(password="1")	# 把表中id为2的那行数据的password改成1
```

###### 查

语法：

- `类名.objects.all()`：查询表中所有数据
- `类名.objects.filter()`：筛查相应的数据

注意：返回的数据都是一个`QuerySet`类型数据，可以理解为`List`，只是每个元素是一个对象罢了。

```python
all_data = UserInfo.objects.all()
for obj in all_data:
    print(obj.id, obj.name, obj.password, obj.age)
```

```python
# UserInfo.objects.filter(id=1)		# 获得一行数据，但是也是QuerySet的一个列表，只是只有一个元素
# 所以可以通过first()来取到第一个单独的元素
data = UserInfo.objects.filter(id=1).first()
print(data.id, data.name, data.password, data.age)
```

### 7.3 用户管理案例

先在`index_userinfo`添加几行数据

![image-20220206204025191](Django.assets/image-20220206204025191.png)

然后我们改写之前写过的`user_list.html`、对应的视图函数`user_list()`，用表格把`index_userinfo`的数据全渲染出来。

![image-20220206212434046](Django.assets/image-20220206212434046.png)

![image-20220206212448539](Django.assets/image-20220206212448539.png)

![image-20220206212520036](Django.assets/image-20220206212520036.png)

挺简单的，要不再来试试实现用户注册的功能，我们改写之前写过的`user_add.html`

![image-20220206215102439](Django.assets/image-20220206215102439.png)

![image-20220206215115470](Django.assets/image-20220206215115470.png)

然后，我们来测试一下。

![image-20220206215215059](Django.assets/image-20220206215215059.png)

![image-20220206215234289](Django.assets/image-20220206215234289.png)

可以看到，我们成功实现了增加功能，同理，条件筛选查找、删除都可以实现。

# Django web开发 Day2

接下来是在做一个系统的实践中学习一些新的点。这个系统呢，我们做的是员工管理系统。有些点说过了，就一下带过了。

## 1. 创建项目

![image-20220209012709651](Django.assets/image-20220209012709651.png)

把django默认创建的templates删除，以及`settings.py`中的`TEMPLATES["DIRS"]`修改成`[]`。

![image-20220209012819606](Django.assets/image-20220209012819606.png)

## 2. 创建app

前面说过了在terminal中输入指令`python manage.py startapp em_web`创建app。（app名随便取，这里叫`em_web`）

不过pycharm也提供了一个快捷方法：

![image-20220209013836738](Django.assets/image-20220209013836738.png)

然后在下方就可以看到类似于terminal的界面，唯一不同的是，省略掉了`python manage.py`，直接写后面的指令即可（也会有一些指令匹配显示）。

![image-20220209013937762](Django.assets/image-20220209013937762.png)

![image-20220209014154837](Django.assets/image-20220209014154837.png)

注册app：

![image-20220209014457550](Django.assets/image-20220209014457550.png)

## 3. ORM创建表结构

### 3.1 常见参数位

整理了一些model中字段名的常见参数：

- `max_length`：一般是`CharField()`中用，有关字符的一般都要带，字符的最大长度
- `verbose_name`：是用来注释字段名的，方便人家知道该字段是什么意思，而且如果调用django的admin模块来后台管理的话，字段名会自动替换成`verbose_name`
- `primary_key`：声明主键，主键是唯一且非空的，一般都是写`primary_key=True`，`=False`的话不写这个参数即可，不需要特意写`=False`
- `default`：默认值
- `max_digits`：`DecimalField()`用，规定数字最长是多少（不包括正负号）
- `decimal_places`：`DecimalField()`用，规定显示小数点后几位
- `null`&`blank`：声明该字段可以为空，组合使用，一般都是写`null=True, blank=True`，`=False`的话不写这个参数即可，不需要特意写`=False`；如果想知道blank和null有什么区别，详见这篇[博文](https://www.cnblogs.com/linkenpark/p/7484542.html)
- `choices`：添加django的约束，注意，给这个参数赋值时得用**元组**

### 3.2 创建表结构

![image-20220209022022461](Django.assets/image-20220209022022461.png)

### 3.3 设置表间关系

#### 3.3.1 一对多 ForeignKey

现在，我们得设置一个字段，让每个员工都有自己属于的部门。前面有数据库的笔记，就直接说了，不引导了，员工和部门之间是“多对一”的关系，所以在“多”的那个表设置外键。

> P.S. 一般表间联系都是用 id，而不是用名称这种的字段名。因为这样【节省存储开销】，id这种字段一般比其他字段所耗存储都要小。
>
> But，在一些比较大的公司，联系会直接用名称，因为大公司的某些数据表可能每天被查询上万上亿次，如果还仍采用 id的话，查询的时候得连表操作，速度较慢。【加速查找，允许有这种冗余】
>
> 我们自己写的小项目就用 id了。

> Q：不写外键行不行？直接声明一个整型字段，存部门 id。
>
> A：这样是不行的。因为这个关系是有约束的，部门 id必须是部门表内存在的 id，而不是乱填的。所以还是老老实实用外键。

在员工表中设置外键：`dep = models.ForeignKey(to="Department", to_field="id")`，注意生成表后，django会自动在此字段名后加上`_id`，所以实际表中的字段名是`dep_id`。

不过，这样设置的外键还不行，如果直接执行生成表的操作的话，会报错的。现在假设一个场景：部门表有一个部门被裁撤了，员工表中，原属于该部门的员工改怎么办？

不管？肯定是不行的，因为上面说到了，这个关系是有约束的，`dep_id`必须在部门表中存在此`id`，故肯定要对这个情况设置参数来调用相应的解决方案。

有许多解决方法：

- 删除关联的员工：一般叫**级联删除**，相应配置为`on_delete=models.CASCADE`
- 不删置为空：这样写，必须设置允许该字段可以为空，相应配置为`null=True, blank=True, on_delete=models.SET_NULL`

这里我们就设置级联删除：`dep = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)`

#### 3.3.2 添加django约束

上面我们说的是数据库的约束条件，其实django也可以添加约束条件，通过choices这个参数来添加的。

![image-20220209140531220](Django.assets/image-20220209140531220.png)

### 3.4 创建数据库

好了，接着我们用MySQL创建数据库或者navicat创建，前面说过navicat创建了，这里说MySQL命令行的创建方式

```mysql
# 先进mysql
mysql -u root -p
输入密码，回车确认
# 创建数据库
create databases 数据库名 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
# 查看是否有刚才创建的数据库
show databases;
```

修改django中的配置文件，连接MySQL

```python
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'dbname',
    'USER': 'root',
    'PASSWORD': 'xxx',
    'HOST': '127.0.0.1',
    'PORT': 3306,
}
```

> 如果没装 `mysqlclient`模块，记得在 `settings.py`同目录下的 `__init.py__`中添加代码：
>
> ```python
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

![image-20220209142119449](Django.assets/image-20220209142119449.png)

### 3.5 指令生成

Terminal执行两条指令生成表

```shell
python manage.py makemigrations
python manage.py migrate
```

或者在pycharm提供的那个界面写

```shell
makemigrations
migrate
```

![image-20220209142718624](Django.assets/image-20220209142718624.png)

> P.S. 当你没用mysqlclient时，如果报错：`django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.`，说明pymysql版本太低了，删除再安装就是新版的了，指令如下，在 Terminal中执行：
>
> ```shell
> pip uninstall pymysql
> pip install pymysql
> ```

mysql或navicat中查看表，之前展示的是navicat，这里用mysql来看。

```mysql
# 先进MySQL，前面以写，这里就不写了
# 进入相应数据库
use em_web;
# 展示所有表
show tables;
```

![image-20220209143056957](Django.assets/image-20220209143056957.png)

## 4. 静态文件的管理

先搞好static和templates

![image-20220209143528044](Django.assets/image-20220209143528044.png)

## 6. 部门管理

好了，接下来就开始功能实现了。

### 6.1 原始方法实现

#### 6.1.1 部门列表

##### 页面构思

先大体画一画页面的模样

![image-20220209144044645](Django.assets/image-20220209144044645.png)

##### 三要素

创建`dep_list.html`，撰写视图函数`dep_list()`，设置url

![image-20220209144411425](Django.assets/image-20220209144411425.png)

![image-20220209145921267](Django.assets/image-20220209145921267.png)

![image-20220209144541645](Django.assets/image-20220209144541645.png)

##### 构建页面

然后我们快速的通过bootstrap来构建页面的大体布局，从[Bootstrap组件](https://v3.bootcss.com/components)这里找需要的样式，添加进来修改。

![image-20220209150903009](Django.assets/image-20220209150903009.png)

修改好的导航栏代码（最好自己改好，不建议copy，这里只是给大家参考）：

```html
<nav class="navbar navbar-default">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Employee Manager</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active"><a href="/dep_list/">部门管理 <span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">登录</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">Dropdown <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

接着往下做，还得做个按钮和表格（面板+表格）。

![image-20220209152833465](Django.assets/image-20220209152833465.png)

相关代码为：

```html
<div class="container">
    <div style="margin-bottom: 10px">
        <a class="btn btn-success" href="#">
            <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
            新建部门
        </a>
    </div>
    <div class="panel panel-default">
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th" aria-hidden="true"></span>
                部门列表
            </div>
            <table class="table table-striped table-hover">
                <thead>
                <tr>
                    <th>部门ID</th>
                    <th>部门名称</th>
                    <th>操作</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>Mark</td>
                    <td>Otto</td>
                    <td>
                        <a class="btn btn-primary btn-xs">编辑</a>
                        <a class="btn btn-danger btn-xs">删除</a>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
</div>
```

然后也可以加一加注释，方便自己以后修改即可。

![image-20220209153032232](Django.assets/image-20220209153032232.png)

##### 加载数据

因为我们现在暂时没有数据，所以先手动往数据库里插入几条数据。

```mysql
insert into em_web_department(dep_name) values("IT部"),("销售部"),("运营部");
```

![image-20220209154302407](Django.assets/image-20220209154302407.png)

##### 完善视图函数

然后我们再完善视图函数，把数据库中的数据传到前端。

![image-20220209154410269](Django.assets/image-20220209154410269.png)

然后前端调用

![image-20220209154441199](Django.assets/image-20220209154441199.png)

数据就成功渲染到了前端了。

![image-20220209154640802](Django.assets/image-20220209154640802.png)

#### 6.1.2 部门添加

修改跳转连接，target是设置跳转的方式，默认是本页面跳转，`_blank`就是新建页面跳转。

![image-20220209155318172](Django.assets/image-20220209155318172.png)

设置url、视图函数、html文件三要素

![image-20220209160706034](Django.assets/image-20220209160706034.png)

因为`dep_add.html`有些东西和`dep_list.html`有些代码是重复的，所以我们复制过来。

代码先不展示，在下面一起展示。和`dep_list.html`一样，通过bootstrap官网组件，设置一个面板，面板中放一个表单。

```django
{% load static %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>【EmployeeManager】部门添加</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1-dist/css/bootstrap.css' %}">
</head>
<body>
<!-- 导航栏 -->
<nav class="navbar navbar-default">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Employee Manager</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active"><a href="/dep_list/">部门管理 <span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">登录</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">Dropdown <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
<!-- 主体部分 -->
<div class="container">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">
                <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                部门添加
            </h3>
        </div>
        <div class="panel-body">
            <form class="form-horizontal">
                <div class="form-group">
                    <label for="dep_name" class="col-sm-2 control-label">部门名称</label>
                    <div class="col-sm-8">
                        <input type="text" class="form-control" id="dep_name" name="dep_name" placeholder="请输入部门名称 Please Input DepartmentName">
                    </div>
                </div>
                <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                        <button type="submit" class="btn btn-success">添 加</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
<script rel="script" src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
<script rel="script" src="{% static 'plugins/bootstrap-3.4.1-dist/js/bootstrap.js' %}"></script>
</body>
</html>
```

![image-20220209164050327](Django.assets/image-20220209164050327.png)

接着我们完善视图函数，实现部门添加的功能

![image-20220209170036039](Django.assets/image-20220209170036039.png)

完善前端form表单

![image-20220209165542910](Django.assets/image-20220209165542910.png)

测试功能

![image-20220209170127619](Django.assets/image-20220209170127619.png)

![image-20220209170145471](Django.assets/image-20220209170145471.png)

再点“新建部门”，再添加试试

![image-20220209170225799](Django.assets/image-20220209170225799.png)

#### 6.1.3 部门删除

这个功能不需要跳转页面，点击`dep_list.html`中每行结尾的删除按钮就删除对应行的数据。

那问题来了，点`id=2`对应的删除，怎么让后台也知道`id=2`？很简单，前端页面跳转的时候，跳转链接增加`?id=2`后缀，通过GET方法传递数据。所以，我们得设置一个删除按钮的跳转链接。

![image-20220209184009601](Django.assets/image-20220209184009601.png)

![image-20220209172938522](Django.assets/image-20220209172938522.png)

此时，url还是正常写，不需要写`?`后面的路径匹配。

![image-20220209184412303](Django.assets/image-20220209184412303.png)

测试功能

![image-20220209184626498](Django.assets/image-20220209184626498.png)

![image-20220209184644100](Django.assets/image-20220209184644100.png)

点击谁，谁就会被删掉。

#### 6.1.4 部门编辑

编辑页面和添加页面很像，唯一不同的是，就是框里的内容应该有个默认值。所以，三要素先写好，html文件能copy过来的能copy过来。

再来，点击编辑按钮也得需要让前端告诉后端是修改谁的名称，然后后端跳转页面时，也得给前端传数据库中原始的名称。先完善前端跳转的链接。

![image-20220209190947422](Django.assets/image-20220209190947422.png)

再完善视图函数，这些都是`GET`请求响应的处理逻辑，所以我们写在`GET`中。然后还得想想`POST`请求，用户点击修改后，应该通过`POST`获取新名称，修改数据库的旧名称，再跳转`dep_list.html`页面。

![image-20220209192220449](Django.assets/image-20220209192220449.png)

But，你会发现这样写是不行的，第一次通过`GET`获取的id数据，在`POST`中是调用不到的，所以我们还得让前端传`POST`请求的时候，同时要传id和name两个数据，所以要写一个`input`，然后设置`type="hidden"`和`name`，然后在视图函数中，重新接收id信息。

![image-20220209200359763](Django.assets/image-20220209200359763.png)

![image-20220209200418839](Django.assets/image-20220209200418839.png)

测试功能

点击“编辑”按钮，跳转`dep_update.html`

![image-20220209200524616](Django.assets/image-20220209200524616.png)

修改，并提交

![image-20220209202011961](Django.assets/image-20220209202011961.png)

修改成功

![image-20220209202030356](Django.assets/image-20220209202030356.png)

再改回来也是可以的

![image-20220209202538358](Django.assets/image-20220209202538358.png)

不过，还有另一种传id的方式，就是直接写入url中。把`urls.py`中写入这么一句：

```python
# 访问链接'127.0.0.1:8000/dep/数字/update/'时触发
path('dep/<int:nid>/update/', views.dep_update)
# 不过，为了和update区分开，这里再写个edit，通过url来传递id，实现update同样的效果
path('dep/<int:nid>/edit/', views.dep_edit)
# P.S. django 1.x.x不支持此功能
```

与此url对应的视图函数，就必须带上`nid`这个参数了，不然我们后端无法调用这个参数。

```python
def dep_edit(request, nid):
	...
```

此时，前端跳转的链接就不用写`?`来传参了，之间跳转即可（这里再加一行`<a></a>`，区别开两个方式）。

![image-20220209210119614](Django.assets/image-20220209210119614.png)

新的视图函数逻辑也不同了。

![image-20220209210226890](Django.assets/image-20220209210226890.png)

![image-20220209205909421](Django.assets/image-20220209205909421.png)

接着就是写`POST`部分了，和之前一样的思路，就是id用参数nid即可，不需要再通过`POST`获取id了。

![image-20220209210649915](Django.assets/image-20220209210649915.png)

功能也都可以正常跑。

可以看到，这个思路和我们一开始说的错误很像，唯一区别就是一开始错误是在视图函数中声明一个变量存第一次`GET`发来的值，但是`POST`中调用时，无法调用；而这个把需要用`GET`发给后端的值，直接写入url中，把url当做一个中转站，`POST`调用的时候直接调用参数即可。

#### 6.1.5 模板的继承

##### 使用方法

6.1.1到6.1.4，我们写了三个页面，可以发现有很多代码都是重复的，一模一样。eg：导航栏、引入文件等代码都是重复的。所以我们可以将这些重复的模板代码，单独写到一个html中，然后其他html需要就调用即可。

首先，我们随便从写好的三个html文件中复制全部代码，新建`dep_base.html`，然后我们来看看哪些代码是可以不用变的（红框部分都可以不用变）。

![image-20220210210813126](Django.assets/image-20220210210813126.png)

> P.S. 这三个html实现的都是部门管理这个功能，所以导航栏的 `active`始终是“部门管理”那个 `li`标签，所以对于部门管理这部分的页面，可以共用这个导航栏，所以叫 `dep_base.html`。比如后面员工管理，导航栏的active就不是“部门管理”这个 `li`了，那我们可以换一个模板继承，比如修改出一个 `emp_base.html`。当然，你也可以把模板文件中，相同代码再继承，出一个 `base.html`，这样都是可以的。

然后我们就来学习继承的语法，首先将需要继承的部分不动，把不需要继承的地方换成这段代码：

```django
{# XXX是这个块的名字，子模板想要往哪加代码，就是通过名字来确定的 #}
{% block XXX %}{% endblock %}
```

![image-20220210211642871](Django.assets/image-20220210211642871.png)

然后，我们修改其他三个页面，删除其中与`dep_base.html`重复的代码，让那三个页面继承`dep_base.html`。

eg：`dep_list.html`我们就可以写成这样，只保留不同代码的部分，其他部分都删除。

![image-20220210212052359](Django.assets/image-20220210212052359.png)

同理，操作另外两个html文件。

![image-20220210212343030](Django.assets/image-20220210212343030.png)

![image-20220210212506981](Django.assets/image-20220210212506981.png)

我们再去前端看看，页面还是正常显示的，功能也都是正常跳转的。

![image-20220210212600230](Django.assets/image-20220210212600230.png)

和python的继承逻辑很像的，大家应该可以理解。

##### 模板继承的好处

模板继承是很灵活的，你可以定义多个block，给子模板添加东西，上面我们定义了title块给子模板修改页面标题，content块给子模板撰写自己的主体部分。

我们还可以定义css块，让子模板可以引入只有自己使用的样式；定义js块，让子模板引入自己使用的js，等等等等。大家可以自行按实际需求来写。

另外，如果你要对一些代码进行修改时，你可能需要把三个文件中的相应代码都要修改，而用了继承，你就只需要修改模板即可。eg：修改导航栏的布局。

##### 语法总结

```django
{# 定义块 #}
{% block XXX %}{% endblock %}

{# 继承语法 #}
{# 要写前面，先继承，再调用块；继承哪个html就写哪个 #}
{% extends 'XXXX.html' %}
{# 调用块，并写入代码 #}
{% block XXX %}		{# 调用XXX块，在XXX块中，写入... #}
	...		{# 写入的模板代码 #}
{% endblock %}
```

#### 6.1.6 员工管理

前面我们实现了部门管理，接下来我们就来接着实现员工管理。

##### 员工列表

和部门列表很像，我们先修改出一个`emp_base.html`，和`dep_base.html`就差一个导航栏的`active`不同。

![image-20220210223507434](Django.assets/image-20220210223507434.png)

![image-20220210223535034](Django.assets/image-20220210223535034.png)

好了，我们开始写`emp_list.html`，和`dep_list.html`很像，我们快速搭建，让大体页面先出来，有的东西就先注释不加。

![image-20220210224128040](Django.assets/image-20220210224128040.png)

```django
{% extends 'emp_base.html' %}

{# 页面标题 #}
{% block title %}
    <title>【EmployeeManager】员工列表</title>
{% endblock %}

{# 页面主体 #}
{% block content %}
    <div class="container">
        <div style="margin-bottom: 10px">
            <a class="btn btn-success" href="" target="_blank">
                <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                创建员工
            </a>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th" aria-hidden="true"></span>
                员工列表
            </div>
            <table class="table table-striped table-hover">
                <thead>
                <tr>
                    <th>员工ID</th>
                    <th>员工名称</th>
                    <th>操作</th>
                </tr>
                </thead>
                <tbody>
{#                {% for dep in dep_queryset %}#}
                    <tr>
                        <td>1</td>
                        <td>xxx</td>
                        <td>
                            <a class="btn btn-primary btn-xs" href="#">编辑</a>
                            <a class="btn btn-danger btn-xs" href="#">删除</a>
                        </td>
                    </tr>
{#                {% endfor %}#}
                </tbody>
            </table>
        </div>
    </div>
{% endblock %}
```

然后我们来看怎么渲染列表数据，这么多列的数据，我们一个一个写上去。

![image-20220210224526134](Django.assets/image-20220210224526134.png)

和`dep_list.html`一样，我们在数据库中插入一些数据再实现渲染功能。进入mysql，插入数据：

```mysql
use em_web;
# 查看表的字段名
desc em_web_employee;
# 查看有哪些可用的部门id
select id from em_web_department;
# 插入数据
insert into em_web_employee(name,password,age,account,create_time,gender,dep_id) values("zm","123",20,10000.23,"2000-09-28",1,1);
insert into em_web_employee(name,password,age,account,create_time,gender,dep_id) values("lx","abc",21,1000.64,"2020-08-29",1,3);
insert into em_web_employee(name,password,age,account,create_time,gender,dep_id) values("gzh","321",22,50000.98,"1999-09-27",1,4);
insert into em_web_employee(name,password,age,account,create_time,gender,dep_id) values("xcq","213",19,1000.98,"2010-07-2",2,1);
# 查看表中是否有数据
select * from em_web_employee;
```

插入完成

![image-20220210235658941](Django.assets/image-20220210235658941.png)

渲染就很简单了，参考部门列表的view写，这里就不说过程了，直接展示结果。

![image-20220210235753032](Django.assets/image-20220210235753032.png)

这里要提一下的是，入职时间这个数据。

![image-20220211000123424](Django.assets/image-20220211000123424.png)

![image-20220211000140042](Django.assets/image-20220211000140042.png)

可以看到，这里获取到的入职时间是datetime类型的数据，之前学习python模块那章时提过，把datetime类型数据转换成string是要用`strftime("%Y-%m-%d-%H-%M")`，我们只需要在前端显示年月日即可，所以`"%Y-%m-%d"`即可。

![image-20220211094321141](Django.assets/image-20220211094321141.png)

![image-20220211094334689](Django.assets/image-20220211094334689.png)

然后我们再调整员工性别，不能显示1和2，得显示对应的男和女，当时我们再models中用choice设置了，所以我们得用django的方法来调用，调用方法是`get_字段名称_display()`

![image-20220211095311862](Django.assets/image-20220211095311862.png)

![image-20220211095325125](Django.assets/image-20220211095325125.png)

再来，再改所属部门，可以想到代码怎么写：`Department.objects.filter(id=emp.dep_id).first()`，但是，django也给这个提供了外键操作方法：`emp.dep`，会把名为`dep`的那个外键，自动链表，返回外表中相应的那行数据。

> P.S. 注意：外键叫啥就写啥，不用加 `_id`，eg：这里的外键叫 dep，所以`emp.dep.dep_name`就可以获取部门名称了，而不是`emp.dep_id.dep_name`。

简而言之，`emp.dep`等价于`Department.objects.filter(id=emp.dep_id).first()`。所以我们通过`.`调用就可以获得所属部门名称了。

![image-20220211104702084](Django.assets/image-20220211104702084.png)

![image-20220211104709943](Django.assets/image-20220211104709943.png)

我们这样写就是在后端把数据格式调整好，再传到前端，也可以在前端实现数据格式的调整，但python语法和django模板语法是不同的，所以我们得改些代码。

![image-20220211105410869](Django.assets/image-20220211105410869.png)

![image-20220211105517358](Django.assets/image-20220211105517358.png)

可以看到，我们需要改两句。模板语法中，不允许加`()`，如果在python中需要加括号的，在模板语法中去掉就好。但是像时间这种括号里带参数的呢？怎么删括号？哎，模板语法中用`|`来写，而且Django模板改写了`strftime()`，封装成了`date`。

```django
{{ emp.create_time|date:"Y-m-d H:i:s" }}
```

我们只需要`"Y-m-d"`就行。

![image-20220211110028966](Django.assets/image-20220211110028966.png)

![image-20220211110119465](Django.assets/image-20220211110119465.png)

##### 员工新建

和部门添加功能实现过程一样，这样的原始方式就是马上用的django组件的原理。所以大家可以参考部门添加功能的实现，来写员工新建。

这里我们就点出几个点：

1. 新建的时候，每个输入框传入的数据都得判断非空，员工新建这么多栏信息，光写判断都麻烦死
2. 如果有错误，页面应该有一些错误提示
3. 如果需要改输入框，页面上每个字段可能都得重新写一遍
4. 关联的数据还得手动获取并手动循环展示在页面（Form组件解决不了，还得自己写点逻辑实现）

接着，我们就开始用Form组件和ModelForm组件来重新实现员工新建。

### 6.2 Form&ModelForm

django中提供了Form和ModelForm组件，可以帮助我们快速方便达到开发目标。其中，Form组件时比较简便的，ModelForm组件是最简便的。不过要理解ModelForm组件，得先理解Form组件，理解Form组件也得先理解原始方法实现的逻辑。

#### 6.2.1 Form概述

```python
# views.py
class MyForm(Form):
    {# widget=forms.Input表示在前端渲染成输入框 #}
    user = forms.CharField(widget=forms.Input)
    pwd = forms.CharField(widget=forms.Input)
    email = forms.CharField(widget=forms.Input)

def emp_add(request):
    """员工新建"""
    if request.method == "GET":
        form = MyForm()
        return render(request, "emp_add.html", {"form": form})
```

```django
{# emp_add.html #}
<form method="post">
    {{ form.user }}
    {{ form.pwd }}
    {{ form.email }}
</form>

{# 或者这么写 #}
</form>
    {% for field in form %}
        {{ field }}
    {% endfor %}
</form>
```

可以发现，MyForm里面的内容和models.py中数据表的代码很像，所以我们可以用ModelForm组件更简化代码。

#### 6.2.2 ModelForm概述

```python
# models.py
class Employee(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="员工姓名", max_length=16)
    password = models.CharField(verbose_name="员工密码", max_length=64)
    age = models.IntegerField(verbose_name="员工年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间", )

    # 添加django中的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="员工性别", choices=gender_choices)

    # 生成表时，django会生成dep_id字段而不是dep字段
    dep = models.ForeignKey(verbose_name="所属部门", to="Department", to_field="id", on_delete=models.CASCADE)
```

```python
# views.py
class MyForm(ModelForm):
	class Meta:
        model = EmployeeInfo
        # 想加什么字段，放在列表中即可
        fields = ["name", "password", "age"]

def emp_add(request):
    """员工新建"""
    if request.method == "GET":
        form = MyForm()
        return render(request, "emp_add.html", {"form": form})
```

```django
{# emp_add.html #}
</form>
    {% for field in form %}
        {{ field }}
    {% endfor %}
</form>
```

ModelForm对于那些操作数据表增删改查的功能，是最简便的方法，使用也不止上面这些方法，我们只是简单说一说。下面我们边实现功能，边学习ModelForm的更多使用方法。

#### 6.2.3 员工新建（ModelForm实现）

![image-20220211123321805](Django.assets/image-20220211123321805.png)

![image-20220211123459781](Django.assets/image-20220211123459781.png)

![image-20220211123519663](Django.assets/image-20220211123519663.png)

然后我们开始用ModelForm的逻辑来完善`views.py`。

![image-20220211213840957](Django.assets/image-20220211213840957.png)

![image-20220212132036919](Django.assets/image-20220212132036919.png)

那我们前面的中文怎么办？修改html文件，通过`.`运算，调用`label`，就可以通过ModelForm来显示`models.py`文件中相应字段名的`verbose_name`属性。

![image-20220212132418059](Django.assets/image-20220212132418059.png)

现在我们继续加输入框，继续完善views.py中的列表（`"gender","dep"`暂不添加）

![image-20220212132810547](Django.assets/image-20220212132810547.png)

然后前端就直接可以渲染出来了，不用再改任何东西。

![image-20220212132845047](Django.assets/image-20220212132845047.png)

接着，我们实现关联数据，来添加`gender`和`dep`外键

![image-20220212133020137](Django.assets/image-20220212133020137.png)

刷新页面

![image-20220212133108416](Django.assets/image-20220212133108416.png)

![image-20220212133126069](Django.assets/image-20220212133126069.png)

问题又来了，这个所属部门下拉选框里显示的怎么不是中文了，看意思是一个个的Department对象，在ModelForm的源码中，就是直接输出对象的，所以导致了这个下拉选框里显示的都是这样的。

那如何解决呢？在python学习面向对象时，我们介绍了几个双下划线的方法，其中有一个`__str__`的方法，是实现输出对象时所输出的内容。在这里，就可以解决这一问题了。

```python
class Foo(object):
    def __str__(self):
        return "haha"
obj = Foo()
print(obj)
```

在`models.py`中，为Department对象添加`__str__`方法，并指定输出对象时，返回“部门名称”。

![image-20220212134657922](Django.assets/image-20220212134657922.png)

刷新页面，即可。

![image-20220212134812317](Django.assets/image-20220212134812317.png)

所以，当我们在写`models.py`中的对象时，我们可以直接加上`__str__`，防止以后需要输出。

But，这个界面和`dep_add.html`上的输入框样式都不一样，我们可以对生成的input框添加样式嘛？答案是肯定可以的。我们找到`views.py`中员工新建的ModelForm类，其中添加`widgets`变量，在那里添加样式。

![image-20220212140130146](Django.assets/image-20220212140130146.png)

代码中，`TextInput()`就表示所有`type="text"`的input框，attrs参数就是传入的属性及属性值，eg：这里的`{"class": "form-control"}`就是让前端的input框的class属性`="form-control"`。

刷新页面，就可以看到页面上`type="text"`的input框样式变了。

![image-20220212140407920](Django.assets/image-20220212140407920.png)

同理，我们可以一个个的把不同type的输入框样式给它添加上去。

Input类型有这些：

![image-20220212140749725](Django.assets/image-20220212140749725.png)

我们按英文意思可以对应上`models.py`中不同的Field（eg：TextInput对应CharField）

![image-20220212141232804](Django.assets/image-20220212141232804.png)

![image-20220212141252807](Django.assets/image-20220212141252807.png)

但是，这样一个一个的添加样式，很麻烦，所以有个简单的方式：

![image-20220212141445183](Django.assets/image-20220212141445183.png)

刷新页面，可以在pycharm的run界面看到数据，django会根据Meta中的fields去`models.py`找

![image-20220212141525861](Django.assets/image-20220212141525861.png)

然后，我们可以直接在这个循环里加`attrs`就行了。

![image-20220212142757087](Django.assets/image-20220212142757087.png)

![image-20220212142823480](Django.assets/image-20220212142823480.png)

如果某些输入框的样式不想调整，还可以增加判断。

![image-20220212143124935](Django.assets/image-20220212143124935.png)

![image-20220212143136282](Django.assets/image-20220212143136282.png)

当然，其他样式都是可以加的哈，比如我们加一个`placeholder`，后端和前端一样，通过label把`models.py`的`verbose_name`调用过来。

![image-20220212143451835](Django.assets/image-20220212143451835.png)

![image-20220212143606193](Django.assets/image-20220212143606193.png)

下面就来实现post请求了，也是用ModelForm的方法来实现。

![image-20220212152747819](Django.assets/image-20220212152747819.png)

调用我们定义好的ModelForm，把前端POST传来的数据传进ModelForm；ModelForm封装了校验代码，我们调用`is_valid()`方法即可，它的返回值是Boolean类型，我们可以和if组合使用。如果是True，就可以通过cleaned_data属性查看数据；如果是False，就可以调用errors属性查看报错信息。

![image-20220212154913801](Django.assets/image-20220212154913801.png)

ModelForm还提供了写入数据库的封装方法：`save()`，我们`is_valid()`为True时，就得把`cleaned_data`写入数据库。

But，我们通过`save()`方法就可以实现了，不需要再通过`object.create()`去写入数据库了。直接来看看是否能正常插入。

![image-20220212155419017](Django.assets/image-20220212155419017.png)

![image-20220212155409903](Django.assets/image-20220212155409903.png)

> P.S. 可能大家会问，那 ModelForm怎么知道插入到哪个表上？其实是知道的，我们写 ModelForm类的时候就指定了一个 model的参数，传入了相应的 models.py中的对象。

我们再来完善，将报错显示在前端，提高前端交互效果。

![image-20220213122029244](Django.assets/image-20220213122029244.png)

ModelForm很方便，直接传新建的ModelForm对象即可，然后在前端`.`调用`errors`，从而显示报错信息。因为一个输入框可能有多个报错，所以`emp_add_form.errors`ModelForm源码返回的是一个列表格式数据，我们一般只取第一个报错信息显示，所以前端我们得写成`emp_add_form.errors.0`

![image-20220213122339409](Django.assets/image-20220213122339409.png)

开始测试报错信息，比如我们不输入数据，直接提交

![image-20220213004221151](Django.assets/image-20220213004221151.png)

如果如上图显示，是浏览器自带的，我们把它关掉，然后再测试

![image-20220213004303812](Django.assets/image-20220213004303812.png)

![image-20220213122514298](Django.assets/image-20220213122514298.png)

可以正常显示报错信息了，ModelForm也会帮我们显示在相应输入框的报错信息，极大程度方便了开发。我们再加一个样式，可以更好一些。当然，还有一些其他类型的报错信息，比如我们给name加上一个约束（在ModelForm中也能加）。

![image-20220213123317492](Django.assets/image-20220213123317492.png)

![image-20220213123456977](Django.assets/image-20220213123456977.png)

不过，这些报错信息都是英文，对于中文用户，比较的不友好，我们在django的settings.py中，设置语言为`'zh-hans'`。

![image-20220213123644319](Django.assets/image-20220213123644319.png)

![image-20220213123741447](Django.assets/image-20220213123741447.png)

好了，至此，ModelForm的相关内容就大致到这，接下来我们再用它来实现员工的编辑和删除。

#### 6.2.4 员工删除

因为删除不用输入框，也不用新界面，所以很容易，和`dep_del()`一样，很好写。类比`dep_del()`和`dep_list.html`完善一下`emp_list.html`和`emp_del()`即可实现。

```python
# urls.py
path('emp_del/', views.emp_del),

# views.py
def emp_del(request):
    """员工删除"""
    emp_del_id = request.GET.get("emp_del_id")
    Employee.objects.filter(id=emp_del_id).delete()
    return redirect("/emp_list/")
```

```django
<a class="btn btn-danger btn-xs" href="/emp_del/?emp_del_id={{ emp.id }}">删除</a>
```

#### 6.2.5 员工编辑

步骤分析：

- 点击编辑，跳转页面
- 编辑页面（根据id获取数据，并将默认值显示在前端）
- 获取前端数据，校验
- 更新数据库

我们先把url搞好，保证可以跳转页面。

```django
{# emp_list.html #}
<a class="btn btn-primary btn-xs" href="/emp/{{ emp.id }}/update/">编辑</a>

{# urls.py #}
path('emp/<int:nid>/update/', views.emp_update),
```

```python
# views.py
def emp_update(request, nid):
    """员工编辑"""
    return render(request, "emp_update.html", {})
```

测试一下跳转的url变的是否符合逻辑，这里就不截图了。然后我们开始完善`views.py`，和`emp_add()`的GET代码逻辑完全一样，先复制一个新ModelForm（可以不用，后面再说）。

![image-20220213200259311](Django.assets/image-20220213200259311.png)

![image-20220213200236294](Django.assets/image-20220213200236294.png)

然后前端页面也是和`emp_add.html`一样的，把主体部分copy过来，把相应的部分改一下即可。

![image-20220213201939438](Django.assets/image-20220213201939438.png)

但默认值怎么设置呢？可能想到了之前`dep_update()`时，在前端设置input框的value属性即可完成默认值的显示。

But，ModelForm也提供了相关方法来显示默认值。首先我们根据id获取数据库中相应的那行值（QuerySet类型数据），然后通过ModelForm提供的`instance`参数传入数据，ModelForm就会默认把传入的那个对象展示到前端了。

![image-20220213203041349](Django.assets/image-20220213203041349.png)

刷新页面，即可看到效果。

![image-20220213203100462](Django.assets/image-20220213203100462.png)

接着，再来实现post部分，和之前员工新建时的逻辑一样。

![image-20220215152253475](Django.assets/image-20220215152253475.png)

此时，我们来试试功能。

![image-20220215152850228](Django.assets/image-20220215152850228.png)

![image-20220215152907117](Django.assets/image-20220215152907117.png)

这个修改，完全不符合我们的预期，这个修改更像是添加。在ModelForm中，如果要让`save()`不是另外的去创建，而是修改数据表中的某行值，我们还是要在创建`EmpUpdateForm`对象时，传入`instance`参数，让ModelForm知道，是改哪一行的值。

![image-20220215153255780](Django.assets/image-20220215153255780.png)

再来测试

![image-20220215153326432](Django.assets/image-20220215153326432.png)

![image-20220215153338853](Django.assets/image-20220215153338853.png)

写到这，我们对代码做一些优化。可以发现，get和post都用到了`Employee.objects.filter(id=nid).first()`这句代码，所以我们可以提到最前面。

![image-20220215153949808](Django.assets/image-20220215153949808.png)

再来看我们创建的两个ModelForm的对象，可以看到他们是一样的代码，所以两个视图函数可以共用一个ModelForm的，只要他们链接的数据表是一个，我们就可以只用一个ModelForm。所以我们就修改一下对象名，供`emp_add(request)`和`emp_update(request, nid)`调用即可。

![image-20220215154208379](Django.assets/image-20220215154208379.png)

> P.S. save()方法会把前端用户输入的数据，把偶才能到数据库中。但假设一个场景，前端传入两个数据，数据库一行得要三个参数，剩一个参数是后台给一个默认值和前端的两个数据一起写入数据库。
>
> 这时，我们怎么在后端传入数据呢？可以引用 instance参数，手动赋值进去即可（不过这个字段名是必须得在数据表中存在的哦！）。
>
> ![image-20220215165928863](Django.assets/image-20220215165928863.png)

还需要优化的就是，创建时间的格式问题，因为我们只需要显示年月日即可，不需要显示小时分钟秒，所以ModelForm展示的默认数据后面所带的`00:00`我们想去掉的话，得改`models.py`，原因是数据库表设计的时候不合理，把`create_time`的`DateTimeField()`改成`DateField()`，然后两句指令跑一下，刷新页面即可。

### 6.3 条件搜索

我们现在想在列表页面上加上一个搜索框的功能。

![image-20220215171646639](Django.assets/image-20220215171646639.png)

#### 6.3.1 所用知识点

暂定通过员工姓名来检索结果，可以很容易想到，我们得用models的`filter()`来做。

`filter()`远比我们之前使用的功能要多，它还支持字典设置条件。

```python
search_dict = {
    "name": "zhuming",
    "dep": "IT部",
}
models.Employee.objects.filter(**search_dict)

# 等同于
models.Employee.objects.filter("name": "zhuming", "dep": "IT部")
```

不过，条件不只是要判断`=`，大于小于那些也有相应的语法：

```python
# 数字的一些符号
id=12	# id=12的筛选出来
id__gt=12	# id>12的筛选出来
id__gte=12	# id>=12的筛选出来
id__lt=12	# id<12的筛选出来
id__lte=12	# id<=12的筛选出来

search_dict = {
    "id__lte": 12,
}
models.Employee.objects.filter(**search_dict)
```

```python
# 字符串的一些符号
phone = "17732101234"	# phone = "17732101234"的筛选出来
phone__startswith="177"	# "177"开头的筛选出来
phone__endswith="1234"	# "1234"结尾的筛选出来
phone__contains="321"	# 包含"321"的筛选出来

search_dict = {
    "phone__contains": "12",
}
models.Employee.objects.filter(**search_dict)
```

#### 6.3.2 实现功能

懂了这些过后，我们开始做这个功能。先完善一下页面，搞一个搜索框出来。

![image-20220215175856821](Django.assets/image-20220215175856821.png)

该部分前端代码如下：

```html
<div style="float: right; width: 300px">
    <form method="get">
        <div class="input-group">
            <label for="search"></label>
            <input type="text" id="search" name="search" class="form-control" placeholder="请输入员工姓名 支持模糊查询">
            <span class="input-group-btn">
                <button class="btn btn-default" type="submit">
                    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
                </button>
            </span>
        </div>
    </form>
</div>
```

接着完善一下视图函数。

![image-20220215180807050](Django.assets/image-20220215180807050.png)

这样就可以了，然后红线划去的部分是`order_by("id")`，就是让QuerySet数据按`id`升序排列，如果想降序就加一个`-`，eg：`order_by("-id")`。

我们就可以测试功能了。（eg：模糊搜索包含z的名字）

![image-20220215182129392](Django.assets/image-20220215182129392.png)

![image-20220215182141922](Django.assets/image-20220215182141922.png)

不输入，直接搜索。

![image-20220215182215569](Django.assets/image-20220215182215569.png)

可以看出，有个缺点，输入框点击搜索后就清空了，用户很容易忘了自己是搜什么的，所以，后端传递参数时，多传一个；前端再设置input框的value值。然后自己测一测即可。

```python
return render(request, "emp_list.html", {"emp_queryset": emp_data, "search_data": search_data})
```

```django
<input type="text" id="search" name="search" class="form-control" value="{{ search_data }}" placeholder="请输入员工姓名 支持模糊查询">
```

此时，你会发现，一开始输入框显示None了，所以我们要给他赋值一个空字符串，不能不管（None就是因为不管才出现的），所以完善一下代码：

![image-20220215210451929](Django.assets/image-20220215210451929.png)

### 6.4 分页显示

#### 6.4.1 所用知识点

和切片很像，就是不会越界（如果QuerySet的列表不够10个数据，它不会报错，而是有几个就输出几个）。

```python
# filter和all都可以
Employee.objects.all()	# 获取全部数据
Employee.objects.all()[0:10]	# 获取前10条数据
```

我们先增多数据（放进视图函数`emp_list()`中，刷新一遍页面就注释掉，只需要增多100个就可以了）

```python
for i in range(100):
    Employee.objects.create(name="test"+i, password="12", age=10, account=0, create_time="2000-09-28", gender=1, dep=1)
```

#### 6.4.2 实现功能

还是和搜索一样，通过get来获取page参数，page若获取不到，就默认是1；然后用切片来

![image-20220215203702220](Django.assets/image-20220215203702220.png)

然后我们手动测试，修改网址的page参数，看看是否实现分页显示了。

![image-20220215204414467](Django.assets/image-20220215204414467.png)

![image-20220215204804379](Django.assets/image-20220215204804379.png)

下面我们就得找一找合适的bootstrap分页标签，然后放在页面中。

```html
<!-- bootstrap 分页 -->
<ul class="pagination">
    <li><a href="#" aria-label="Previous"><span aria-hidden="true">«</span></a></li>
    <li class="active"><a href="?page=1">1</a></li>
    <li><a href="?page=2">2</a></li>
    <li><a href="?page=3">3</a></li>
    <li><a href="?page=4">4</a></li>
    <li><a href="?page=5">5</a></li>
    <li><a href="#" aria-label="Next"><span aria-hidden="true">»</span></a></li>
</ul>
```

![image-20220215205323340](Django.assets/image-20220215205323340.png)

这个`href`写`?page=1`时，点击它就会默认给当前url后面加上`?page=1`，然后访问。但是这样太死板了，我们这里不止5页的数据啊，我们得后端传值告诉前端有多少页，完善一下`emp_list()`。

![image-20220215210831449](Django.assets/image-20220215210831449.png)

但是，这样是不行的，我们得给前端从`1`到`page_num`的列表，而不是`page_num`，不然前端循环没办法写。

![image-20220215211208330](Django.assets/image-20220215211208330.png)

最终视图函数的代码是：

![image-20220215211428422](Django.assets/image-20220215211428422.png)

前端写一个循环渲染

![image-20220215211249421](Django.assets/image-20220215211249421.png)

前端就好了，点击也可以点击进去，但是问题又来了，如果现在是1w条数据，我们这个页码全渲染出来就会很占地方，所以我们还得改。

![image-20220215211451421](Django.assets/image-20220215211451421.png)

这个就有很多解决思路了，比如用下拉框来写（移动端用的较多），不过PC端比较常用的方法是显示当前页面的前`x`条和后`y`条页码。`x`和`y`是自己决定的。其实啊，不管是显示前后多少页，说到底都是把`page_num`这个参数控制好。eg：我们来做`x=2`，`y=7`的情况。（这里为什么要写x和y而不直接写数据呢？是为了后期改成函数，方便多个视图函数调用）这里的`ifelse`判断得慢慢写，还得注意`range()`取前不取后的特点。

![。image-20220215215008965](Django.assets/image-20220215215008965.png)

![image-20220215215509170](Django.assets/image-20220215215509170.png)

![image-20220215215456387](Django.assets/image-20220215215456387.png)

然后我们写上下页的逻辑

![image-20220215221450605](Django.assets/image-20220215221450605.png)

![image-20220215221500595](Django.assets/image-20220215221500595.png)

#### 6.4.3 封装调用

因为我们这里要封装`views.py`中分页的代码，为了统一，这里给出分页实现代码：

```python
def emp_list(request):
    """员工管理"""
    # 搜索
    search_filter = {}
    search_data = request.GET.get("search")
    if search_data:
        search_filter["name__contains"] = search_data
    else:
        search_data = ""

    # 直接实现
    # 获取get传来的page
    page_str = request.GET.get("page")
    # 如果用户未输入page参数，默认为1
    if page_str:
        page = int(request.GET.get("page"))
    else:
        page = 1
    page_max_item = 10  # 一页最多多少行数据
    start = (page - 1) * page_max_item  # 切片开始位
    end = page * page_max_item  # 切片结束位

    emp_data = Employee.objects.filter(**search_filter).order_by("id")
    total = emp_data.count()  # 数据总量
    emp_data = emp_data[start:end]

    # 页码
    page_num = int(total / page_max_item)
    if total % page_max_item:
        page_num += 1

    # 前2页，后7页
    x = 2
    y = 7
    if page <= x:
        pre_list = range(1, page)
    else:
        pre_list = range(page-x, page)

    if page > page_num-y:
        next_list = range(page+1, page_num+1)
    else:
        next_list = range(page+1, page+y+1)
    
    return render(request, "emp_list.html", {
        "emp_queryset": emp_data, "search_data": search_data,
        "pre_list": pre_list, "next_list": next_list,
        "now_page": page, "pre": page-1, "next": page+1, "page_max": page_num
    })
```

还有一个输入框跳转指定页的功能，我们没有实现，但逻辑和条件搜索的逻辑一模一样。接下来，我们要把这一大堆代码封装，这样我们以后需要实现分页这个功能时，直接调用就行了，不需要再写这么一大堆代码。

![image-20220225130751742](Django.assets/image-20220225130751742.png)

我们先创建`utils`文件夹（按照规范，我们自己封装的工具一般都要放在`utils`文件夹中），再创建py文件封装我们的分页工具类，我们这里命名为`pagination.py`。

我们先简单封装一下，设置几个参数。

![image-20220225131024104](Django.assets/image-20220225131024104.png)

然后改写`views.py`中`emp_list()`函数，调用我们的Pagination对象来实现分页。

```python

```

开始测试，发现报错`AttributeError: 'int' object has no attribute 'isdecimal'`，定位报错地点是`pagination.py`。经分析，一开始访问`emp_list`页面时，`now_page`通过`get`获取不到当前页，默认为1，是int类型，如果直接进if判断，int类型是没有`isdecimal()`的方法的，所以报错。两个方法：

1. 保证`now_page`是str类型，用`str(now_page)`处理
2. 增加if判断分支

这里我们增加if分支来解决

![image-20220225132602536](Django.assets/image-20220225132602536.png)

然后页面就可以正常显示了，不过还有问题

![image-20220225134450444](Django.assets/image-20220225134450444.png)

这个没关系，我们完全封装好了之后再改。现在要来思考一件事，如何让这个分页组件可以更灵活，比如可以自由选择是否有“首尾页跳转”、是否有“form跳转部分”。而且不知道大家发现了没有，我们为了一个分页传了太多的参数了。

![image-20220225135439655](Django.assets/image-20220225135439655.png)

我们换个思路，我们在Pagination对象中，把前端代码写好，然后最终只传一个HTML代码至前端，这样不光可以方便自由选择分页的部分功能，也可以减少往前端传的参数。基于这个思路，我们再继续封装。

```python
# pagination.py
from django.utils.safestring import mark_safe	# django为了安全会默认拒绝渲染后端的html代码，所以我们需要mark_safe()给html代码标记为安全，才可以在前端渲染


class Pagination(object):
    """自定义分页组件"""

    def __init__(self, request, temp_name_param, queryset, page_form_method="get",
                 page_size=10, nex=5, prev=5, form_switch=False, first_switch=False,
                 last_switch=False, a_next=False, a_prev=False):
        # form跳转页码的name值
        self.temp_name_param = temp_name_param
        # 获取当前页
        if page_form_method == "post":
            # 通过POST获取当前页，默认为1
            now_page = request.POST.get(temp_name_param, 1)
        else:
            # 通过GET获取当前页，默认为1
            now_page = request.GET.get(temp_name_param, 1)

        # 是否是数字
        if now_page == 1:
            pass
        elif now_page.isdecimal():
            now_page = int(now_page)
        else:
            # 不是数据就默认为1
            now_page = 1

        # 当前页
        self.now_page = now_page
        # 每页显示数
        self.page_size = page_size
        # 数据总量
        self.total = queryset.count()
        # 切片开始位
        self.start = (now_page - 1) * page_size
        # 切片结束位
        self.end = now_page * page_size
        # 对ORM从数据库中拿到的数据进行切片，获得当前页面所对应的数据
        self.page_queryset = queryset[self.start:self.end]
        # 总页数
        self.page_num = int(self.total / self.page_size)
        if self.total % self.page_size:
            self.page_num += 1

        # 显示当前页的前多少页
        self.nex = nex
        # 显示当前页的后多少页
        self.prev = prev

        # 组件调用
        self.form_switch = form_switch  # 是否显示 form跳转页码 组件
        self.first_switch = first_switch  # 是否显示 首页跳转 组件
        self.last_switch = last_switch  # 是否显示 尾页跳转 组件
        self.a_next = a_next  # 是否显示 上一页跳转 组件
        self.a_prev = a_prev  # 是否显示 下一页跳转 组件

    def page_form(self):
        """ 添加form部分的html代码
        :return: (str）form部分的html代码
        """
        return f'''
            <li>
                <form method="get" style="float: left;">
                    <label for="page"></label>
                    <input id="page" name="{self.temp_name_param}"
                           style="border-radius: 0; float: left; display: inline-block; margin-left: -1px; width: 80px"
                           type="text" class="form-control" placeholder="页码">
                    <button type="submit" style="-moz-border-radius-topleft: 0; -moz-border-radius-bottomleft: 0;
                           margin-left: -5px" class="btn btn-default">跳转</button>
                </form>
            </li>
        '''

    @staticmethod
    def page_first():
        """ 添加首页页码的html代码
        :return: （str）html代码
        """
        return '<li><a href="?page=1">首页</a></li>'

    def page_last(self):
        """ 添加尾页页码的html代码
        :return: （str）html代码
        """
        return f'<li><a href="?page={self.page_num}">尾页</a></li>'

    def page_next(self):
        """ 添加下一页的html代码
        :return: （str）html代码
        """
        if self.now_page == self.page_num:
            html = '<li class="disabled"><a href="#" aria-label="Next"><span aria-hidden="true">»</span></a></li>'
        else:
            html = f'<li><a href="?page={self.now_page + 1}" aria-label="Next"><span aria-hidden="true">»</span></a></li>'
        return html

    def page_prev(self):
        if self.now_page == 1:
            html = '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'
        else:
            html = f'<li><a href="?page={self.now_page - 1}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'
        return html

    def basic(self):
        """ 生成基础的html代码
        :return: （str）html代码
        """
        nex_html = ""
        if self.now_page <= self.nex:
            nex_list = range(1, self.now_page)
        else:
            nex_list = range(self.now_page - self.nex, self.now_page)
        for page in nex_list:
            nex_html += f'<li><a href="?page={page}">{page}</a></li>'

        now_html = f'<li class="active"><a href="?page={self.now_page}">{self.now_page}</a></li>'

        prev_html = ""
        if self.page_num - self.now_page <= self.prev:
            prev_list = range(self.now_page + 1, self.page_num + 1)
        else:
            prev_list = range(self.now_page + 1, self.now_page + self.prev + 1)
        for page in prev_list:
            prev_html += f'<li><a href="?page={page}">{page}</a></li>'

        return nex_html + now_html + prev_html

    def html(self):
        """ 生成全部的html
        :return: (str) html代码
        """
        html = ""
        if self.first_switch:
            html += self.page_first()
        if self.a_prev:
            html += self.page_prev()
        html += self.basic()
        if self.a_next:
            html += self.page_next()
        if self.last_switch:
            html += self.page_last()
        if self.form_switch:
            html += self.page_form()

        return mark_safe(html)
```

```python
# views.py
def emp_list(request):
    """员工管理"""
    # 搜索
    search_filter = {}
    search_data = request.GET.get("search")
    if search_data:
        search_filter["name__contains"] = search_data
    else:
        search_data = ""
    # 搜索条件筛选从数据库拿的数据
    emp_data = Employee.objects.filter(**search_filter).order_by("id")

    # 分页
    # 封装对象实现
    from em_web.utils.pagination import Pagination
    pagination = Pagination(request, "page", emp_data, page_form_method="get", page_size=10)

    return render(request, "emp_list.html", {
        "emp_queryset": pagination.page_queryset, "search_data": search_data, "page_html_string": pagination.html()
    })
```

```django
{# emp_list.html部分代码 #}
<ul class="pagination">
    {{ page_html_string }}
</ul>
```

可以自己测试，是符合逻辑的（默认显示前5页和后5页）。

然后我们对参数进行配置，自由搭配组件。

```python
pagination = Pagination(request, "page", emp_data, page_form_method="get", page_size=10, nex=3, prev=4, first_switch=True, last_switch=True, form_switch=True, a_next=True, a_prev=True)
```

![image-20220225224546893](Django.assets/image-20220225224546893.png)

可以看出，原本`views.py`中大段的代码，已经被我们封装至`utils`中了，`views.py`一下变得清爽了许多，而且以后我们需要实现分页的效果时，直接创建对象调用方法即可，还能应对各种场景下的需求，对组件进行增删。

But，如果你的页面中其他地方没有form表单，那么这个Pagination就够用了，不幸的是，我们这个页面有其他的form表单，就是右上角的搜索框，如果你先搜索一个值，在点击分页的按钮，我们会发现，原本的搜索条件失效了。也就是说，如果我们想解决这个Bug，我们就得把除开分页的form表单的条件数据都带着，然后一起去跳转其他分页。

```shell
# 我们原来是这样跳转
127.0.0.1:8000?page=1 -> 127.0.0.1:8000?page=3
# 但如果有其他的form表单的条件数据，就产生了Bug
127.0.0.1:8000?search=zm&page=1 -> 127.0.0.1:8000?page=3	# 错误！
# 按照正确的逻辑，应该是这样（所以一定要带着其他form表单的数据一起跳转其他分页）
127.0.0.1:8000?search=zm&page=1 -> 127.0.0.1:8000?search=zm&page=3	# 正确！
```

这里要解决这个问题，我们先说一个知识点：

```python
# 加到视图函数中，然后访问相应的页面
print(request.GET)	# 会获取所有的get传来的数据
print(request.GET.urlencode())	# 将get获取到的数据再转化成url中的格式
```

我们访问`http://127.0.0.1:8000/emp_list/?search=z&page=2`

![image-20220225231121324](Django.assets/image-20220225231121324.png)

可以看到，`request.GET`返回的是一个QueryDict的一个数据类型，这个数据类型是不允许手动增加参数的。但是通过阅读完源码后，我们可以修改默认参数来实现允许手动增加参数。But，如果直接修改默认参数的话，不是很安全，所以我们copy一份，再修改它的默认参数，因为我们只需要让跳转链接里有数据即可。

![image-20220226024257960](Django.assets/image-20220226024257960.png)

再访问上面的链接，会发现输出会不同。

![image-20220226024439546](Django.assets/image-20220226024439546.png)

通过这个知识点，我们就可以来完善Pagination了。

![image-20220226034619679](Django.assets/image-20220226034619679.png)

![image-20220226034630505](Django.assets/image-20220226034630505.png)

![image-20220226034701527](Django.assets/image-20220226034701527.png)

![image-20220226034754959](Django.assets/image-20220226034754959.png)

![image-20220226034801987](Django.assets/image-20220226034801987.png)

![image-20220226035008319](Django.assets/image-20220226035008319.png)

最终，我们测试一下效果，都是可以的。不过，可能细心的你发现，form页码跳转还是不会携带search的参数。

这个问题呢，这里无法避免。如果要实现的话，得用Ajax或者js来做，如果不怕麻烦的话，可以手动写input框，设置`type`为`hidden`，然后添加进后端的html代码中，从而实现某个参数的携带。所以呢，这里就不考虑这个问题了。

好的，那么接下来，我们再实现部门管理的分页显示。

```python
# views.py
def dep_list(request):
    """部门列表"""
    # 获取数据库中数据
    all_dep_data = Department.objects.all()  # QuerySet(<对象>, <对象>, ...)
    pagination = Pagination(request, "page", all_dep_data, page_form_method="get", page_size=2, nex=3, prev=4,
                            first_switch=True, last_switch=True, form_switch=True, a_next=True, a_prev=True)
    return render(request, "dep_list.html", {
        "dep_queryset": pagination.page_queryset,
        "page_html_string": pagination.html()
    })
```

```django
{# dep_list.html #}
<ul class="pagination">
    {{ page_html_string }}
</ul>
```

很方便吧。

### 6.5 时间选择组件

这里我们调用的是bootstrap-datepicker插件，调用的语法如下：

```html
<link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1-dist/css/bootstrap.css' %}">
<!-- datepicker必须提前引入bootstrap的css -->
<link rel="stylesheet" href="{% static 'plugins/datepicker.css' %}">
<!-- 后面会利用id来写js -->
<input id="dt" type="text" class="form-control" placehorder="入职时间">

<script rel="script" src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
<script rel="script" src="{% static 'plugins/bootstrap-3.4.1-dist/js/bootstrap.js' %}"></script>
<!-- datepicker必须提前引入JQuery和bootstrap的js -->
<script rel="script" src="{% static 'plugins/bootstrap-datepicker.js' %}"></script>
<!-- 调用datepicker设置显示格式 -->
<script>
    $(function () {
        $('#dt').datepicker({
            format: 'yyyy-mm-dd',
            startDate: '0',
            language: 'zh-CN',
            autoclose: true,
        });
    })
</script>
```

我们用这个插件来完善一下我们的`emp_add.html`，因为我们是用ModelForm来生成的页面，所以我们怎么通过调用input框的id来实现插件呢？

其实，我们右击网页点检查，会发现，ModelForm在帮我们渲染前端输入框时，默认都会有一个id（命名格式：`id_+字段名`），所以我们直接用即可。

![image-20220226100129541](Django.assets/image-20220226100129541.png)

此时，我们点击创建时间，就可以通过日历快速选择日期了。

### 6.6 ModelForm样式优化

前面我们说ModelForm说过，ModelForm渲染在前端的输入框没有任何样式，需要我们通过widget来设置其属性及属性值。

![image-20220226101404116](Django.assets/image-20220226101404116.png)

然后我们又介绍了快速给所有输入框上样式的方法，通过`__init__()`去实现。

![image-20220226101634297](Django.assets/image-20220226101634297.png)

但是，现在我们再看这个方法，有些不严谨。如果输入框原本有一些样式的话，通过这段代码，不管你原本有无样式，`field.widget.attrs`都会给你定死成`"class": "form-control", "placeholder": field.label`。

所以我们要来完善一下逻辑。

![image-20220226101926888](Django.assets/image-20220226101926888.png)

But，如果以后我们用到ModelForm的话，我们这段代码得重复写。所以我们还可以将这个`__init__()`方法写到utils中去。

![image-20220226102559869](Django.assets/image-20220226102559869.png)

然后我们在`views.py`中需要写ModelForm的时候，就不去继承`forms.ModelForm`了，而是去继承`em_web.utils.bootstrap`中的BootstrapModelForm了。

![image-20220226102902911](Django.assets/image-20220226102902911.png)

这样，我们以后就不需要每次都继承`__init__()`方法去上样式了。