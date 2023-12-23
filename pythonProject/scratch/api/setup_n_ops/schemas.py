# Marshmallow schema -- can turn dictionary or objects into JSON n lists
#    what is definition of an item? .... it has an ID, name, price & a store ID
from marshmallow import Schema, fields


class ItemSchema(Schema):  # Define fields & how they behave for input n output
    id = fields.Str(dump_only=True)  # Should this field b used when loading data,
    # coming from request or when returning data from our API? We only need to
    # use it for returning data. So, set dump_only to True
    name = fields.Str(required=True)  # when we recv data & pass that data thru
    # Schema, it will say u cant pass name thru API. It can only be used for
    # returning data thru API. So, we dont want dump_only, cuz name is something we
    # do recv from JSON payload of a request. Instead we can set isReqd to True
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


# So, we hv defined Schema & ID is NOT going to be used for validation, when data
# is coming from a request, validation will only b performed for other three and
# their data types.


class ItemUpdateSchema(Schema):  # We have diff. data requirements for item update.
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

# How to use this schema to validate incoming data & turning valid data output?
# 1st Validation: parse/check/validate data that client sends us, make sure its
# correct and adheres to Schema. ID fields require NO data validation as those
# will be used only to send data back to client as acknowledgement.
