from argparse import ArgumentParser, Namespace

def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog = "SSL Metrics Density Issues", usage = "Generate metrics based on Density issues"
    )
    parser.add_argument(
        "-j",
        "--json",
        required = True,
        type = str,
        help = "json file created through LOC"
    )