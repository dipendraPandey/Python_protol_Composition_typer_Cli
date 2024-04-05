import typer

from protocols_and_composition_in_python.logger import std_out_logger
from protocols_and_composition_in_python.add.add_protocal_implementation import AddService, AddServiceProtocol, LoggingAddService, TimingAddService


def main(a: int, b: int, debug: bool = False, timing: bool = False) -> None:
    """
    Adding 'a' to 'b' made easy!
    """
    service: AddServiceProtocol = AddService()
    if timing:
        service = TimingAddService(service=service, logger=std_out_logger("timing"))
    if debug:
        service = LoggingAddService(service=service, logger=std_out_logger("logging"))
    print(service.add(a, b))


if __name__ == "__main__":
    typer.run(main)