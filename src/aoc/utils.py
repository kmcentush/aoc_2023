def multiline_input() -> str:  # pragma: no cover
    print("Input:")
    contents = []
    while True:
        line = input()
        if line == "END":
            break
        else:
            contents.append(line)
    print("Input accepted.")
    return "\n".join(contents)
