import os

from servicefoundry import Build, PythonBuild, Resources, Service

API_KEY = input(f"Find the API Key here: https://app.truefoundry.com/settings")


os.environ["TFY_HOST"] = "https://app.truefoundry.tech/"

WORKSPACE = input(f"Set Workspace to deploy to (You can get one from {os.getenv('TFY_HOST')}/workspaces) ")

os.environ["TFY_API_KEY"] = API_KEY 


service = Service(
    name="text-summarizer",
    image=Build(
        build_spec=PythonBuild(
            command="python app.py",
        ),
    ),
    ports=[{"port": 8080}],
    resources=Resources(memory_limit=1000, memory_request=500,
                        cpu_limit=2, cpu_request=1.5),
)
service.deploy(workspace_fqn="tfy-dev-cluster:arsh-dev")
