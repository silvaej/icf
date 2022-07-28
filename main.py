import os
from check_speed import check_speed
from create_csv import create_csv

try:
    import click
except ModuleNotFoundError:
    os.system('python -m pip install click')
    import click


@click.command()
@click.option('-p', '--params', nargs=3, help='Duration(mins):FLOAT Interval(mins):FLOAT filename:String')
def set_params(params):
    """
    Collect all parameters from the command line interface (CLI) then execute check_speed() and create_csv()

        Parameters:
        params (tuple): the number of duration and intervals, and the filename

        Returns:
        null: Returning value

    """

    # check if duration is greater than the interval
    if (duration := int(params[0])) < (interval := int(params[1])):
        print('Duration should be greater than the interval. Please check your inputs!')
        return

    # checking internet speed
    try:
        data = check_speed(duration, interval)
        filename = params[2] + '.csv'
    except ValueError as e:
        print(f'Error: {e}, please check your inputs!')
        return

    # saving data to csv
    print('saving to csv ...')
    create_csv(data, filename)
    print('DONE! :)')
