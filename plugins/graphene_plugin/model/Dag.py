from airflow.models.dag import DagModel as MyDag
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

class DagModel(SQLAlchemyObjectType):
    class Meta:
        model = MyDag
        interfaces = (relay.Node, )
        #exclude_fields = ("last_scheduler_run",'last_pickled','last_expired','schedule_interval')
