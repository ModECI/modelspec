import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import Any
import sys
import yaml


# Example testing multiple options...


def convert2float(x: Any) -> float:
    print("convert2float {} ({})".format(x, type(x)))
    """Convert to float if not None"""
    if x is not None:
        return float(x)
    else:
        return None


def convert2int(x: Any) -> int:
    print("convert2int {} ({})".format(x, type(x)))
    """Convert to int if not None"""
    if x is not None:
        return int(x)
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
    str_val: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class TopClass(Base):
    """
    A model....

    Args:
        id: The unique id of the thing
        float_like_req: name says it all...
        float_like_optional: name also says it all...
        int_like_optional: name also says it all...
    """

    id: str = field(validator=instance_of(str))
    float_like_req: float = field(
        default=None, validator=instance_of(float), converter=convert2float
    )
    float_like_optional: float = field(
        default=None, validator=optional(instance_of(float)), converter=convert2float
    )
    int_like_optional: int = field(
        default=None, validator=optional(instance_of(int)), converter=convert2int
    )

    mid: MidClassNoId = field(
        default=None, validator=optional(instance_of(MidClassNoId))
    )


tc = TopClass(
    id="MyTest", float_like_req="04"
)  # a string which can be converted to a float...

# tc.float_like_req = 2.01
tc.float_like_optional = 44
# tc.float_like_optional2 = 66
tc.mid = MidClassNoId(int_val=4, str_val="three")


print(tc)

tc.to_yaml_file("test_instance.yaml")
tc.to_json_file("test_instance.json")

if sys.version_info >= (3, 8):
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


print("Generating specification in YAML")
with open("test.specification.yaml", "w") as d:
    d.write(yaml.dump(doc_dict, indent=4, sort_keys=False))
