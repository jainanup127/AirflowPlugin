from airflow.models.dagrun import DagRun as MyDagrun
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

class DagRunModel(SQLAlchemyObjectType):
    class Meta:
        model = MyDagrun
        interfaces = (relay.Node, )
        exclude_fields = ('conf')
