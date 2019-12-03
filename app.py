from starlette.applications import Starlette
from starlette.config import Config
from starlette.graphql import GraphQLApp

from core import graphql

config = Config(".env")
app = Starlette(debug=True)
app.add_route("/", GraphQLApp(schema=graphql.schema))
