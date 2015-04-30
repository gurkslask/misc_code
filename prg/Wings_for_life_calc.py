bil_h_dict = {0: 0, 30: 15, 60: 16, 120: 17, 180: 20}
keys_list = bil_h_dict.keys()
p_h = 5.3
bil_h = 0.0

bil_dist = 0.0
p_dist = 0.1
time_passed = 0

while p_dist > bil_dist:
    time_passed += 1
    if time_passed in keys_list:
        bil_h = bil_h_dict[time_passed]
    try:
        bil_dist += (bil_h / 60)
    except ZeroDivisionError:
        pass
    p_dist += 1/p_h
print('Personen har kommit: {}km\nBilen har kommit: {}km'.format(p_dist, bil_dist))



