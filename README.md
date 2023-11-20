# SEP-Med
此项目旨在开发一个安全评估平台，用户可以使用此平台对软件进行安全评估，并获得一份安全评估报告，报告的内容包括安全评估场景、安全评估指标以及各项指标的分数。
## 主要功能
  - 用户的登录与注册。
  - 侧边栏功能，包含任务管理，场景管理，指标管理。
  - 任务管理功能：管理员可以创建任务，查看任务，删除任务，对任务进行模糊搜索，一个任务可以生成一个评分报告，管理员可以更改每个指标的分数，以及；普通用户只能查看任务和搜索任务。
  - 场景管理：管理员可以创建场景，查看场景，删除场景，对场景信息进行修改，对场景进行模糊搜索；普通用户只能查看场景和搜索场景。
  - 指标管理：管理员可以创建指标，查看指标，删除指标，对指标信息进行修改，对指标进行模糊搜索；普通用户只能查看指标和搜索指标。

## 开发工具
- [VS-Code](https://code.visualstudio.com/download)

## 开发环境
- 使用 Anaconda 创建 ```python==3.11``` 的开发环境 ```dj_py311``` 
  - ```conda create -n dj_py311 python==3.11```
- 激活 ```dj_py311```
  - ```conda activate dj_py311```
- 安装 Django
  - ```python -m pip install Django```
- 安装 pandas
- 安装 numpy
- 安装 jinja2
- 安装 bs4
  - ```pip install pandas numpy jinja2 beautifulsoup4```

## 部署环境
  ### Anaconda
  - 需要在本地安装[Anaconda](https://www.anaconda.com/)
  - 使用```environment.yml```创建开发环境
   ```bash 
  conda env create -f environment.yml
  ```
  ### Docker
  - 在项目运行前，需要先在Docker上开启mysql容器


## 本地部署 ```MySQL``` 数据库
  - 依赖 docker 与 docker-compose
    - [docker](https://docs.docker.com/engine/install/) 与 [docker-compose](https://docs.docker.com/compose/install/) 安装
  - 上述工具安装成功后，进入 mysqlv57 文件夹，依次执行下面的命令即可启动MySQL
    - ```mkdir {data,etc,logs,my.cnf}```
    - ```docker-compose -f docker-compose.yml up```
  - 本地即开启了 MySQL 服务，登录认证用户名为 ```root```，密码为 ```sep2023@```
  - 部署成功后会看到下面的图
![MySQL](images/mysqlconfig.png)

## 运行
  - 修改```SEP_Med_Web/setting.py``` 修改数据库配置，如下所示：
    ``` python 
    DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.mysql",
          "HOST": "127.0.0.1",
          "PORT": "3307",
          "NAME": "SoftEvaPlt",
          "USER": "root",
          "PASSWORD": "sep2023@",
      }
    }
  (这里的端口号默认是3306，正如docker-compose.yml文件里一样，但是如果本地已经安装过mysql，那么3306号端口就会被mysql占用，所以我这里改成3307映射本地3306端口，当然也可以结束本地3306的进程，将这里的端口号写成3306)
  
### 创建数据库
  mysql数据库中，在SoftEvaPlt数据库中导入```SoftEvaPlt.sql```文件，表会自动创建。
  在终端下执行：
    ``` 
        python manage.py makemigrations \
        python manage.py migrate  ```

  系统会自动构建django框架需要的表。
### vscode终端运行项目
  执行：
  ``` bash 
      python manage.py runserver
  ```
  浏览器打开: http://127.0.0.1:8000/auth/login 就可以进行登录和注册了。

## 时间安排
| 任务 | 开始时间 | 结束时间 | 交付结果 |进度|
|:-|:-:|:-:|:-|:-|
|数据库表结构设计与实现|2023/11/02|2023/11/05|包含表结构的sql文件|Done|
|前端页面设计与开发|2023/11/02|2023/11/12|前端结果展示|Done|
|系统功能与组件开发|2023/11/02|2023/11/12|系统开发源代码|Done|
|联调测试与交付|2023/11/12|2023/11/14|开发文档及源代码|Done|
