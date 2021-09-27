# Django

### Apache2, wsgi 설치

```bash
$ sudo apt-get update
$ sudo apt install upgrade
$ sudo atp-get install apahce2
$ sudo apt install libapache2-mod-wsgi-py3
$ sudo service apache2 (start,stop,restart)

# 켜져있는지 확인
$ ps aux | grep apache2
# 패키지 설치 확인
$ dpkg -l | grep apache2
```



### demon 프로그램 확인

```bash
# demon 프로그램들이 있는 디렉토리
$ ls /etc/init.d

# 실행되고 있는 프로그램들
$ sudo service --status-all | grep +
```



### firewalld(선택)

```bash
$ sudo apt install firewalld -y

# 버전확인
$ sudo firewall-cmd --version

# 새로운 rule 적용
$ sudo firewall-cmd --permanent --zone=public --add-port=80/tcp
$ sudo firewall-cmd --reload
 
# 모든 값 조회
$ sudo firewall-cmd --list-all
```



### apt, apt-get 차이

> apt는 apt-get과 apt-cache의 기능 중에서 잘 사용되지 않는 기능을 제외하고 만든 새로운 tool이다. 여기서 apt-get은 패키지 설치를 담당하고, apt-cache는 패키지 검색을 담당하는 tool이다. 결론적으로 apt-get이 아닌 apt를 사용하는 것이 사용성 측면에서는 유리하다.

### 

### apache2, django 연동

ec2로 ubuntu 설치시 python3.8.5 가 설치되어있다.

- 가상환경 설치 

```bash
$ sudo apt-get install python3-venv -y
$ python3 -m venv venv
$ source venv/bin/activate
```



- apache2 설정 파일 수정

```bash
(venv) $ sudo apt install libapache2-mod-wsgi-py3
(venv) $ sudo vi /etc/apache2/sites-available/000-default.conf

# 수정
<VirtualHost *:80>

        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        #ErrorLog ${APACHE_LOG_DIR}/error.log
        #CustomLog ${APACHE_LOG_DIR}/access.log combined


        ErrorLog /home/ubuntu/todo/server/logs/error.log
        CustomLog /home/ubuntu/todo/server/logs/access.log combined

        <Directory /home/ubuntu/todo/server/mypjt/>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

		#python-path: 장고프로젝트 폴더 위치 / python-home:가상환경 venv 위치
        WSGIDaemonProcess server python-path=/home/ubuntu/todo/server python-home=/home/ubuntu/todo/server/venv
        WSGIProcessGroup server
        WSGIScriptAlias / /home/ubuntu/todo/server/mypjt/wsgi.py

		# admin 페이지 css 적용
        Alias /static/ /home/ubuntu/todo/server/venv/lib/python3.8/site-packages/django/contrib/admin/static/
        <Directory /home/ubuntu/todo/server/venv/lib/python3.8/site-packages/django/contrib/admin/static>
                Require all granted
        </Directory>

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>
```



- cors 에러 날시

```bash
# /etc/apache2/apache2.conf 추가하기
WSGIPassAuthorization On
```



### RDS(Mysql)

aws에서 rds 생성시 퍼블릭 액세스 허용 체크

```bash
# ubuntu mysqlclient 설치 후 rds 접속후 데이터베이스 생성
$ sudo apt update
$ sudo apt install mysql-server
$ mysql -u admin -p -h mysql-1.cxgaxmvbweba.us-east-1.rds.amazonaws.com

mysql> create database movies;
mysql> create user 'jaehong'@'%' identified by 'woghd2816!';
mysql> grant all privileges on movies.* to 'jaehong'@'%';
mysql> show grants for 'jaehong'@'%';
mysql> flush privileges;

# 밑에 설치로 안되면 그다음 설치할 것
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
$ pip install mysql-client

$ sudo aptinstall libmysqlclient-dev
$ sudo apt install python3-mysqldb
$ sudo apt-get install gcc -y


# django 프로젝트의 settings.py 파일 수정
DATABASES = {
          'default': {
             # 'ENGINE': 'django.db.backends.sqlite3',
              'ENGINE': 'django.db.backends.mysql',
             # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
              'NAME':'movies',
              'USER':'jaehong',
              'PASSWORD':'woghd2816!',
              'HOST':'mysql-1.cxgaxmvbweba.us-east-1.rds.amazonaws.com
',
              'PORT':'3306',
              'OPTIONS':{
                  'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
              },
          }
      }  
```

- apache 실행

```bash
$ python3 -m manage migrate
$ sudo service apache2 restart
```





# Vue

git clone 받은후 프로젝트 최 상단 위치에 .env.local 파일 생성

```bash
# .env.local
VUE_APP_SERVER_URL='http://52.69.127.109:80'
```



- nginx 설치

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install nginx
```

- nginx 설정 파일 수정

```bash
$ sudo vi /etc/nginx/sites-available/default

server {
        listen 80 default_server;
        listen [::]:80 default_server;


        root /var/www/html/dist;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files $uri $uri/ /index.html;
        }
}
```

- npm 설치 후 빌드

```bash
$ sudo apt install npm

# vue 프로젝트 폴더에서 npm run build 명령어를 통해 빌드 파일 생성
# dist 파일을 /var/www/html/ 폴더안으로 이동

$ sudo service nginx restart
```

