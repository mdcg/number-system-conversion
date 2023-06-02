from dataclasses import dataclass


@dataclass
class Converter:
    base: int
    function: callable


CONVERSION_BASES = {
    "DECIMAL": Converter(
        base=10,
        function=int,
    ),
    "BINARY": Converter(
        base=2,
        function=bin,
    ),
    "OCTAL": Converter(
        base=8,
        function=oct,
    ),
    "HEXADECIMAL": Converter(
        base=16,
        function=hex,
    ),
}

ALLOWED_BASES = ", ".join(CONVERSION_BASES.keys())


class BaseConverter:
    @staticmethod
    def process(from_base: str, to_base: str, value: str) -> str:
        try:
            from_base_converter = CONVERSION_BASES[from_base]
            to_base_converter = CONVERSION_BASES[to_base]
        except KeyError:
            raise Exception(
                f"Operation not allowed. Use the following bases for the calculator to work correctly: {ALLOWED_BASES}"  # noqa
            )

        value_to_decimal = int(value, base=from_base_converter.base)

        return to_base_converter.function(value_to_decimal)
