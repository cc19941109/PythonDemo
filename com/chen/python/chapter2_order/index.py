months = [
    'January',
    'Febuary'
    , 'March'
    , 'April'
    , 'May',
    'June',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

print(endings)


year=input('year:')
month = input('Month[1-12]:')
day = input('day[1-31]')

# 转换为int型
month_nub = int(month)
day_number = int(day)


month_name = months[month_nub-1]
ordinal = day+endings[day_number-1]
print(month_name +' '+ordinal+'. '+year)