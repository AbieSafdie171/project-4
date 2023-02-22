"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

from acp_times import open_time, close_time
import nose  # Testing framework
import logging
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def loop_check(brevet_dist, brevet_start_time, checkpoints):
    for km, times in checkpoints.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time
        assert close_time(km, brevet_dist, brevet_start_time) == end_time


def test_brevet1():
    brevet_dist = 200
    brevet_start_time = arrow.get("2023-02-17T00:00")
    checkpoints = {
        0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
        50: (brevet_start_time.shift(hours=1.0, minutes=28),
             brevet_start_time.shift(hours=3.0, minutes=30)),
        100: (brevet_start_time.shift(hours=2.0, minutes=56),
              brevet_start_time.shift(hours=6.0, minutes=40)),
        175: (brevet_start_time.shift(hours=5.0, minutes=9),
              brevet_start_time.shift(hours=11.0, minutes=40)),
        200: (brevet_start_time.shift(hours=5.0, minutes=53),
              brevet_start_time.shift(hours=13.0, minutes=30)),
    }

    loop_check(brevet_dist, brevet_start_time, checkpoints)


def test_brevet2():
    brevet_dist = 400
    brevet_start_time = arrow.get("2023-02-17T00:00")
    checkpoints = {
        0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
        50: (brevet_start_time.shift(hours=1.0, minutes=28),
             brevet_start_time.shift(hours=3.0, minutes=30)),
        100: (brevet_start_time.shift(hours=2.0, minutes=56),
              brevet_start_time.shift(hours=6.0, minutes=40)),
        175: (brevet_start_time.shift(hours=5.0, minutes=9),
              brevet_start_time.shift(hours=11.0, minutes=40)),
        200: (brevet_start_time.shift(hours=5.0, minutes=53),
              brevet_start_time.shift(hours=13.0, minutes=20)),
        300: (brevet_start_time.shift(hours=9.0, minutes=0),
              brevet_start_time.shift(hours=20.0, minutes=0)),
        400: (brevet_start_time.shift(hours=12.0, minutes=8),
              brevet_start_time.shift(hours=27.0, minutes=0)),
        460: (brevet_start_time.shift(hours=12.0, minutes=8),
              brevet_start_time.shift(hours=27.0, minutes=0)),

    }

    loop_check(brevet_dist, brevet_start_time, checkpoints)



def test_brevet3():
    brevet_dist = 600
    brevet_start_time = arrow.get("2023-02-17T00:00")
    checkpoints = {
        0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
        50: (brevet_start_time.shift(hours=1.0, minutes=28),
             brevet_start_time.shift(hours=3.0, minutes=30)),
        100: (brevet_start_time.shift(hours=2.0, minutes=56),
              brevet_start_time.shift(hours=6.0, minutes=40)),
        175: (brevet_start_time.shift(hours=5.0, minutes=9),
              brevet_start_time.shift(hours=11.0, minutes=40)),
        200: (brevet_start_time.shift(hours=5.0, minutes=53),
              brevet_start_time.shift(hours=13.0, minutes=20)),
        300: (brevet_start_time.shift(hours=9.0, minutes=0),
              brevet_start_time.shift(hours=20.0, minutes=0)),
        400: (brevet_start_time.shift(hours=12.0, minutes=8),
              brevet_start_time.shift(hours=26.0, minutes=40)),
        560: (brevet_start_time.shift(hours=17.0, minutes=28),
              brevet_start_time.shift(hours=37.0, minutes=20)),
        600: (brevet_start_time.shift(hours=18.0, minutes=48),
              brevet_start_time.shift(hours=40.0, minutes=0)),
        620: (brevet_start_time.shift(hours=18.0, minutes=48),
              brevet_start_time.shift(hours=40.0, minutes=0)),

    }

    loop_check(brevet_dist, brevet_start_time, checkpoints)


def test_brevet4():
    brevet_dist = 1000
    brevet_start_time = arrow.get("2023-02-17T00:00")
    checkpoints = {
        0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
        100: (brevet_start_time.shift(hours=2.0, minutes=56),
              brevet_start_time.shift(hours=6.0, minutes=40)),
        200: (brevet_start_time.shift(hours=5.0, minutes=53),
              brevet_start_time.shift(hours=13.0, minutes=20)),
        300: (brevet_start_time.shift(hours=9.0, minutes=0),
              brevet_start_time.shift(hours=20.0, minutes=0)),
        400: (brevet_start_time.shift(hours=12.0, minutes=8),
              brevet_start_time.shift(hours=26.0, minutes=40)),
        500: (brevet_start_time.shift(hours=15.0, minutes=28),
              brevet_start_time.shift(hours=33.0, minutes=20)),
        600: (brevet_start_time.shift(hours=18.0, minutes=48),
              brevet_start_time.shift(hours=40.0, minutes=0)),
        650: (brevet_start_time.shift(hours=20.0, minutes=35),
              brevet_start_time.shift(hours=44.0, minutes=23)),
        750: (brevet_start_time.shift(hours=24.0, minutes=9),
              brevet_start_time.shift(hours=53.0, minutes=8)),
        822: (brevet_start_time.shift(hours=26.0, minutes=44),
              brevet_start_time.shift(hours=59.0, minutes=26)),
        900: (brevet_start_time.shift(hours=29.0, minutes=31),
              brevet_start_time.shift(hours=66.0, minutes=15)),
        1000: (brevet_start_time.shift(hours=33.0, minutes=5),
              brevet_start_time.shift(hours=75.0, minutes=0)),
        1200: (brevet_start_time.shift(hours=33.0, minutes=5),
              brevet_start_time.shift(hours=75.0, minutes=0)),

    }

    loop_check(brevet_dist, brevet_start_time, checkpoints)

def test_brevet5():
    brevet_dist = 200
    brevet_start_time = arrow.get("2023-02-17T00:00")
    checkpoints = {
        0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
        50: (brevet_start_time.shift(hours=1.0, minutes=28),
             brevet_start_time.shift(hours=3.0, minutes=30)),
        100: (brevet_start_time.shift(hours=2.0, minutes=56),
              brevet_start_time.shift(hours=6.0, minutes=40)),
        175: (brevet_start_time.shift(hours=5.0, minutes=9),
              brevet_start_time.shift(hours=11.0, minutes=40)),
        200: (brevet_start_time.shift(hours=5.0, minutes=53),
              brevet_start_time.shift(hours=13.0, minutes=30)),
        220: (brevet_start_time.shift(hours=5.0, minutes=53),
              brevet_start_time.shift(hours=13.0, minutes=30)),
    }

    loop_check(brevet_dist, brevet_start_time, checkpoints)