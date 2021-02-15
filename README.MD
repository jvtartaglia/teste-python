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
        "email": "test@email.com",
    }

### Response

    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 35
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Mon, 15 Feb 2021 13:30:38 GMT

    {'Ok':' child/parent created sucessfully'}

## Create with relationship

### Request

`POST /api/parent`

    {
        "name": "Test",
        "email": "test@email.com",
        "child_id": [1, 2, 3, ...]
    }

`POST /api/child`

    {
        "name": "Test",
        "email": "test@email.com",
        "parent_id": [1, 2]
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
        {
            "id": 1,
            "name": "This is a test",
            "email": "test_email@server.com",
            "created_at": "2021-02-15 18:22:14.087695",
            "updated_at": "2021-02-15 18:22:40.367555"
        },

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
        {
            "id": 6,
            "name": "Some Child",
            "email": "some_child@email.com",
            "created_at": "2021-02-15 18:17:25.820599",
            "updated_at": "2021-02-15 18:18:44.726464"
        }
    }

## Get by count

### Request

`GET /api/parents?children=<integer>` 

`GET /api/children?parents=<integer>`


### Response

    HTTP/1.1 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 386
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Mon, 15 Feb 2021 13:38:12 GMT

    {
        {
            "id": 1,
            "name": "This is a test",
            "email": "test_email@server.com",
            "created_at": "2021-02-15 18:22:14.087695",
            "updated_at": "2021-02-15 18:22:40.367555"
        },

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