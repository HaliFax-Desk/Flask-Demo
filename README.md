在构建Flask应用中遇到的小问题 

我的第一个Flask应用是使用ChatGPT写出来的

本地搭建遇到很多小毛病，基本都是本地的问题（ChatGPT真的好强）

①本地Flask需要安排好目录树，如果你使用Pycharm构建应用的话直接选就行，会自动安排好

```text
├── app.py
├── static
│   └── style.css
├── templates
│   └── index.html
└── uploads 
```

- `app.py`：包含 Flask 应用的主要代码。
- `static/`：包含应用程序使用的静态文件（例如 CSS、JavaScript 和图像文件）。
- `templates/`：包含应用程序使用的 HTML 模板。
- `uploads/`：用于存储上传的文件。

② index.html索引HTML需要放在templates文件夹下，app.py才能访问到

③ 在app.py下设置好了：`@app.route('/',`这个代表你的根目录在app.py目录下

④ 当Flask显示

​		`filenotfounderrorfilenotfounderror: [Errno 2] No such file or directory: ''`

​	的时候，有很大可能是你的from表单没有完全填好，然后提交上去

​	这个会导致你的第一个参数OK，返回成功，第二个参数不OK，返回Error

