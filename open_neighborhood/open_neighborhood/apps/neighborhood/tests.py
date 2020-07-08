from django.test import TestCase
import json
from graphene_django.utils.testing import GraphQLTestCase
import schema
# Create your tests here.

class MyTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_some_query(self):
        response = self.query(
            '''
            query{
                Person{
                    person_id
                    id_card
                    name
                    birth
                    status
                    created_at 
                }
            }                     
            ''',
            op_name='Person'
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # Add some more asserts if you like
