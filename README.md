# xennanews
Newsservers (aka Usenet servers) hosted at Xennanews


# trigger

```
$ telnet news.caiway.nl nntp
Trying 91.223.220.18...
Connected to news.kabelfoon.nl.
Escape character is '^]'.
200 Welcome to news.caiway.nl NNTPSwitch-SVN-811, 85144 groups available, posting allowed, slot 55, connections 1
quit
205 Exit articles 0, bytes 0, groups 0, posts 0, postbytes 0
```

So news.caiway.nl points to 91.223.220.18 ... which is ...

```
$ host 91.223.220.18
18.220.223.91.in-addr.arpa domain name pointer vip18.xennanews.com.
```

... vip18.xennanews.com. Let's try if vip19.xennanews.com exists:

```
$ telnet vip19.xennanews.com nntp
Trying 91.223.220.19...
Connected to vip19.xennanews.com.
Escape character is '^]'.
200 Welcome to Cambrium NNTPSwitch-SVN-811, 77143 groups available, posting allowed, slot 239, connections 1
quit
205 Exit articles 0, bytes 0, groups 0, posts 0, postbytes 0
Connection closed by foreign host.
```

So, yes, and it is meant for "Cambrium"

If so, let's find out which other usenet servers aka newsservers are hosted by Xennanews.

# Method

First create a list like:

```
vip1.xennanews.com
vip2.xennanews.com
vip3.xennanews.com
vip4.xennanews.com
vip5.xennanews.com
vip6.xennanews.com
vip7.xennanews.com
vip8.xennanews.com
vip9.xennanews.com
vip10.xennanews.com
vip11.xennanews.com
vip12.xennanews.com
vip13.xennanews.com
vip14.xennanews.com
vip15.xennanews.com
vip16.xennanews.com
vip17.xennanews.com
vip18.xennanews.com
vip19.xennanews.com
...
```

Then feed then into a newsserver checker

```
python tellertje.py | awk '{ print "./newsserver_check.py " $1 }'  | /bin/sh | grep -vi "not OK"  | sed -e 's/200 //g' | sed -e 's/ NNTPSwitch-SVN.*//'  | grep -vi afo013 > xennanews-superclean2.txt
```


