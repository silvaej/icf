import time
import subprocess
import os
from collections import defaultdict


def check_speed(duration, intervals):
    """Gather the data and link the result to the dictionary.

        Parameters:
        The parameter includes the result of duration and interval and the speed of upload, download and ping.

        Returns:
        Import the value from the equation and associate it in the dictionary.
   """
        
    number_of_loops = duration//intervals
    speedtest_command = 'speedtest-cli --csv-delimiter "?" --csv'

    # check if speedtest-cli is installed in the system
    try:
        subprocess.Popen('speedtest-cli --version')
        
    # install speedtest-cli if not found
    except FileNotFoundError:
        os.system('python -m pip install speedtest-cli')

    # getting headers
    headers = subprocess.Popen('speedtest-cli --csv-header',
                               stdout=subprocess.PIPE).stdout.readline().rstrip().decode('UTF-8').split(',')

    # initialized dictionary
    result_dictionary = defaultdict(list)

    for i in range(number_of_loops):
        print(f'{i+1}/{number_of_loops} Running speedtest ...')

        raw_result = subprocess.Popen(
            speedtest_command, stdout=subprocess.PIPE).stdout
        result = raw_result.readline().rstrip().decode('UTF-8').split('?')

        print(result)
        if len(result) != len(headers):
            continue

        # add result to the dictionary
        for header, value in zip(headers, result):
            result_dictionary[header].append(value)

        print('Done!\n')

        # convert intervals from minute to seconds
        time.sleep(intervals * 60)

    return result_dictionary