sunriseHour, sunriseMinutes = map(int, input().split())
sunsetHour, sunsetMinutes = map(int, input().split())

minutesSunrise = sunriseMinutes + sunriseHour * 60
minutesSunset = sunsetMinutes + sunsetHour * 60

sumTime = minutesSunrise + minutesSunset
averageTime = sumTime // 2

difference = (12 * 60) - averageTime

hour = abs(difference) // 60
minutes = abs(difference) % 60

if difference <= 0:
    print(hour, minutes)
elif hour != 0 and minutes != 0:
    print(f"-{hour} -{minutes}")
elif hour != 0:
    print(f"-{hour} {minutes}")
else:
    print(f"{hour} -{minutes}")
