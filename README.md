# u13 url shortener

Simple URL shortener

## Run the server locally
````bash
$ flask run --reload
 * Serving Flask app 'u13'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
````

## Creating users for the stats page

Create an admin user with password _admin123_:

````bash
echo "admin:admin:$(python -c 'from werkzeug.security import generate_password_hash; print(generate_password_hash("admin123"))')" >> instance/users.txt
````

This assumes the _instance_ directory already exists, it will be auto-created when the server is running

## Add a link and access it

````bash
$ http POST http://localhost:5000/short/add_link url='https://github.com/martineg/u13'
HTTP/1.1 200 OK
Connection: close
Content-Length: 64
Content-Type: application/json
Date: Fri, 07 Jun 2024 13:33:25 GMT
Server: Werkzeug/3.0.3 Python/3.12.3

{
    "short_url": "3610ba2",
    "url": "https://github.com/martineg/u13"
}

$ http GET http://localhost:5000/short/3610ba2
HTTP/1.1 302 FOUND
Connection: close
Content-Length: 249
Content-Type: text/html; charset=utf-8
Date: Fri, 07 Jun 2024 13:34:26 GMT
Location: https://github.com/martineg/u13
Server: Werkzeug/3.0.3 Python/3.12.3

<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="https://github.com/martineg/u13">https://github.com/martineg/u13</a>. If not, click the link.
````

## Show statistics

````bash
$ http GET http://localhost:5000/short/stats --auth admin:admin123
HTTP/1.1 200 OK
Connection: close
Content-Length: 48
Content-Type: application/json
Date: Fri, 07 Jun 2024 13:35:47 GMT
Server: Werkzeug/3.0.3 Python/3.12.3

{
    "stats": {
        "https://github.com/martineg/u13": 3
    }
}
````
