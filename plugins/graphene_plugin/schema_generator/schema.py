import graphene

class SchemaGenerator:
    def getSchema(query, types):
        return graphene.Schema(query, types)