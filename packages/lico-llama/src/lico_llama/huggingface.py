from pathlib import Path
from dataclasses import dataclass

from huggingface_hub import hf_hub_download, list_repo_files, get_paths_info, RepoFile


@dataclass
class Repo:
    id: str
    paths: list[str]


class HubManager:
    def _show_repo_name(self) -> None:
        print(f"=== {self._repo_info.id} ===")

    def get_paths_info(self) -> None:
        self._show_repo_name()

        for info in get_paths_info(
            repo_id=self._repo_info.id,
            paths=list_repo_files(repo_id=self._repo_info.id)
        ):
            if not isinstance(info, RepoFile):
                continue
            if info.lfs is None:
                continue
            print(f"{info.path}: {info.lfs.size / 1024**3:.2f} GB")

    def download_model(self) -> None:
        self._show_repo_name()

        dest: Path = self._models_dir / self._repo_info.id
        dest.mkdir(parents=True, exist_ok=True)

        for filename in self._repo_info.paths:
            path: str = hf_hub_download(
                repo_id=self._repo_info.id,
                filename=filename,
                local_dir=str(object=dest),
            )
            print(f"Downloaded: {path}")

    def __init__(self) -> None:
        self._models_dir: Path = Path.home() / "develop" / ".llama" / "models"
        self._repo_info = Repo(
            id="unsloth/gemma-4-12B-it-qat-GGUF",
            paths=[
                "mtp-gemma-4-12B-it.gguf",
                "gemma-4-12B-it-qat-UD-Q4_K_XL.gguf",
                "mmproj-BF16.gguf"
            ]
        )


def main() -> None:
    manager = HubManager()
    manager.get_paths_info()
    # manager.download_model()


if __name__ == "__main__":
    main()
