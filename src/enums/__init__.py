import enum


class FieldType(enum.Enum):
    STRING = "_string"
    DATE = "_date"
    INT = "_int"
    DOUBLE = "_double"


class HierarchyRelationType(enum.Enum):
    ALLOWED = "_allowed"
    NOT_ALLOWED = "_notAllowed"
    DEFAULT = "_default"
