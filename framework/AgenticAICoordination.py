import asyncio
import os

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from framework.agentFactory import AgentFactory

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def main():
    model_client = OpenAIChatCompletionClient( model="gpt-4o" , api_key=OPENAI_API_KEY)
    factory = AgentFactory( model_client )
    database_agent = factory.create_database_agent( system_message=("""
            You are a Database specialist responsible for retrieving employee data.

            Your task:
            1. Connect to the MySQL database 'cmk_mysql'
            2. Query the 'employee' table to get a employee record
            3. Query the 'employee_service' table to get additional employee data
            4. Combine the data from both tables using employee_code column
            5. Prepare all the  data in a structured format so that another agent can understand
            When ready, write: "DATABASE_DATA_READY "
            """) )

    api_agent = factory.create_api_agent(system_message=("""
              You are an API testing specialist with access to REST API

                Your task:
                1. FIRST: Extract the EXACT registration data from DatabaseAgent's EMPLOYEE message
                2. Here is the API details 
                    URL: http://localhost:8081/api/v1/employee/{id}
                    Content-Type: application/json
                   extract the **service ID** from employee , got it from Database Agent and pass it to above uri id field
                   The API returns EmployeeRequest object which contains  same data format extracted in DatabaseAgent's EMPLOYEE message
                   Here is the Response reference
                   public class EmployeeRequest {
                            private Long id;
                            private String name;
                            private String email;
                            private String employeeCode;
                    }
                   compare both rest API result(EmployeeRequest) and EMPLOYEE Message. if both are same then write  "BOTH - DATA ARE SAME"
                
                 3. REGISTRATION PROCESS COMPLETE
                """))


    team = RoundRobinGroupChat( participants=[database_agent, api_agent],
                                termination_condition=TextMentionTermination( "REGISTRATION PROCESS COMPLETE" ) )

    task_result = await Console( team.run_stream( task="Execute Sequential Steps\n\n"

                                                       "STEP 1 - DatabaseAgent (FIRST):\n"
                                                       "Get random  data from database tables and format it clearly.\n\n"

                                                       "STEP 2 - APIAgent:\n"
                                                       "Read api structure, then make employee get api call  using the database data.\n\n"

                                                  ))
    final_message = task_result.messages[-1]
    final_message.content

asyncio.run( main() )