import argparse
import serial

from serial_connection import SerialConnection


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
        "port",
        type=str,
        help="The port the arduino is connected to.",
    )
    args = parser.parse_args()

    print("Connecting...")
    try:
        connection: SerialConnection = SerialConnection(args.port)
    except serial.serialutil.SerialException as e:
        print(e)
        return

    print("Sending message...")
    connection.send("Hello World!")
    print("Receiving message...")
    print(connection.recv())


if __name__ == "__main__":
    main()
