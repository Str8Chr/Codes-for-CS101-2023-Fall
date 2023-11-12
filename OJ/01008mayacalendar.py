haab = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin',
         'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin',
         'muan', 'pax', 'koyab', 'cumhu', 'uayet']
tzolkin = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi',
           'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben',
           'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
n = int(input())
print(n)
for _ in range(n):
    day, month, year = input().split()
    day = int(day[:-1])
    month = haab.index(month)
    year = int(year)
    days = year * 365 + month * 20 + day
    year = days // 260
    days %= 260
    month = days % 20
    day = days % 13 + 1
    print(day, tzolkin[month], year)