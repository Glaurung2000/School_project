import sensor, image, time, math, pyb, random, math
from pyb import Servo, Pin, Timer, millis
enable_lens_corr = True
true = True
TRUE = True
t = True
T = True
false = False
FALSE = False
f = False
F = False
usb = pyb.USB_VCP()
Debug = True
red_ang_green_cubes = True
black_wallse = True
detect_turns = True
r_led = pyb.LED(1)
g_led = pyb.LED(2)
b_led = pyb.LED(3)
button = Pin('P0', Pin.IN)
s1 = Servo(2)
timer = Timer(2, freq=1000)
IN4 = timer.channel(3, Timer.PWM, pin=Pin('P4'))
IN3 = timer.channel(4, Timer.PWM, pin=Pin('P5'))
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_gain(False, -1)
sensor.set_auto_exposure(False, 5000)
sensor.set_auto_whitebal(False)
sensor.skip_frames(time = 2000)
clock = time.clock()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
wight = (255, 255, 255)
black =(0, 0, 0)
yellow = (255, 255, 0)
pink = (255, 30, 255)
grey = (100, 100, 100)
dark_pink = (153, 0, 76)
light_grey = (180, 180, 180)
purple = (120, 0, 153)
thresholds = [
              (25, 95, -90, -28, 28, 90),
              (30, 55,  70, 89, 40, 70)]
black_wall = [(0, 13, -7, 7, -7, 7)]
turning_lines = [(70, 98, -27, 17, 40, 95)]
blue_lines = [(80, 97, -55, -35, -20, -5)]
straight_angle = 1350
right_angle = straight_angle - 350
left_angle = straight_angle + 350
cube_bypassing = f
negative_value = f
button_state = f
STOP = t
turns = 0
robot_speed = 52
robot_stop = 100
finish_time = 120000
last_click_time = 0
stop_time = 0
previous_turning_time = 0
cube_bypassing_time = 0
cube_on_turn = False
WK = 1.65
CK = 1.22
clockwize = f
turning = f
extra_turning = f
global_error = 0
first_line = True
direction = ''
checker = True
seen_red_last_time = 0
red_counter = 0
def emergency_stop():
    s1.pulse_width(straight_angle)
    IN3.pulse_width_percent(0)
    IN4.pulse_width_percent(0)
    stream.close()
    r_led.on()
    g_led.on()
    b_led.off()
    while(True): pass
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
def drive(angle):
    global turns
    global clockwize
    global straight_angle
    global robot_speed
    global global_error
    if STOP:
        s1.pulse_width(straight_angle)
        IN3.pulse_width_percent(0)
        IN4.pulse_width_percent(0)
    else:
        if Debug: print(angle)
        if extra_turning:
            b_led.off()
            g_led.on()
            if (clockwize and (angle < straight_angle)): angle = right_angle + 15
            elif (not(clockwize) and (angle > straight_angle)): angle = left_angle - 15
        elif turning:
            if (clockwize and not(cube_on_turn)): angle = straight_angle - 165
            elif (not(clockwize) and not(cube_on_turn)): angle = straight_angle + 165
            elif (clockwize and cube_on_turn): angle = angle - 40
            elif (not(clockwize) and cube_on_turn): angle = angle + 40
        s1.pulse_width(int(angle))
        time.sleep_ms(50)
        global_error += int(angle) - straight_angle
        if Debug: print("angle " + str(int(angle)))
        IN3.pulse_width_percent(100)
        IN4.pulse_width_percent(robot_speed)
        g_led.off()
