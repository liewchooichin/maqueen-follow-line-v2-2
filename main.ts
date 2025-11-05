function move_away_from_obstacle () {
    // facing obstacle, move backwards
    if (is_obstacle()) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 15)
    } else {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 15)
    }
}
function track_black_line () {
    if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        basic.showString("M")
        get_position()
        adjust_out_of_position()
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        basic.showString("S")
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 15)
    } else {
        // if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 or maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        basic.showString("T")
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 15)
        get_position()
        adjust_out_of_position()
    }
}
// else:
// basic.show_string("---")
// - backward left, right,
// - forward left, right,
// - forward,
function move_randomly () {
    random_facing = randint(0, 4)
    if (random_facing == 0) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 0)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 15)
        basic.showNumber(0)
        basic.pause(100)
    } else if (random_facing == 1) {
        // turn left
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 15)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 0)
        basic.showNumber(1)
        basic.pause(100)
    } else if (random_facing == 2) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 15)
        basic.showNumber(2)
        basic.pause(100)
    } else if (random_facing == 3) {
        // backward left
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 15)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
        basic.showNumber(3)
        basic.pause(100)
    }
    move_away_from_obstacle()
}
function get_position () {
    if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        position_to_adjust = "L"
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        position_to_adjust = "R"
    } else {
        position_to_adjust = "M"
    }
}
function adjust_out_of_position () {
    basic.showString("A")
    // left sensor on white part
    if (position_to_adjust == "L") {
        while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 15)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 10)
        }
        position_to_adjust = "M"
    } else if (position_to_adjust == "R") {
        // left sensor on white part
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 10)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 15)
        }
        position_to_adjust = "M"
    } else if (position_to_adjust == "M") {
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1) {
            latest_position = "L"
        } else if (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            latest_position = "R"
        } else {
            latest_position = "M"
        }
        if (latest_position == "L") {
            while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1) {
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 15)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 10)
            }
            position_to_adjust = "M"
        } else if (latest_position == "R") {
            while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 10)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 15)
            }
            position_to_adjust = "M"
        } else {
            move_randomly()
        }
    } else {
    	
    }
}
function is_obstacle () {
    distance = maqueen.Ultrasonic()
    if (distance >= 0 && distance <= 4) {
        return true
    } else if (distance > 4) {
        return false
    } else {
        return false
    }
}
let distance = 0
let random_facing = 0
let latest_position = ""
let position_to_adjust = ""
position_to_adjust = "M"
latest_position = "M"
basic.showIcon(IconNames.SmallSquare)
basic.forever(function () {
    track_black_line()
})
