# GIỚI THIỆU PROJECT

Đây là [project][pj-url] xây dựng website để quản lí một phòng mạch tư. Hỗ trợ việc nhập, xuất và xem xét dữ liệu một cách nhanh chóng và thuận tiện cho các phòng mạch có quy mô nhỏ với từ 1-2 nhân viên và lượng khách từ 30-40 người / ngày.\
Project còn là đồ án môn học NMCNPM lớp 19_22/HCMUS với sự đóng góp của các thành viên:

- Nguyễn Minh Phúc (19120119)
- Trần Mỹ Hân (19120217)
- Tạ Võ Anh Khuê (19120551)
- Nguyễn Minh Long (19120568)
- Phạm Văn Nam (19120597)
  
# MÔI TRƯỜNG THỰC THI

[![py-image]][py-url]
[![django-image]][django-url]
[![vscode-image]][vscode-url]
[![db-image]][db-url]

Environments:

- [Python <3.10][py-url]

Code-editor:

- [VSCode][vscode-url]

Dependencies:

- [Django <= 4.0.4][django-url]
- [Django-database (default: SQLite)][db-url]
- [django-filter==21.1][dj-filter-url]
- [shortuuid==1.0.9][suuid-url]

Deployment:

- [Heroku-site][heroku-url]
- [Heroku-CLI][heroku-cli-url]

Deployment dependecies:

- [whitenoise==6.0.0][wn-url]
- [gunicorn==20.1.0][gu-url]

# HƯỚNG DẪN CẤU HÌNH PROJECT TRÊN LOCAL PC

> Yêu cầu: đã cài đặt Python <3.10 / môi trường có hỗ trợ Python <3.10

Download [Project][pj-url] .zip từ github hoặc clone project về local với lệnh git:

```git
git clone https://github.com/PhmNm/ClinicWeb_SEProject_HCMUS.git
```

Cài đặt các Package và Library cần thiết:

```terminal
cd ClinicWeb_SEProject_HCMUS

pip install -r requirements.txt
```

Trong trường hợp không có ý định deploy trên Heroku thì chỉ cần cài đặt các thư viện Django, django-filter và shortuuid:

```terrminal
pip install django==4.0.4 django-filter==21.1 shortuuid==1.0.9
```

Sau khi cài đặt các gói cần thiết, chạy lệnh sau để khởi động server:

```terminal
python3 manage.py runserver
```

Nếu trên terminal hiện yêu cầu migrate thì ngắt server bằng lệnh Ctrl + C và thực hiện lệnh migrate sau đó khởi động server:

```terminal
python3 manage.py migrate

python3 manage.py runserver
```

Vào trình duyệt và mở localhost ở port :8000 là đã có thể thao tác với web trên localhost: [127.0.0.1](http://127.0.0.1:8000/)

# HƯỚNG DÃN DEPLOY LÊN HEROKU

> Vì Heroku ngưng hỗ trợ deployment thông qua github nên cần cài đặt [Heroku CLI][heroku-cli-url] để deployment từ local lên Heroku

Yêu cầu: đã tạo tài khoản Heroku \
Các bước cài đặt và authorize bằng Heroku CLI: [Heroku CLI][heroku-cli-url]
Tạo app mới với CLI (sau khi đã log in):

```terminal
heroku create clinic-web-project
```

Remote đến app đã tạo với git:remote như sau:

```terminal
heroku git:remote -a clinic-web-project
```

Để tránh git đang remote đến app ở github hay nơi khác, ta kiểm tra bằng lệnh:

```terminal
git remote
```

Nếu trong remote tồn tại các remote khác, ta chạy lệnh sau để xoá:

```terminal
git remote remove [name-of-remote]
```

Cần cài đặt các dependecies whitenoise và gunicorn để hỗ trợ deploy lên Heroku
> Nếu đã thực hiện cài tất cả gói trong requirements.txt trên thì không cần thực hiện bước dưới đây

```terminal
pip install whitenoise==6.0.0 gunicorn==20.1.0
```

Sử dụng Code editor để:

- Tạo file requirements.txt như trong repositories chứa các dependencies đã sử dụng trong project để Heroku nhận diện
- Tạo file runtime.txt chứa thông tin môi trường sử dụng. Với project hiện tại:

```file content
python-3.9.6
```

- Nếu trong quá trình deploy xảy ra lỗi buildpack (lỗi về environment), ta vào settings của app trên website để add buildpack vào app (add Python)
- Tạo Procfile chứa nội dung như sau:

> Lưu ý: Profile không có đuôi filetype

```file content
web: gunicorn clinic_web.wsgi --log-file -
```

Sau đó vào app trên website và chọn Open app ở bên phải màn hình để lấy link mà website sau khi deploy sẽ sử dụng, ở đây là:

```webste
https://clinic-web-project.herokuapp.com/
```

Mở file settings.py và thực hiện một số thay đổi sau:

- Thêm các host vào ALLOWED_HOST:

```file content
ALLOWED_HOSTS = ['clinic-web-project.herokuapp.com','127.0.0.1']
```

- Thêm STATIC_ROOT:

```file content
STATIC_ROOT = BASE_DIR / 'web_core/staticfies'
```

- Thêm whitenoise middleware vào MIDDLEWARE ngay sau Security Middleware:

```file content
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
```

- Thêm shortuuid vào INSTALLED_APP

```file content
INSTALLED_APPS = [
    ...
    'web_core',
    'django_filters',
    'shortuuid',
]
```

Thêm vào .gitignore các file/folder thừa không hỗ trợ cho việc deploy, ví dụ: pycache, virtual-environment,...

Sau khi thực hiện các bước trên, thực hiện kiểm tra git trước khi add và commit bằng lệnh "git status"

Nếu thông tin trên git status không có gì sai sót ta thực hiện add và commit

```terrminal
git add .

git commit -m "First commit"
```

Kiểm tra lại git lần nữa bằng "git status" để chắc chắn trước khi push. Thực hiện push bằng lệnh

```terrminal
git push heroku master
```

# LINK DEMO

> NOT HAVE YET

# CURRENT STATUS

Đã hoàn thành các yêu cầu trong [Yêu cầu đồ án][ycda-url]

# FUTURE WORKS

Bổ sung các chức năng:

- Đặt khám online
- Tư vấn trực tuyến
- Mở rộng quy mô trang web dựa trên quy mô phòng mạch

[py-image]: https://img.shields.io/badge/Python-%3C3.10-green
[py-url]: https://www.python.org/downloads/release/python-396/
[django-image]: https://img.shields.io/badge/Django-4.0.4-green
[django-url]: https://docs.djangoproject.com/en/4.0/
[dj-filter-url]: https://django-filter.readthedocs.io/en/stable/index.html
[suuid-url]: https://github.com/skorokithakis/shortuuid
[Vscode-image]: https://img.shields.io/badge/vscode-x64-green
[vscode-url]: https://code.visualstudio.com/
[db-image]: https://img.shields.io/badge/Django--database-SQLite-green
[db-url]: https://docs.djangoproject.com/en/4.0/intro/tutorial02/#:~:text=By%20default%2C%20the%20configuration%20uses,else%20to%20support%20your%20database.
[heroku-url]: https://heroku.com/
[heroku-cli-url]: https://devcenter.heroku.com/articles/heroku-cli
[wn-url]: http://whitenoise.evans.io/en/stable/
[gu-url]: https://gunicorn.org/
[pj-url]: https://github.com/PhmNm/ClinicWeb_SEProject_HCMUS
[ycda-url]: https://drive.google.com/file/d/1QRFuxP6xEDBku2tr9FxRY4xV9YSZ012J/view
