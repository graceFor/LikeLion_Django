# Model & Admin

1. Models.py 안에 어떤 종류의 데이터를 처리할지 class로 정의

2. DB에게 알려줘야함

   <img src="./img/스크린샷 2020-07-22 오후 5.51.25.png" width="40%" height="30%"> </img>

   - python manage.py makemigrations
   - python manage.py migrate

3. admin 계정 생성
   - python manage.py createsuperuser
   - 그 후에 admin.py에 데이터 등록

-> 데이터베이스에 어떻게 생긴 데이터를 넣을지 정의하고, 거기에 admin 권한으로 데이터 집어넣기
