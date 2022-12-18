homework2
==============================

gasanov homework2 vk autumn 2022 MLOps bmstu

команда сборки Docker:
~~~
docker build -t gassanov/mlops:2.0 .
~~~

для того чтобы подтянуть из облачного хранилища
~~~
docker pull gassanov/mlops:2.0
~~~

запуск контейнера:
~~~
docker run --name rest_service -p 8000:8000 gassanov/mlops:2.0
~~~

запуск скрипта в контейнере:
~~~
cd homework2
make requests           
~~~
