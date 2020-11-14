from flask_restx import fields

CogUpsertRequest = {
    "name": fields.String(required = True)
}