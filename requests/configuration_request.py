from flask_restx import fields

ConfigurationUpsertRequest = {
    "key": fields.String(required = True),
    "value": fields.String(required = True),
    "cog_id": fields.Integer(required = True)
}
