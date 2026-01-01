from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


class McpConfig:

    @staticmethod
    def get_mysql_workbench():
        mysql_server_params = StdioServerParams(
            command="/usr/local/bin/uv",
            args=[
                "--directory",
                "/Users/cmk/myenv/lib/python3.13/site-packages",
                "run",
                "mysql_mcp_server"
            ],
            env={
                "MYSQL_HOST": "localhost",
                "MYSQL_PORT": "3306",
                "MYSQL_USER": "<USER_NAME>",
                "MYSQL_PASSWORD": "<PASSWORD>",
                "MYSQL_DATABASE": "<DB_NAME>"
            } )
        return McpWorkbench( server_params=mysql_server_params )

    @staticmethod
    def get_rest_api_workbench():
        rest_api_server_params = StdioServerParams(
            command="npx",
            args=[
                "-y",
                "dkmaker-mcp-rest-api"
            ],
            env={
                "REST_BASE_URL": "http://localhost:8081",
                "HEADER_Accept": "application/json"
            } )
        return McpWorkbench( rest_api_server_params )
