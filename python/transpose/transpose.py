def transpose(lines):
    lines = lines.split("\n")

    for i in range(len(lines) - 1):
        if len(lines[-1 - i - 1]) < len(lines[-1 - i]):
            lines[-1 - i - 1] = lines[-1 - i - 1].ljust(len(lines[-1 - i]))

    max_len = max(len(line) for line in lines)

    out = ["" for _ in range(max_len)]

    for i in range(max_len):
        for j, line in enumerate(lines):
            out[i] += line[i] if i < len(line) else ""

    return "\n".join(out)
