import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

# Example testing multiple option...


@modelspec.define
class TopClass(Base):
    """
    A model....

    Args:
        id: The unique id of the thing
        float_or_int: name says it all
    """

    id: str = field(validator=instance_of(str))
    float_like_req: int = field(
        default=None, validator=instance_of(float), converter=float
    )
    float_optional: int = field(default=None, validator=optional(instance_of(float)))


tc = TopClass(id="MyTest", float_like_req="03")
tc.float_optional = 2.3


print(tc)

tc.to_yaml_file("test_instance.yaml")

doc_md = tc.generate_documentation(format="markdown")

with open("test.md", "w") as d:
    d.write(doc_md)


print("\nGenerating specification in dict form")
doc_dict = tc.generate_documentation(format="dict")

import yaml

print("Generating specification in YAML")
with open("test.specification.yaml", "w") as d:
    d.write(yaml.dump(doc_dict, indent=4, sort_keys=False))
