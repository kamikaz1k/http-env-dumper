# http-env-dumper
Exposes ENV vars via HTTP requests

Use it to explore your remote cloud environment, because docs are too hard.

## How to use
Run commands from makefile

Make HTTP requests to get env variables

get from docker hub

### Examples:

```
curl localhost:9090
> {"HOME":"/root","HOSTNAME":"a0782241125e","LANG":"C.UTF-8","LISTEN_PORT":"80"}

curl localhost:9090/HOME
> {"HOME":"/root"}

curl localhost:9090/HOMe
> {"HOMe":null}
```
