import neomodel


class User(neomodel.StructuredNode):
    email = neomodel.EmailProperty(unique_index=True)
    first_name = neomodel.StringProperty()
    last_name = neomodel.StringProperty()
    birthday = neomodel.DateProperty()
    password = neomodel.StringProperty(required=True)
    friends = neomodel.Relationship('User', 'ARE_FRIENDS')
    friend_request_sent = neomodel.RelationshipTo('User', 'FRIEND_REQUEST')
    friend_request_received = neomodel.RelationshipFrom('User', 'FRIEND_REQUEST')
