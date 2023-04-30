from dataclasses import dataclass


@dataclass
class Converter:
    base: int
    function: callable


CONVERSION_BASES = {
    "DECIMAL": Converter(10, int),
    "BINARY": Converter(2, bin),
    "OCTAL": Converter(8, oct),
    "HEXADECIMAL": Converter(16, hex),
}


class BaseConverter:
    @staticmethod
    def process(from_base: str, to_base: str, value: str):
        try:
            from_base_converter = CONVERSION_BASES[from_base]
            to_base_converter = CONVERSION_BASES[to_base]
        except KeyError:
            raise Exception(
                f"Operation not allowed. Use the following bases for the calculator to work correctly: {', '.join(CONVERSION_BASES.keys())}"
            )

        value_to_decimal = int(value, from_base_converter.base)
        decimal_to_the_new_base = to_base_converter.function(value_to_decimal)

        return decimal_to_the_new_base
