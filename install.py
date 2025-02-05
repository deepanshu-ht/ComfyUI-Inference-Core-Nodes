import sys
import subprocess

from pathlib import Path
from typing import List

PARENT_DIR = Path(__file__).parent


def pip_install(args: List[str]) -> None:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", ] + args, cwd=PARENT_DIR
    )


def try_get_cuda_version() -> str | None:
    try:
        import torch
        return torch.version.cuda
    except ImportError or AttributeError:
        return None


def main() -> None:

    cuda_version = try_get_cuda_version()
    if cuda_version is not None:
        pip_install(["-e", ".[cuda]"])
    else:
        # Default install
        pip_install(["-e", ".[cpu]"])


if __name__ == "__main__":
    main()
