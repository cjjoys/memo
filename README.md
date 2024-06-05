# memo
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=anuraghazra)](https://github.com/anuraghazra/github-readme-stats)

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


------------------------------------
최신: 1.28
릴리스 날짜: 2023년 9월 20 일
지원 종료: 2024년 12월 4일 †
지원되는 운영 체제: UBUNTU_20_64, UBUNTU_18_S390X


1.27
릴리스 날짜: 2023년 5월 24 일
지원 종료: 2024년 8월 14일 †
지원되는 운영 체제: UBUNTU_20_64, UBUNTU_18_S390X, UBUNTU_18_64

기본값: 1.26
릴리스 날짜: 2023년 2월 1 일
지원 종료: 2024년 4월 24일 †
지원되는 운영 체제: UBUNTU_20_64, UBUNTU_18_S390X, UBUNTU_18_64




