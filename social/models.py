import neomodel

class LastName(neomodel.StructuredNode):
    name_day = neomodel.DateProperty()
    last_name = neomodel.StringProperty(unique_index=True)
    user = neomodel.RelationshipFrom('User', 'HAS_NAME', cardinality=neomodel.ZeroOrMore)

class User(neomodel.StructuredNode):
    # uid = UniqueIdProperty()
    email = neomodel.EmailProperty(unique_index=True)
    first_name = neomodel.StringProperty()
    last_name = neomodel.RelationshipTo('LastName', 'HAS_NAME', cardinality=neomodel.OneOrMore)
    friends = neomodel.Relationship('User', 'ARE_FRIENDS')