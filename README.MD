# Python Flask API 

## Clone the repo

    git clone https://github.com/jvtartaglia/teste-python.git

## 'cd' into Root/ directory

    cd ./teste-python/Root/

## Run

    docker-compose up -d --build

# Static routes

### Default page

`/` 


   
    Parent/Child API v1.0

### Static folder page

`/static` 


   
    Use essa pasta para sincronizacao em tempo real com arquivos fora do container
    
    O volume e montado no diretorio default /var/lib/docker/volumes


# REST API

The REST API to the example app is described below.

## Create

### Request

`POST /api/parent` 

`POST /api/child`

    {
        "name": "Test",
        "email": "test@email.com"
    }

### Response

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 35
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Mon, 15 Feb 2021 13:30:38 GMT

    {'Ok':' child/parent created sucessfully'}

## Update

### Request

`PUT /api/parent/<id>` 

`PUT /api/child/<id>`

    {
        "name": "Another Test", # optional
        "email": "another_email@email.com" # optional
    }

### Response

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 35
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Mon, 15 Feb 2021 13:36:40 GMT

    {'Ok':' child/parent updated sucessfully'}


## Get all

### Request

`GET /api/parents` 

`GET /api/children`


### Response

    HTTP/1.1 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 386
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Mon, 15 Feb 2021 13:38:12 GMT

    {
        ...
    }



## Get by id

### Request

`GET /api/parent/<id>` 

`GET /api/child/<id>`


### Response

    HTTP/1.1 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 169
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Mon, 15 Feb 2021 13:40:27 GMT

    {
        ...
    }


## Delete

### Request

`DELETE /api/parent/<id>` 

`DELETE /api/child/<id>`


### Response

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 35
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Mon, 15 Feb 2021 13:42:11 GMT

    {'Ok':' child/parent deleted sucessfully'}