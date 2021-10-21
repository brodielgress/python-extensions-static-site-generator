from ssg import hooks

import time

start_time = None

total_written = 0

@.register("start_build")
def start_build():
    