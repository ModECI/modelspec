import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from modelspec.utils import load_json
from typing import List

# Example testing multiple options...

from typing import Any


def convert2float(x: Any) -> float:
    print("Converting {} ({})".format(x, type(x)))
    """Convert to float if not None"""
    if x is not None:
        return float(x)
    else:
        return None


@modelspec.define
class MidClassNoId(Base):
    """
    A model....

    Args:
        int_val: name says it all...
        str_val: name says it all...
    """

    int_val: int = field(default=None, validator=instance_of(int))
    str_val: int = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class TopClass(Base):
    """
    A model....

    Args:
        id: The unique id of the thing
        float_like_req: name says it all...
        float_like_optional: name also says it all...
        float_like_optional2: name also says it all...
    """

    id: str = field(validator=instance_of(str))
    float_like_req: int = field(
        default=None, validator=instance_of(float), converter=convert2float
    )
    float_like_optional: int = field(
        default=None, validator=optional(instance_of(float)), converter=convert2float
    )
    float_like_optional2: int = field(
        default=None, validator=optional(instance_of(float)), converter=convert2float
    )

    mid: MidClassNoId = field(
        default=None, validator=optional(instance_of(MidClassNoId))
    )


tc = TopClass(
    id="MyTest", float_like_req="04"
)  # a string which can be converted to a float...

# tc.float_like_req = 2.01
tc.float_like_optional = 44
tc.float_like_optional2 = 66
# tc.mid = MidClassNoId(int_val=4, str_val="three")


print(tc)

tc.to_yaml_file("test_instance.yaml")
tc.to_json_file("test_instance.json")
tc.to_xml_file("test_instance.xml")

str_b4 = str(tc)

str_json_after = TopClass.from_json_file("test_instance.json")
print(str_json_after)
str_yaml_after = TopClass.from_yaml_file("test_instance.yaml")
print(str_yaml_after)

doc_md = tc.generate_documentation(format="markdown")

with open("test.md", "w") as d:
    d.write(doc_md)


print("\nGenerating specification in dict form")
doc_dict = tc.generate_documentation(format="dict")

import yaml

print("Generating specification in YAML")
with open("test.specification.yaml", "w") as d:
    d.write(yaml.dump(doc_dict, indent=4, sort_keys=False))
