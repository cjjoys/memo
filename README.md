# memo


e# memo

#log 관련 설정

# Logs are managed by logrotate on Debian
logfile_rotate 10

debug_options ALL,6
buffered_logs on

logformat common     %>a %[ui %[un [%{NOW::%Y-%m-%d %H:%M:%S}tl] "%rm %ru HTTP/%rv" %>Hs %<st %Ss:%Sh
logformat combined   %>a %[ui %[un [%{NOW::%Y-%m-%d %H:%M:%S}tl] "%rm %ru HTTP/%rv" %>Hs %<st "%{Referer}>h" "%{User-Agent}>h" %Ss:%Sh

logformat squid      %ts.%03tu %6tr %>a %Ss/%03>Hs %<st %rm %ru %[un %Sh/%<a %mt
logformat referrer   %ts.%03tu %>a %{Referer}>h %ru
logformat useragent  %>a [%tl] "%{User-Agent}>h"

access_log /app/squid/logs/access.log logformat=combined
cache_log /app/squid/logs/cache.log


git remote add origin https://github.com/cjjoys/testw.git
git branch -M main
git push -u origin main





