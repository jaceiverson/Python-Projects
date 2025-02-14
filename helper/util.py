import pickle
from configparser import ConfigParser
from cProfile import run
from time import perf_counter_ns

from rich.console import Console
from rich.table import Table

"""
WRAPPERS
"""


def build_output_table(function_name: str, time: int, runs: int):
    """
    takes in a function name, time, and runs and returns a formatted string
    """
    table = Table()
    table.add_column("Function Name", justify="center", style="yellow")
    table.add_column("Avg Time (ns)", justify="center", style="green")
    table.add_column("Executions", justify="center", style="blue")

    table.add_row(function_name, f"{time:,}", str(runs))
    return table


# a timer wrapper to time functions in ns
def mytime(func):
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()
        print(f"{func.__name__:>10} : {end-start:>10} ns")
        return result

    return wrapper


# average time decorator
def avgtime(run_times: int = 10, just_print: bool = False):
    def wrap(func):
        def wrapper(*args, **kwargs):
            times = []
            for _ in range(run_times):
                start = perf_counter_ns()
                func()
                end = perf_counter_ns()
                times.append(end - start)

            if just_print:
                print(
                    f"{func.__name__:>30}:{int(sum(times)/len(times)):>5,} ns:{run_times:>5,}runs"
                )
            else:
                table = build_output_table(
                    func.__name__, int(sum(times) / len(times)), run_times
                )
                console = Console()
                console.print(table)

        return wrapper

    return wrap


"""
OBJECT MANIPULATIONS
"""


def chunks(l, n=5):
    """
    params:
        l: taks in a list (or list like object)
        n: takes an int: default = 5 this is how big the smaller
            chunks will be
    returns:
        a list of lists with the smaller lists being size n
    """
    return [l[i : i + n] for i in range(0, len(l), n)]


def replace_text(text, delimiter, location, new_text):
    """
    delimit_change_join

    takes in a string, a delimiter, location (to change the string), and
    new text to replace at the desired location

    this funciton splits,changes the desired text (at the proper location) to
    the new_text variable.

    it then returns a joined string
    """

    temp = text.split(delimiter)
    temp[location] = new_text
    return delimiter.join(temp)


"""
FILE I/O
reading and writing files using pickle & configparser
"""


def pickle_write(file_name, data):
    """
    takes a filename and data and writes it to pickle
    """
    with open(file_name, "wb") as fid:
        pickle.dump(data, fid, pickle.HIGHEST_PROTOCOL)


def pickle_read(file_name):
    """
    takes a filename and reads from pickle
    """
    with open(file_name, "rb") as f:
        data = pickle.load(f)
    return data


def write(data, filepath="config.ini"):
    """
    pass in a dictionary, and filepath, and it will store the info
    in a config file to use in another program
    """
    config = ConfigParser()

    sections = list(data.keys())

    for x in sections:
        config[x] = data[x]

    # write to config file
    with open(filepath, "w") as configfile:
        config.write(configfile)


def read(filepath="config.ini", out=False):
    config = ConfigParser()

    config.read(filepath)

    if out:
        for group in config.sections():
            for key in config[group]:
                print(config[group][key])

    return config
