# -*- encoding=utf8 -*-
__author__ = "Adrian"

from airtest.core.api import *

auto_setup(__file__)

start_app("dk.tactile.lilysgarden")

wait(Template(r"1.png", record_pos=(0.195, 0.186), resolution=(2960, 1440)))
sleep(2)
if exists(Template(r"2.png", record_pos=(0.179, 0.077), resolution=(2960, 1440))):

    touch(Template(r"3.png", record_pos=(0.18, 0.079), resolution=(2960, 1440)))

    wait(Template(r"4.png", record_pos=(-0.127, -0.051), resolution=(2960, 1440)))
    touch(Template(r"5.png", record_pos=(-0.121, 0.02), resolution=(2960, 1440)))
    sleep(10)
    assert_exists(Template(r"6.png", record_pos=(-0.328, -0.185), resolution=(2960, 1440)), "Facebook start log in button works.")

    touch(Template(r"7.png", record_pos=(-0.471, -0.199), resolution=(2960, 1440)))
    wait(Template(r"8.png", record_pos=(-0.121, 0.023), resolution=(2960, 1440)))
    assert_exists(Template(r"9.png", record_pos=(-0.006, -0.113), resolution=(2960, 1440)), "Facebook backbutton works.")
    touch(Template(r"0.png", record_pos=(0.169, -0.108), resolution=(2960, 1440)))
    
wait(Template(r"10.png", record_pos=(0.001, 0.18), resolution=(2960, 1440)))
if exists(Template(r"11.png", record_pos=(-0.003, 0.185), resolution=(2960, 1440))):
    touch(Template(r"11.png", record_pos=(-0.003, 0.185), resolution=(2960, 1440)))
    sleep(2)
    
if  exists(Template(r"222.png", record_pos=(-0.001, -0.172), resolution=(2960, 1440)))
    touch(Template(r"232.png", record_pos=(-0.002, 0.166), resolution=(2960, 1440)))
    sleep(2)
if exists(Template(r"12.png", record_pos=(-0.01, -0.146), resolution=(2960, 1440))):
    assert_exists(Template(r"13.png", record_pos=(-0.003, 0.115), resolution=(2960, 1440)), "Update available.")
    touch(Template(r"14.png", record_pos=(0.188, -0.141), resolution=(2960, 1440)))

wait(Template(r"15.png", record_pos=(-0.426, 0.173), resolution=(2960, 1440)))
touch(Template(r"16.png", record_pos=(0.454, -0.204), resolution=(2960, 1440)))
assert_exists(Template(r"17.png", record_pos=(-0.145, 0.061), resolution=(2960, 1440)), "Setting buttons exist.")
    
assert_exists(Template(r"18.png", record_pos=(0.153, -0.046), resolution=(2960, 1440)), "Volume and sound button exist.")
if exists(Template(r"19.png", record_pos=(-0.124, -0.072), resolution=(2960, 1440))):
    touch(Template(r"20.png", record_pos=(-0.125, -0.071), resolution=(2960, 1440)))
    wait(Template(r"21.png", record_pos=(0.006, 0.066), resolution=(2960, 1440)))
    touch(Template(r"22.png", record_pos=(-0.002, 0.107), resolution=(2960, 1440)))
    sleep(10)
    touch(Template(r"23.png", record_pos=(-0.132, 0.077), resolution=(2960, 1440)))
    assert_exists(Template(r"24.png", record_pos=(-0.125, -0.076), resolution=(2960, 1440)), "Facebook log in works.")
if exists(Template(r"25.png", record_pos=(-0.123, -0.073), resolution=(2960, 1440))):
    touch(Template(r"26.png", record_pos=(-0.118, -0.074), resolution=(2960, 1440)))
    assert_exists(Template(r"27.png", record_pos=(-0.121, -0.076), resolution=(2960, 1440)), "Facebook log out works.")
touch(Template(r"28.png", record_pos=(-0.152, -0.007), resolution=(2960, 1440)))
assert_exists(Template(r"29.png", record_pos=(-0.011, -0.205), resolution=(2960, 1440)), "User support button works.")
    
touch(Template(r"30.png", record_pos=(-0.433, -0.207), resolution=(2960, 1440)))
touch(Template(r"31.png", record_pos=(0.283, -0.165), resolution=(2960, 1440)))
touch(Template(r"32.png", record_pos=(-0.432, 0.166), resolution=(2960, 1440)))
assert_exists(Template(r"33.png", record_pos=(-0.223, -0.129), resolution=(2960, 1440)), "Tasks button works.")
    
touch(Template(r"34.png", record_pos=(0.284, -0.148), resolution=(2960, 1440)))
wait(Template(r"35.png", record_pos=(0.387, 0.168), resolution=(2960, 1440)))
touch(Template(r"36.png", record_pos=(0.387, 0.168), resolution=(2960, 1440)))

assert_exists(Template(r"37.png", record_pos=(-0.002, 0.128), resolution=(2960, 1440)), "Level start button works.")
touch(Template(r"38.png", record_pos=(-0.003, 0.127), resolution=(2960, 1440)))
sleep(3)
touch(Template(r"39.png", record_pos=(0.452, 0.196), resolution=(2960, 1440)))
sleep(2)
assert_exists(Template(r"40.png", record_pos=(0.373, 0.199), resolution=(2960, 1440)), "Stage pause menu works.")

touch(Template(r"41.png", record_pos=(0.345, 0.197), resolution=(2960, 1440)))
sleep(1)
assert_exists(Template(r"42.png", record_pos=(0.347, 0.196), resolution=(2960, 1440)), "Music button works.")
touch(Template(r"43.png", record_pos=(0.347, 0.197), resolution=(2960, 1440)))
touch(Template(r"44.png", record_pos=(0.4, 0.197), resolution=(2960, 1440)))
sleep(1)
assert_exists(Template(r"45.png", record_pos=(0.402, 0.197), resolution=(2960, 1440)), "Sound button works.")
touch(Template(r"46.png", record_pos=(0.402, 0.197), resolution=(2960, 1440)))
sleep(1)
touch(Template(r"47.png", record_pos=(0.293, 0.197), resolution=(2960, 1440)))
touch(Template(r"48.png", record_pos=(-0.364, -0.216), resolution=(2960, 1440)))
assert_exists(Template(r"49.png", record_pos=(-0.001, 0.007), resolution=(2960, 1440)), "Lives pop-up menu.")
touch(Template(r"50.png", record_pos=(0.195, -0.146), resolution=(2960, 1440)))
sleep(2)
touch(Template(r"51.png", record_pos=(-0.213, -0.217), resolution=(2960, 1440)))
assert_exists(Template(r"52.png", record_pos=(-0.002, -0.148), resolution=(2960, 1440)), "Coins menu.")
touch(Template(r"53.png", record_pos=(0.282, -0.176), resolution=(2960, 1440)))
home()




