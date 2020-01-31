# **************************************************************
# Project 02 - Disciplina de robótica Móvel UFC / IFCE / LAPISCO
#       Simulação 01 com robô Pioneer 3AT - Webots R2020a
#                       Distance sensors
#        Python 3.6 na IDE Pycharm - controller <extern>
#                By: Jefferson Silva Almeida
#                       Data: 23/01/2020
# **************************************************************

from controller import Robot
from controller import Motor
from controller import DistanceSensor

# time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.28

# maximal value returned by the sensors
MAX_SENSOR_VALUE = 1024
# minimal distance, in meters, for an obstacle to be considered
MIN_DISTANCE = 1.0

# create the robot instance
robot = Robot()

# get a handler to the motors and set target position to infinity (speed control)
leftMotorFront = robot.getMotor('front left wheel')
rightMotorFront = robot.getMotor('front right wheel')
leftMotorBack = robot.getMotor('back left wheel')
rightMotorBack = robot.getMotor('back right wheel')

leftMotorFront.setPosition(float('inf'))
rightMotorFront.setPosition(float('inf'))
leftMotorBack.setPosition(float('inf'))
rightMotorBack.setPosition(float('inf'))

# initialize devices
ps = []
psNames = [
    'so0', 'so1', 'so2', 'so3',
    'so4', 'so5', 'so6', 'so7'
]

for i in range(8):
    ps.append(robot.getDistanceSensor(psNames[i]))
    ps[i].enable(TIME_STEP)

while robot.step(TIME_STEP) != -1:
    # read sensors outputs
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())
        # print(psValues[i])

    # detect obstacles
    right_obstacle = psValues[0] > 70.0 or psValues[1] > 70.0 or psValues[2] > 70.0
    left_obstacle = psValues[5] > 70.0 or psValues[6] > 70.0 or psValues[7] > 70.0
    front_obstacle = psValues[3] > 50.0 or psValues[4] > 50.0
    # print(right_obstacle)
    # print(left_obstacle)

    # initialize motor speeds at 50% of MAX_SPEED.
    leftSpeed = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED

    # modify speeds according to obstacles
    if front_obstacle:
        leftSpeed -= 0.5 * MAX_SPEED
        rightSpeed += 0.5 * MAX_SPEED
        print("front_obstacle")
    elif left_obstacle:
        leftSpeed -= 0.5 * MAX_SPEED
        rightSpeed += 0.5 * MAX_SPEED
        print("left_obstacle")
    elif right_obstacle:
        leftSpeed += 0.5 * MAX_SPEED
        rightSpeed -= 0.5 * MAX_SPEED
        print("right_obstacle")

    # set up the motor speeds at x% of the MAX_SPEED.
    leftMotorFront.setVelocity(leftSpeed)
    rightMotorFront.setVelocity(rightSpeed)
    leftMotorBack.setVelocity(leftSpeed)
    rightMotorBack.setVelocity(rightSpeed)

    pass
