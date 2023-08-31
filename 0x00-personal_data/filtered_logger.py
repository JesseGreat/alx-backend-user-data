#!/usr/bin/env python3
"import regular expressions module"

import re

"function that returns the log message obfuscated:"


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    pattern = rf'(?<={separator})({"|".join(fields)})=[^{separator}]+'
    return re.sub(pattern, rf'\1={redaction}', message)
