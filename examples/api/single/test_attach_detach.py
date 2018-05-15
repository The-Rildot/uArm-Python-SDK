#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFactory, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI
from uarm.swift.protocol import SERVO_BOTTOM, SERVO_LEFT, SERVO_RIGHT, SERVO_HAND

"""
测试锁住和解锁接口
"""

swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})

swift.waiting_ready()

swift.set_servo_detach(servo_id=SERVO_BOTTOM)
time.sleep(2)
swift.set_servo_detach(servo_id=SERVO_LEFT)
time.sleep(2)
swift.set_servo_detach(servo_id=SERVO_RIGHT)
time.sleep(2)
swift.set_servo_detach(servo_id=SERVO_HAND)

time.sleep(2)
swift.set_servo_attach(servo_id=SERVO_BOTTOM)
time.sleep(2)
swift.set_servo_attach(servo_id=SERVO_LEFT)
time.sleep(2)
swift.set_servo_attach(servo_id=SERVO_RIGHT)
time.sleep(2)
swift.set_servo_attach(servo_id=SERVO_HAND)

swift.set_servo_detach()
time.sleep(5)
swift.set_servo_attach()
time.sleep(2)

swift.disconnect()
