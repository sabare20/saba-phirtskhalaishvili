week_temp=((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))
mon_temps=week_temp[0]
mon_temps_avg=sum(mon_temps)/len(mon_temps)
print(f'mon_temps_avg={mon_temps_avg}')
print(f'mon_temps_max={max(mon_temps)}')
print(f'mon_temps_min=min(mon_temps)')
tu_temps=week_temp[1]
tu_temps_avg=sum(tu_temps)/len(tu_temps)
print(f'tu_temps_avg={tu_temps_avg}')
print(f'tu_temps_max={max(tu_temps)}')
print(f'tu_temps_min={min(tu_temps)}')
we_temps=week_temp[2]
we_temps_avg=sum(we_temps)/len(we_temps)
print(f'we_temps_avg={we_temps_avg}')
print(f'we_temps_max={max(we_temps)}')
print(f'we_temps_min={min(we_temps)}')
thu_temps=week_temp[3]
thu_temps_avg=sum(thu_temps)/len(thu_temps)
print(f'thu_temps_avg={thu_temps_avg}')
print(f'thu_temps_max={max(thu_temps)}')
print(f'thu_temps_min={min(thu_temps)}')
fry_temps=week_temp[4]
fry_temps_avg=sum(fry_temps)/len(fry_temps)
print(f'fry_temps_avg={fry_temps_avg}')
print(f'fry_temps_max={max(fry_temps)}')
print(f'fry_temps_min={min(fry_temps)}')
sat_temps=week_temp[5]
sat_temps_avg=sum(sat_temps)/len(sat_temps)
print(f'sat_temps_avg={sat_temps_avg}')
print(f'sat_temps_max={max(sat_temps)}')
print(f'sat_temps_min={min(sat_temps)}')
sun_temps=week_temp[6]
sun_temps_avg=sum(sun_temps)/len(sun_temps)
print(f'sun_temps_avg={sun_temps_avg}')
print(f'sun_temps_max={max(sun_temps)}')
print(f'sun_temps_min={min(sun_temps)}')
week_temp_avg=(mon_temps_avg+tu_temps_avg+we_temps_avg+thu_temps_avg+fry_temps_avg+sat_temps_avg+sun_temps_avg)/len(week_temp)
print(f'week_temp_avg={week_temp_avg}')