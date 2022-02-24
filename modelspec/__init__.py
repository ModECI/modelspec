__version__ = "0.1.4"

import attr

# Define some aliases for attr.define and other attrs stuff. This should hid attrs from the user a bit.
define = attr.define
has = attr.has
field = attr.field
fields = attr.fields
optional = attr.validators.optional
instance_of = attr.validators.instance_of
in_ = attr.validators.in_
