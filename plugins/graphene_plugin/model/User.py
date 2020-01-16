from airflow.models.user import User as MyUser
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserModel(SQLAlchemyObjectType):
    class Meta:
        model = MyUser
        interfaces = (relay.Node, )
        #exclude_fields = ('conf')

