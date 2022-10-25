# django

- 路由
- 路由分发
- 模板
- ORM
  - 增删改查
    - save()
    - delete()
    - objects.all()
    - objects.get(pk=x)

---

- 注册路由

- 注册APP

- 注册模板 templates

- 继承模型

- render 渲染方法

  - request
  - 页面模板

  - context 上下文 数据传递 键值存储

---

## 数据库

- 注册数据库
  - ENGINE = 'django.db.backends.mysql', 
  - NAME, 
  - USER, PASSWORD, 
  - HOST, PORT

- 驱动

  - mysqlclient

  - pymysql
  - pymysql.install_as_MySQLdb() # 在\__init__.py

- 迁移

  - python manage.py migrate

- 

## pycharm 常用快捷键

- Alt + Enter
- Ctrl + p： 参数提示