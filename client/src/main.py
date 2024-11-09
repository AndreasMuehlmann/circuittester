import os
import argparse
import serial
import yaml

from serial_connection import SerialConnection
from tester import TesterException
from truth_table_tester import truthTableTesterFromYaml, TruthTableTester


def main():
    parser = argparse.ArgumentParser(
        prog="circuittester",
        description="Testing circuits based on a task written in yaml."
    )
    parser.add_argument(
        "task",
        type=str,
        help="The yaml file specifying a task.",
    )
    parser.add_argument(
        "--port",
        type=str,
        help="The port the arduino is connected to.",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.task):
        print("Error: \"{args.task}\" is not a file.")
        return
    try:
        with open(args.task, "r") as file:
            task = yaml.safe_load(file)
    except Exception as e:
        print(f"Error: {e}")
        return

    if args.port:
        port = args.port
    elif task.get("port") is not None:
        port = task.get("port")
    else:
        print("Error: Port has to be provided as argument or in task.")
        return

    taskType = task.get("type")
    if taskType is None:
        print("Error: Expected \"type\" key in task specification.")
        return

    try:
        if taskType == "truth-table":
            tester: TruthTableTester = truthTableTesterFromYaml(task)
        else:
            print(f"Error: \"{taskType}\" is not an available type for a task."
                  f"Available task types are: \"truth-table\"")
            return
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        connection: SerialConnection = SerialConnection(port)
    except serial.serialutil.SerialException as e:
        print(f"Error: {e}")
        return

    try:
        tester.test(connection)
    except TesterException as e:
        print(f"Error: {e}")
        connection.send("Tester NothingTester")
        connection.reset()
        return

    connection.send("Tester NothingTester")
    connection.reset()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
