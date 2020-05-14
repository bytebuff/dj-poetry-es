# django + es 实现唐诗宋词搜索引擎
通过django和elasticsearch实现的对大约311860首唐诗宋词的搜索引擎，主要使用了一下技术以及依赖：
- docker
- elasticsearch
- django
- djangorestframe
- vue
- semantic-ui

## 启动方式
1. 新建虚拟环境（当然也可以不新建）
    python3 -m venv env
    . env/bin/activate
2. 数据库迁移
    python manage.py makemigrations
    python manage.py migrate
3. 数据填充
    把古诗数据填充进数据库：
    python manage.py shell
    from poems.models import Poem
    Poem().populate()
4. 创建es索引
    python manage.py search_index --rebuild
5. 启动
    python manage.py runserver
6. 查看
    在浏览器: 127.0.0.1:8000 查看