from servicefoundry import Build, PythonBuild, Resources, Service
import os

os.environ["TFY_HOST"] = "https://app.truefoundry.tech/"
os.environ["TFY_API_KEY"] = "<your-api-key>"  # replace this


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