name = "/" + str(pyb.rng()) + ".bin"
print(name)
stream = image.ImageIO(name, "w")
#stream = image.ImageIO("/112349354.bin", "r")
while(True):
    lines = list()
    clock.tick()
    #img = stream.read(copy_to_fb=True, loop=True, pause=True)
    img = sensor.snapshot()
    img = img.gaussian(3)
    img = img.gamma_corr(gamma = 0.3, contrast = 18.0, brightness = 0.1)
    nearest_cube = 0
    nearest_cube_area = 0
    cube_error = 0
    img.median(1, percentile=0.8)
    if red_ang_green_cubes:
        i = 0
        b_led.off()
        for blob in img.find_blobs(thresholds, pixels_threshold=20, area_threshold=20, roi = (0, 17, 160, 120)): # 160, 80
            dist = int(math.sqrt(abs(((blob.cx()-80)*(blob.cx()-80))+(((blob.y()+blob.h())-132)*((blob.y()+blob.h())-132)))))
            inverted_dist = int(math.sqrt(abs(((blob.cx()-80)*(blob.cx()-80))+(((blob.y()+blob.h())+45)*((blob.y()+blob.h())+45)))))
            if ((turns > 0)and(turns < 5)and(seen_red_last_time < millis()) \
            and(blob.code()==2)and(inverted_dist > 115)and(dist < 114)and(blob.cx() < 40)):
                red_counter += 1
                seen_red_last_time = millis() + 1200
            if (blob.elongation() > 0.9)or(blob.density() < 0.4)or(blob.area() < 60)  \
            or((blob.h()/ blob.w()) < 0.6)or((blob.code()==1)and(blob.x()>130))or((blob.code()==2)and((blob.x()+blob.w())<30)) \
            or(dist > 113):
                if Debug: img.draw_rectangle(blob.rect(), color = pink)
                if Debug and False: print("@@@@@@@@@@@@@@@ "+str(dist))
                if Debug and False:
                    print("X")
                    print(str(blob.code()) + " " + str((blob.x()+blob.w())/2))
                    print("Р›РёРЅРёСЏ РЅР° " + str(int(blob.elongation()*100)) + "%")
                    print("Р—Р°РїРѕР»РЅРµРЅРёРµ " + str(int(blob.density()*100)) + "%")
                    print("РџРёРєСЃРµР»Рё " + str(int(blob.area() * blob.density())))
                    print(blob.h()/ blob.w())
            else:
                if Debug and False:
                    print("V")
                    print("Р›РёРЅРёСЏ РЅР° " + str(int(blob.elongation()*100)) + "%")
                    print("Р—Р°РїРѕР»РЅРµРЅРёРµ " + str(int(blob.density()*100)) + "%")
                    print("РџРёРєСЃРµР»Рё " + str(int(blob.area() * blob.density())))
                    print(blob.h()/ blob.w())
                b_led.off()
                if i == 0:
                    nearest_cube = blob
                    nearest_cube_area = nearest_cube.area()
                else:
                    new_nearest_cube_area = blob.area()
                    if new_nearest_cube_area > nearest_cube_area:
                        nearest_cube = blob
                        nearest_cube_area = new_nearest_cube_area
                i+=1
        if nearest_cube !=0:
            if nearest_cube.code() == 1:
                cube_error = ((-160 + nearest_cube.x()) * (1 + (nearest_cube.y() + nearest_cube.h())/105) + 40) / 230 * 160
            if nearest_cube.code() == 2:
                cube_error = ((nearest_cube.x()+ nearest_cube.w()) * (1 + (nearest_cube.y() + nearest_cube.h())/105) - 40) / 230 * 160
    left_blob = 0
    left_black_area = 0
    right_blob = 0
    right_black_area = 0
    walls_error = 0
    if black_wallse:
        i = 0
        for blob in img.find_blobs(black_wall, pixels_threshold=10, area_threshold=10, roi = (0, 30, 80, 77)):
            if i == 0:
                left_blob = blob
                left_black_area = left_blob.area() * left_blob.density()
            else:
                new_black_area = blob.area() * blob.density()
                if new_black_area > left_black_area:
                    left_blob = blob
                    left_black_area = new_black_area
            i+=1
        j = 0
        for blob in img.find_blobs(black_wall, pixels_threshold=10, area_threshold=10, roi = (80, 30, 80, 77)):
            if j == 0:
                right_blob = blob
                right_black_area = right_blob.area() * right_blob.density()
            else:
                new_black_area = blob.area() * blob.density()
                if new_black_area > right_black_area:
                    right_blob = blob
                    right_black_area = new_black_area
            j+=1
        walls_error = int(left_black_area - right_black_area)

        turning = False
        extra_turning = False
        if detect_turns:
            for blob in img.find_blobs(turning_lines, pixels_threshold=40, area_threshold=40, roi = (0, 50, 160, 120)):
                if blob.elongation() > 0.6:
                    turning = True
                    if first_line:
                        clockwize =  True
                        first_line = False
                        direction = "CLOCKWIZE"
                    if Debug: img.draw_rectangle(blob.rect(), color = purple)
            for blob in img.find_blobs(blue_lines, pixels_threshold=30, area_threshold=30, roi = (5, 50, 150, 120)):
                if blob.elongation() > 0.6:
                    turning = True
                    if first_line:
                        clockwize =  False
                        first_line = False
                        direction = "CONTRCLOCKWIZE"
                    if Debug: img.draw_rectangle(blob.rect(), color = purple)
            for blob in img.find_blobs(black_wall, pixels_threshold=10, area_threshold=10, roi = (45, 30, 70, 10)):
                if blob.area() * blob.density() > 600:
                    extra_turning = True
                    if Debug: img.draw_rectangle(blob.rect(), color = pink)
        if Debug:
            if left_blob != 0:
                img.draw_rectangle(left_blob.rect(), color = grey)
                print("left: " + str(left_black_area))
            if right_blob != 0:
                img.draw_rectangle(right_blob.rect(), color = grey)
                print("right: " + str(right_black_area))
            if nearest_cube != 0:
                img.draw_rectangle(nearest_cube.rect(), color = grey)
                color_name = "none"
                if nearest_cube.code() == 1:
                    str_color_name = "green"
                if nearest_cube.code() == 2:
                    str_color_name = "red"
                print("cube error: " + str(cube_error))
                img.draw_string(nearest_cube.x(), nearest_cube.y()-7, str_color_name, color = dark_pink, scale = 4, mono_space = False,
                                char_rotation = 0, char_hmirror = False, char_vflip = False,
                                string_rotation = 0, string_hmirror = False, string_vflip = False)
            img.draw_string(5, 100, direction, color = light_grey, scale = 1, mono_space = False,
                            char_rotation = 0, char_hmirror = False, char_vflip = False,
                            string_rotation = 0, string_hmirror = False, string_vflip = False)
            img.draw_string(130, 90, str(turns), color = light_grey, scale = 2, mono_space = False,
                            char_rotation = 0, char_hmirror = False, char_vflip = False,
                            string_rotation = 0, string_hmirror = False, string_vflip = False)
            img.draw_string(110, 90, str(red_counter), color = pink, scale = 1, mono_space = False,
                            char_rotation = 0, char_hmirror = False, char_vflip = False,
                            string_rotation = 0, string_hmirror = False, string_vflip = False)
            print("FPS %f" % clock.fps())
        button_state = button.value()
        if (millis() > finish_time):
            emergency_stop()
        elif button_state and (millis() > last_click_time):
            STOP = not STOP
            if STOP:
                stop_time = millis()
            else:
                time.sleep_ms(200)
                finish_time += millis() - stop_time
                stop_time = 0
            last_click_time = millis() + 1000
        if (turns == 12)and(checker == True): # + red_counter
            finish_time = millis() + 1600
            checker = False
        if turns > 12 + red_counter: emergency_stop()
        new_value = straight_angle
        if nearest_cube == 0:
            cube_on_turn = False
            if walls_error < 0: negative_value = True
            sqrt_value = int(math.sqrt(abs(walls_error)))
            if sqrt_value > 65: sqrt_value = 65
            if negative_value:
                sqrt_value = -sqrt_value
                negative_value = False
            if (cube_bypassing_time < millis()):
                if Debug: print("sqrt_value" + str(sqrt_value))
                new_value = map(-sqrt_value * WK, -70, 70, right_angle, left_angle)
        else:
            cube_on_turn = True
            cube_bypassing_time = millis() + 50
            value = int(cube_error * CK)
            if value > 160: value = 160
            if value < -160: value = -160
            if Debug: print("cube_error " + str(value))
            new_value = map(-value, -160, 160, right_angle, left_angle)
            if new_value > left_angle: new_value = left_angle
            if new_value < right_angle: new_value = right_angle
        drive(new_value)
        if Debug: print("new_value " + str(new_value))
        if turning and (previous_turning_time < millis()):
            previous_turning_time = millis() + 2500
            turns += 1
            r_led.toggle()
    stream.write(img)
    if False and millis() > 180000:
        r_led.on()
        g_led.on()
        b_led.off()
        stream.close()
        while(True): pass
