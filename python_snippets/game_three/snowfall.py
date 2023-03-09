import simple_draw as sd
sd.resolution = (1500, 1000)
def create_snow(N):
    global pointlist
    pointlist = []
    for _ in range(N):
        length = sd.random_number(5, 15)
        x1 = sd.random_number(150, 1500)
        y1 = sd.random_number(800, 1000)
        item_a = sd.random_number(1, 8) / 10
        item_b = sd.random_number(1, 8) / 10
        item_c = sd.random_number(30, 60)
        speed=sd.random_number(5, 10)
        # rand=sd.random_number(1, 2)
        # if rand==1:
        #     turn=-3
        # else:
        #     turn=3
        pointlist.append([x1, y1, length, item_a, item_b, item_c, speed])
    print(pointlist)
def draw_snow_background_color():
    global point1
    for k in pointlist:
        point1 = sd.get_point(k[0], k[1])
        sd.snowflake(center=point1, length=k[2], color=sd.background_color, factor_a=k[3], factor_b=k[4], factor_c=k[5])

def move_snowflake():
    rand = sd.random_number(1, 2)
    for k in pointlist:
        k[1] -= k[6]
    print(pointlist)
        # k[0]+=k[7]
        # if rand == 1:
        #     k[0] -= 3
        # else:
        #     k[0] += 3


def draw_snowflake_colour():
    for k in pointlist:
        z = k[1] - k[6]
        rand=sd.random_number(1,2)
        if rand==1:
            k[0]+=sd.random_number(1,5)
        else:
            k[0]-=sd.random_number(1, 5)
        point2 = sd.get_point(k[0], z)
        sd.snowflake(center=point2, length=k[2], color=sd.COLOR_WHITE, factor_a=k[3], factor_b=k[4], factor_c=k[5])

def delete_snowfalke():
    for k in pointlist:
        if k[1] < 150:
            k[1]=sd.random_number(800, 1000)



# while True:
#     sd.start_drawing()
#     for k in pointlist:
#         rand = sd.random_number(1, 2)
#         point1 = sd.get_point(k[0], k[1])
#         sd.snowflake(center=point1, length=k[2], color=sd.background_color, factor_a=k[3], factor_b=k[4], factor_c=k[5])
#         speed = sd.random_number(5, 20)
#         z = k[1] - speed
#         k[1] -= speed
#         if rand == 1 and k[0] > 90:
#             k[0] -= 3
#         else:
#             k[0] += 3
#         point2 = sd.get_point(k[0], z)
#         sd.snowflake(center=point2, length=k[2], color=sd.COLOR_WHITE, factor_a=k[3], factor_b=k[4], factor_c=k[5])
#         z -= speed
#         if k[1] < 150:
#             sd.snowflake(center=point1, length=k[2])
#             k[1] = sd.random_number(900, 1200)
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# sd.pause()