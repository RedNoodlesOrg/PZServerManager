"""__init__"""

import docker
from pz_server_manager.config import CurrentConfig


def restart():
    """Restart PZ Server"""
    client = docker.DockerClient(base_url=CurrentConfig.DOCKER_URL)
    container = client.containers.get(CurrentConfig.DOCKER_CONTAINER)

    if container is not None:
        container.restart()
    return container is not None
