from marshmallow import Schema, fields


class CustomerSchema(Schema):
    customer_id = fields.Integer(dump_only=True)
    customer_name = fields.String()
    city = fields.String()

class ProductSchema(Schema):
    product_id = fields.Integer(dump_only=True)
    product_name = fields.String()
    category = fields.String()

class TargetSchema(Schema):
    customer_id = fields.Integer()
    ontime_target_percent = fields.Float()
    infull_target_percent = fields.Float()
    otif_target_percent = fields.Float()

class OrderLineSchema(Schema):
    order_id = fields.String()
    order_placement_date = fields.Date()
    customer_id = fields.Integer()
    product_id = fields.Integer()
    order_qty = fields.Integer()
    agreed_delivery_date = fields.Date()
    actual_delivery_date = fields.Date()
    delivery_qty = fields.Integer()
    in_full = fields.Boolean()
    on_time = fields.Boolean()
    on_time_in_full = fields.Boolean()

class OrderAggregateSchema(Schema):
    order_id = fields.String()
    customer_id = fields.Integer()
    order_placement_date = fields.Date()
    on_time = fields.Boolean()
    in_full = fields.Boolean()
    otif = fields.Boolean()