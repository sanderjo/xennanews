Looks like a completely different server: different 200-response, and IPv6-enabled:
```
$ host news.xennanews.com
news.xennanews.com has address 94.232.116.114
news.xennanews.com has IPv6 address 2001:67c:174:101::1002
```
and

```
$ telnet news.xennanews.com 119
Trying 2001:67c:174:101::1002...
Connected to news.xennanews.com.
Escape character is '^]'.
200 Welcome to xennanews
quit
205 Bye. 26 bytes written, 0 accounted.
Connection closed by foreign host.
```
