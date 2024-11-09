import time
from yaml import YAMLObject

import matplotlib.pyplot as plt

from serial_connection import SerialConnection
from tester import Tester, TesterException


class TimingDiagramTester(Tester):
    def __init__(
        self,
        headers: list[str],
        output_measuring_pins: list[int],
        measurement_duration: float
    ):
        self.headers = headers
        self.output_measuring_pins = output_measuring_pins
        self.measurement_duration = measurement_duration

    def test(self, connection: SerialConnection):
        connection.send(f"Tester InputTester {",".join(
            map(str, self.output_measuring_pins))}")
        outputs = [[] for _ in range(len(self.headers) + 1)]
        start = time.time()
        while self.measurement_duration > time.time() - start:
            connection.send("")
            message: str = connection.recv()
            if message.startswith("Error"):
                raise TesterException(f"Arduino {message}")

            measured_output: list[str] = message.split(",")
            if len(measured_output) != len(self.headers):
                raise TesterException(
                    f"The length of measured outputs doesn't match the lenght of headers: {message}.")

            try:
                measured_output = list(map(float, measured_output))
            except ValueError:
                raise Exception(
                    "Measured output can not be converted to a float.")

            outputs[0].append(time.time() - start)
            for i in range(1, len(outputs)):
                outputs[i].append(measured_output[i - 1])

            time.sleep(0.01)

        plt.style.use('fivethirtyeight')
        plt.tight_layout()
        plt.title('Timing diagram')
        plt.xlabel('time in s')
        for index, header in enumerate(self.headers):
            plt.plot(outputs[0], outputs[index + 1], label=header)

        plt.legend(loc='upper left')
        plt.show()


def timingDiagramTesterFromYaml(task: YAMLObject) -> TimingDiagramTester:
    timing_diagram: YAMLObject = task.get("timing-diagram")
    if timing_diagram is None:
        raise TesterException(
            "Expected \"timing-diagram\" key in task specification with type \"timing-diagram\".")

    headers: YAMLObject = timing_diagram.get("headers")
    if headers is None:
        raise TesterException(
            "Expected \"headers\" key in the scope of key \"timing-diagram\" in task specification with type \"timing-diagram\".")
    if not isinstance(headers, list):
        raise TesterException(
            "Expected \"headers\" key to be of type list of string.")
    if not headers:
        raise TesterException(
            "Expected \"headers\" key to not be an empty list.")
    for header in headers:
        if not isinstance(header, str):
            raise TesterException(
                "Expected all values in \"headers\" key to be of type string.")

    output_measuring_pins: YAMLObject = timing_diagram.get(
        "output-measuring-pins")
    if output_measuring_pins is None:
        raise TesterException(
            "Expected \"output-measuring-pins\" key in the scope of key \"timing-diagram\" in task specification with type \"timing-diagram\".")
    if not isinstance(output_measuring_pins, list):
        raise TesterException(
            "Expected \"output-measuring-pins\" key to be of type list of int.")
    if not output_measuring_pins:
        raise TesterException(
            "Expected \"output-measuring-pins\" key to not be an empty list.")
    for output_measuring_pin in output_measuring_pins:
        if not isinstance(output_measuring_pin, int):
            raise TesterException(
                "Expected all values in \"output-measuring-pins\" key to be of type int.")
        if output_measuring_pin < 2 or 53 < output_measuring_pin:
            raise TesterException(
                "Expected all output_measuring_pins to be greater than 1 and smaller than 54.")

    measurement_duration: YAMLObject = timing_diagram.get(
        "measurement-duration")
    try:
        measurement_duration = float(measurement_duration)
    except ValueError:
        raise TesterException(
            "Expected \"measurement-duration\" to be a float.")

    return TimingDiagramTester(
        headers,
        output_measuring_pins,
        measurement_duration
    )
