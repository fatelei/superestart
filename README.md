# superestart
A supervisord plugin used to autorestart program by specific time.

## Usage

```
[eventlistener:superestart]
command=superestart --crontab "0 1 * * *" --group_name foo
events=TICK
```