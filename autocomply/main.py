from typing import Optional

import click

from autocomply.action_system import ActionSystem
from autocomply.logger import setup_logger

logger = setup_logger(__name__)


@click.command()
@click.option("--no-audio", is_flag=True, help="Disable audio capture")
@click.option("--debug", is_flag=True, help="Run in debug mode using test image")
@click.option("--task-profile", "-t", help="Path to task profile YAML file")
@click.option("--instructions", "-i", help="Override task instructions")
def main(
    no_audio: bool = False,
    debug: bool = False,
    task_profile: Optional[str] = None,
    instructions: Optional[str] = None,
):
    action_system = ActionSystem(
        task_profile=task_profile,
        instructions=instructions,
        no_audio=no_audio,
        debug=debug,
    )
    action_system.run()


if __name__ == "__main__":
    main()
