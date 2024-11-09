import time
from yaml import YAMLObject

from tester import Tester, TesterException
from serial_connection import SerialConnection
from utils import left_pad, validate_measured_output, print_truth_table


class TruthTableTester(Tester):
    def __init__(
        self,
        input_headers: list[str],
        input_sending_pins: list[int],
        output_headers: list[str],
        output_measuring_pins: list[int],
        expected_outputs: list[list[int]]
    ):
        self.input_sending_pins = input_sending_pins
        self.output_measuring_pins = output_measuring_pins
        self.expected_outputs = expected_outputs
        self.input_headers = input_headers
        self.output_headers = output_headers

    def test(self, connection: SerialConnection):
        connection.send(f"Tester InputOutputTester {",".join(map(str, self.output_measuring_pins))};{",".join(map(str, self.input_sending_pins))}")
        measured_outputs = []
        for input, expected_output in enumerate(self.expected_outputs):
            input_binary: str = list(left_pad(f"{input:b}", "0", len(self.input_headers)))
            connection.send(",".join(input_binary))

            message: str = connection.recv()
            if message.startswith("Error"):
                raise TesterException(f"Arduino {message}")

            measured_output: list[str] = message.split(",")
            if len(measured_output) != len(self.output_headers):
                raise TesterException(f"The length of measured outputs doesn't match the lenght of output headers: {message}.")
            measured_outputs.append(validate_measured_output(measured_output))

            time.sleep(0.01)

        print_truth_table(self.input_headers, self.output_headers, self.expected_outputs, measured_outputs)


def truthTableTesterFromYaml(task: YAMLObject) -> TruthTableTester:
    truth_table: YAMLObject = task.get("truth-table")
    if truth_table is None:
        raise TesterException(
            "Expected \"truth-table\" key in task specification with type \"truth-table\".")

    input_headers: YAMLObject = truth_table.get("input-headers")
    if input_headers is None:
        raise TesterException(
            "Expected \"input-headers\" key in the scope of key \"truth-table\" in task specification with type \"truth-table\".")
    if not isinstance(input_headers, list):
        raise TesterException(
            "Expected \"input-headers\" key to be of type list of string.")
    if not input_headers:
        raise TesterException(
            "Expected \"input-headers\" key to not be an empty list.")
    for output_header in input_headers:
        if not isinstance(output_header, str):
            raise TesterException(
                "Expected all values in \"input-headers\" key to be of type string.")

    input_sending_pins: YAMLObject = truth_table.get("input-sending-pins")
    if input_sending_pins is None:
        raise TesterException(
            "Expected \"input-sending-pins\" key in the scope of key \"truth-table\" in task specification with type \"truth-table\".")
    if not isinstance(input_sending_pins, list):
        raise TesterException(
            "Expected \"input-sending-pins\" key to be of type list of int.")
    if not input_sending_pins:
        raise TesterException(
            "Expected \"input-sending-pins\" key to not be an empty list.")
    for input_sending_pin in input_sending_pins:
        if not isinstance(input_sending_pin, int):
            raise TesterException(
                "Expected all values in \"input-sending-pins\" key to be of type int.")
        if input_sending_pin < 2 or 53 < input_sending_pin:
            raise TesterException(
                "Expected all input-sending-pins be greater than 1 and smaller than 54.")

    if len(input_headers) != len(input_sending_pins):
        raise TesterException(
            "Expected \"input-headers\" and \"input_sending_pins\" to be of the same length.")

    output_headers: YAMLObject = truth_table.get("output-headers")
    if output_headers is None:
        raise TesterException(
            "Expected \"output-headers\" key in the scope of key \"truth-table\" in task specification with type \"truth-table\".")
    if not isinstance(output_headers, list):
        raise TesterException(
            "Expected \"output-headers\" key to be of type list of string.")
    if not output_headers:
        raise TesterException(
            "Expected \"output-headers\" key to not be an empty list.")
    for output_header in output_headers:
        if not isinstance(output_header, str):
            raise TesterException(
                "Expected all values in \"output-headers\" key to be of type string.")

    output_measuring_pins: YAMLObject = truth_table.get("output-measuring-pins")
    if output_measuring_pins is None:
        raise TesterException(
            "Expected \"output-measuring-pins\" key in the scope of key \"truth-table\" in task specification with type \"truth-table\".")
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

    expected_outputs: YAMLObject = truth_table.get("expected-outputs")
    if expected_outputs is None:
        raise TesterException(
            "Expected \"expected-outputs\" key in the scope of key \"truth-table\" in task specification with type \"truth-table\".")
    if not isinstance(expected_outputs, list):
        raise TesterException(
            "Expected \"expected-outputs\" key to be of type list of list of int.")
    if not expected_outputs:
        raise TesterException(
            "Expected \"expected-outputs\" key to be not be an empty list.")
    if len(expected_outputs) > 2 ** len(input_headers):
        raise TesterException(
            "Expected lenght of expected-outputs to be smaller or equal to 2^lenght(input_headers).")

    for expected_output in expected_outputs:
        if not isinstance(expected_output, list):
            raise TesterException(
                "Expected every element of \"expected-outputs\" key to be of type list of int.")
        if len(expected_output) != len(output_headers):
            raise TesterException(
                "Expected every element of \"expected-outputs\" key to be of the same lenght as output-headers.")
        for expected_output_for_header in expected_output:
            if not isinstance(expected_output_for_header, int):
                raise TesterException(
                    "Expected all values in \"expected-outputs\" key to be of type int.")
            if expected_output_for_header != 0 and expected_output_for_header != 1:
                raise TesterException(
                    "Expected all values in \"expected-outputs\" key to be either 1 or 0.")

    return TruthTableTester(
        input_headers,
        input_sending_pins,
        output_headers,
        output_measuring_pins,
        expected_outputs
    )
