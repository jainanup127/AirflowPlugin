import graphene
from airflow.plugins_manager import AirflowPlugin
from airflow.settings import Session
from flask_graphql import GraphQLView
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from plugins.graphene_plugin.config import *
from plugins.graphene_plugin.model.Dag import DagModel
from plugins.graphene_plugin.model.DagRun import DagRunModel
from plugins.graphene_plugin.model.User import UserModel
from plugins.graphene_plugin.schema_generator.schema import SchemaGenerator as schemaGenerator


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_dags = SQLAlchemyConnectionField(DagModel)
    all_dagruns = SQLAlchemyConnectionField(DagRunModel)
    all_users = SQLAlchemyConnectionField(UserModel)

#schema = graphene.Schema(query=Query, types=[DagModel,DagRunModel,UserModel])
schema = schemaGenerator.getSchema(Query, None)

myapi.add_url_rule(
    '/dags',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,                                                         
        get_context=lambda: {'session':Session()}
    )
)

class AirflowTestPlugin(AirflowPlugin):
    name = "GraphQLAPIsv2"
    # operators = []
    flask_blueprints = [myapi]
    # hooks = []
    # executors = []
    # admin_views = [v]    
    #appbuilder_views = [v_appbuilder_package]
