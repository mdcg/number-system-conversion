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


class BaseConverter:
    @staticmethod
    def process(from_base, to_base, value):
        try:
            from_base_converter = CONVERSION_BASES[from_base]
            to_base_converter = CONVERSION_BASES[to_base]
        except KeyError:
            allowed_bases = ", ".join(CONVERSION_BASES.keys())
            raise Exception(
                f"Operation not allowed. Use the following bases for the calculator to work correctly: {allowed_bases}"  # noqa
            )

        value_to_decimal = int(value, base=from_base_converter.base)
        decimal_to_the_new_base = to_base_converter.function(value_to_decimal)

        return decimal_to_the_new_base
