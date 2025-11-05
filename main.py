def move_away_from_obstacle():
    # facing obstacle, move backwards
    if is_obstacle():
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 15)
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 15)
def track_black_line():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        basic.show_string("M")
        get_position()
        adjust_out_of_position()
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        basic.show_string("S")
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 15)
    else:
        # if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 or maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        basic.show_string("T")
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 15)
        get_position()
        adjust_out_of_position()
# else:
# basic.show_string("---")
# - backward left, right,
# - forward left, right,
# - forward,
def move_randomly():
    global random_facing
    random_facing = randint(0, 4)
    if random_facing == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 15)
        basic.show_number(0)
        basic.pause(100)
    elif random_facing == 1:
        # turn left
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 15)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 0)
        basic.show_number(1)
        basic.pause(100)
    elif random_facing == 2:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 15)
        basic.show_number(2)
        basic.pause(100)
    elif random_facing == 3:
        # backward left
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 15)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
        basic.show_number(3)
        basic.pause(100)
    move_away_from_obstacle()
def get_position():
    global position_to_adjust
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        position_to_adjust = "L"
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        position_to_adjust = "R"
    else:
        position_to_adjust = "M"
def adjust_out_of_position():
    global position_to_adjust, latest_position
    basic.show_string("A")
    # left sensor on white part
    if position_to_adjust == "L":
        while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 15)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 10)
        position_to_adjust = "M"
    elif position_to_adjust == "R":
        # left sensor on white part
        while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 10)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 15)
        position_to_adjust = "M"
    elif position_to_adjust == "M":
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
            latest_position = "L"
        elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            latest_position = "R"
        else:
            while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 15)
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 10)
        if latest_position == "L":
            while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 15)
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 10)
            position_to_adjust = "M"
        elif latest_position == "R":
            while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 10)
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 15)
            position_to_adjust = "M"
        else:
            pass
    else:
        pass
def is_obstacle():
    global distance
    distance = maqueen.ultrasonic()
    if distance >= 0 and distance <= 4:
        return True
    elif distance > 4:
        return False
    else:
        return False
distance = 0
random_facing = 0
latest_position = ""
position_to_adjust = ""
position_to_adjust = "M"
latest_position = "M"
basic.show_icon(IconNames.SMALL_SQUARE)

def on_forever():
    track_black_line()
basic.forever(on_forever)
