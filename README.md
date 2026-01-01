**Multi-Agent Employee Validation System (AutoGen)**

              This project demonstrates how to use AutoGen multi-agent coordination to validate employee data by comparing database records with a REST API response in a sequential and automated way.
              
              The system uses two AI agents working together:
              
              Database Agent – fetches employee data from MySQL
              
              API Agent – calls a REST API and verifies the data against the database result

📌** High-Level Flow**

              Database Agent fetches employee data from MySQL
              
              Data is structured and shared with the API Agent
              
              API Agent calls the Employee REST API
              
              API response is compared with database data
              
              System confirms whether both data sources match

🧠 Agents Involved
1️⃣ **Database Agent**

              Responsibility
              
              Connects to MySQL database
              
              Reads data from:
              
              employee table
              
              employee_service table
              
              Joins both tables using employee_code
              
              Prepares structured employee data

2️⃣ **API Agent**

              Responsibility
              
              Reads employee data from Database Agent
              
              Compares API response with database data
              
              Confirms result by printing: BOTH ARE SAME


🛠️ **Technologies Used**

Python (asyncio)

AutoGen AgentChat

OpenAI GPT-4o

MySQL

REST API (Spring Boot compatible)

Round-Robin Agent Coordination

