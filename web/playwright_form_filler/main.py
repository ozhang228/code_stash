import argparse

from pydantic import BaseModel


class Arguments(BaseModel):
    config_path: str


def parse_arguments() -> Arguments:
    parser = argparse.ArgumentParser(
        description="CLI Tool to simulate filling out a form based on an inputted config file"
    )
    parser.add_argument(
        "-c",
        "--config-file",
        type=str,
        help="The path to the configuration file",
        required=True,
    )

    namespace = parser.parse_args()

    return Arguments(config_path=namespace.config_file)


def main():
    print(parse_arguments())
    pass


if __name__ == "__main__":
    main()
