from typing import Any, Dict, List, Set, Tuple, overload
import sphinx.builders.linkcheck
from sphinx.application import Sphinx
from docutils.nodes import Node
import subprocess
from pathlib import Path


class CheckExternalLinksDiffBuilder(
    sphinx.builders.linkcheck.CheckExternalLinksBuilder
):
    name = "linkcheckdiff"
    epilog = "Look for any errors in the above output or in %(outdir)s /output.txt"

    def init(self) -> None:
        super().init()

        self.path_to_git_repo = subprocess.check_output(
            f"git -C {self.app.srcdir} rev-parse --show-toplevel", shell=True
        ).decode("utf-8")

        # run git diff
        self.changed_files = subprocess.check_output(
            f"git -C {self.app.srcdir} diff --name-only  {self.app.config.linkcheckdiff_branch}",
            shell=True,
        )
        # splitlines
        self.changed_files = self.changed_files.splitlines()
        # convert to utf-8
        self.changed_files = [
            filename.decode("utf-8") for filename in self.changed_files
        ]
        # convert to path
        self.changed_files = [Path(filename.strip()) for filename in self.changed_files]
        # strip extension
        self.changed_files = [
            Path(filename).with_suffix("") for filename in self.changed_files
        ]
        # to absolute path
        self.changed_files = [
            Path(self.path_to_git_repo.strip()) / filename
            for filename in self.changed_files
        ]
        # to set
        self.changed_files = set(self.changed_files)

    def write_doc(self, docname: str, doctree: Node) -> None:
        if Path(self.app.srcdir) / docname in self.changed_files:
            super().write_doc(docname, doctree)


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_builder(CheckExternalLinksDiffBuilder)
    app.add_config_value("linkcheckdiff_branch", "", None)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
