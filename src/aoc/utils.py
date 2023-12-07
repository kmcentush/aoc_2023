def multiline_input() -> str:  # pragma: no cover
    print("Input:")
    contents = []
    while True:
        line = input()
        if line:
            contents.append(line)
        else:
            break
    return "\n".join(contents)
