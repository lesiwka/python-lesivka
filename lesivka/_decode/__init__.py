from . import (
    pre_text,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_6,
    rule_1_7,
    rule_2_1,
    rule_2_2,
    rule_3_1,
    rule_3_2,
)
from ..utils import applier

ORDER = (
    pre_text,
    rule_3_1,
    rule_2_1,
    rule_2_2,
    rule_1_6,
    rule_1_7,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_3_2,
)

apply = applier(*(rule.apply for rule in ORDER))
