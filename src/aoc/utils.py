def load_puzzle(path: str) -> str:  # pragma: no cover
    with open(path) as file:
        return file.read()
