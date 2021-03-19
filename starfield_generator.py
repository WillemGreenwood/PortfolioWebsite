from random import Random

r = Random()

shine_min_time = 5
shine_max_time = 20

shoot_min_time = 7
shoot_max_time = 15

shine_count = 40
shoot_count = 30

def linear():
    return r.randint(0, 100)

def low_weighted():
    n = r.randint(0, 100) + r.randint(0, 100)
    return n - 100 if n >= 100 else 100 - n

def mid_weighted():
    return r.randint(0, 50) + r.randint(0, 50)

def high_weighted():
    n = r.randint(0, 100) + r.randint(0, 100)
    return n if n <= 100 else 200 - n

shine_format = '<div class="shining-star" style="top: {}%; left: {}%; animation-duration: {}s; animation-delay: {}s;"></div>'
shoot_format = '<div class="shooting-star" style="top: {}%; left: {}%; animation-duration: {}s; animation-delay: {}s;"></div>'

for i in range(shine_count):
    print(shine_format.format(low_weighted(), linear(), r.randint(shine_min_time, shine_max_time), r.randrange(shine_max_time)))

for i in range(shoot_count):
    print(shoot_format.format(low_weighted(), linear(), r.randint(shoot_min_time, shoot_max_time), r.randrange(shoot_max_time)))
