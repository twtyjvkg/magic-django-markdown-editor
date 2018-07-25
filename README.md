magic django markdown editor
===

**magic-django-markdown-editor**

magic django markdown editor 是一个神奇的 [Django](http://www.djangoproject.com) markdown编辑器。

它是基于[editormd](http://pandao.github.io/editor.md)开发的。

* Projet Home: https://markdown.xuzhao.xin
* Author: [xuzhao](https://www.xuzhao.xin)
* Email: twtyjvkg@outlook.com

License
===

Apache License 2.0

Version
===

* v1

  * v1.0
  
    将editormd集成到django中，写成组件的形式
    
  * v1.1
  
    修复全屏显示的bug
    
安装和配置
===

* 使用pip命令安装

  ```python
  pip install pip install magic-django-markdown-editor
  ```
  
* 在django项目的配置文件settings.py的INSTALLED_APPS中添加xuzhao.markdown

  ```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'pagedown',
    'haystack',
    'blog',
    'accounts',
    'comments',
    'feedback',
    'compressor',
    'books',
    # 添加markdown编辑器
    'xuzhao.markdown'
    ]
  ```
  
* 在form中使用markdown编辑器

  * 普通form
  
    ```python
    from xuzhao.markdown.widgets import MarkdownWidget
    class FeedBackPostForm(forms.Form):
    body = forms.CharField(widget=MarkdownWidget())
    ```
    
  * Admin form
  
    ```python
    from xuzhao.markdown.widgets import AdminMarkdownWidget
    class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=AdminMarkdownWidget())
    ```



