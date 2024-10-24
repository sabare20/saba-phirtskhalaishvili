input_time=input('enter your time :')
date_time,timezone=input_time.split('+')
date,time=date_time.split('T')
year,mont,day=date.split('-')
hour,minute,seconde=time.split(':')
seconde_1=seconde.split('.')[0]
hour_1=int(hour)%12
timezone_1=int(timezone.split(':')[0])
output_time=f'{day}-{mont}-{year} {hour_1}:{minute}:{seconde_1}+{timezone_1}'
print(output_time)

