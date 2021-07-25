from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from typing_extensions import Literal

    LiteralStr = Literal
else:
    # a type, that when subscripted, returns `str`.
    class _LiteralStr:
        def __getitem__(self, values):
            return str

    LiteralStr = _LiteralStr()
