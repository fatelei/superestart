# superestart
A supervisord plugin used to autorestart program by specific time.

## Usage

```
[eventlistener:superestart]
command=superestart --crontab "0 1 * * *" --group_name foo --api_endpoint "127.0.0.1:9009"
events=TICK_5
```