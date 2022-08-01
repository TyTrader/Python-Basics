# Conditions and if statements
a = 10
b = 100
c = 1000
d = 10000

if a > b:
    print('next')
elif b > a:  # This means if previous conditions were not met, try this.
    print('prev')
else:
    print('done')

if a < b:
    print('next')
elif b < a:  # This means if previous conditions were not met, try this.
    print('prev')
else:
    print('done')

if a == b:
    print('next')
elif b == a:  # This means if previous conditions were not met, try this.
    print('prev')
else:
    print('done')

if a >= b:
    print('next')
elif b >= a:  # This means if previous conditions were not met, try this.
    print('prev')
else:
    print('done')

if a <= b:
    print('next')
elif b <= a:  # This means if previous conditions were not met, try this.
    print('prev')
else:
    print('done')

if a > b and c > d:
    print('next')
elif b > a and d > a:  # This means if previous conditions were not met, try this.
    print('prev')
else:
    print('done')

if a != b and c != d:
    print('next')
elif b != a and d != a:  # This means if previous conditions were not mett, try this.
    print('prev')
else:
    print('done')

if a > b or c > d:
    print('next')
elif b > a or d > c:  # This means if previous conditions were not met, try this.
    print('prev')
else:
    print('done')

# Nested If statements

x = 9

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

elif x < 10:
    print('less than 10')
    if x > 5:
        print('less than 5')

else:
    print('We are finished')
