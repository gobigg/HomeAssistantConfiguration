#!/bin/bash
SET_AGENT="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"
SET_URL="https://www.accuweather.com/en/se/stockholm/314929/minute-weather-forecast/314929"

weather_alert () {

curl -A "$SET_AGENT" -s $SET_URL | \
                        sed -n '/<!-- Summary -->/{n;p;n;p;n}' | \
                        tail -1 | sed  's/<p>/ /' | sed  's/<\/p>/ /' | grep -oE "[A-Z].*"
}

weather_alert

curl 'https://app.dfreeeze.de/users/login.json' -H 'Cookie: undefined_lastselected_car=16190; undefined_lastselected_page=%2Fcars%2Fview%2F16190%23carsViewStatus; isabella.alstrom%40gmail.com_lastselected_car=16190; timestamp_lastviewed_status_car_16190=2018-09-05%2012%3A36%3A12; isabella.alstrom%40gmail.com_lastselected_page=%2Fcars%2Fview%2F16190; CAKEPHP=6nlksoj2th7sss8h9um2rd1853' -H 'Origin: https://app.dfreeeze.de' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://app.dfreeeze.de/users/login' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'data%5BUser%5D%5Bemail%5D=isabella.alstrom%40gmail.com&data%5BUser%5D%5Bpassword%5D=Ziggy0hon' --compressed