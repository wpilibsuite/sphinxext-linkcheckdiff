import pytest


@pytest.mark.sphinx("linkcheckdiff", testroot="file-added")
def test_file_added(app_init_repo):
    app_init_repo.build()

    assert (app_init_repo.outdir / "output.txt").exists()
    content = (app_init_repo.outdir / "output.txt").read_text()

    assert "https://www.google.com/thisisabadurl" in content
    assert content.count(".rst") == 1


@pytest.mark.sphinx("linkcheckdiff", testroot="file-added-no-link")
def test_file_added_no_link(app_init_repo):
    app_init_repo.build()
    assert (app_init_repo.outdir / "output.txt").exists()
    content = (app_init_repo.outdir / "output.txt").read_text()
    assert len(content) == 0


@pytest.mark.sphinx("linkcheckdiff", testroot="file-changed-link")
def test_file_changed_link(app_init_repo):
    app_init_repo.build()

    assert (app_init_repo.outdir / "output.txt").exists()
    content = (app_init_repo.outdir / "output.txt").read_text()

    assert "python.org" not in content
    assert "wpilib.org" in content
    assert content.count(".rst") == 1


@pytest.mark.sphinx("linkcheckdiff", testroot="file-removed")
def test_file_removed(app_init_repo):
    app_init_repo.build()
    assert (app_init_repo.outdir / "output.txt").exists()
    content = (app_init_repo.outdir / "output.txt").read_text()
    assert len(content) == 0


@pytest.mark.sphinx("linkcheckdiff", testroot="files-added-some-link")
def test_files_added_some_link(app_init_repo):
    app_init_repo.build()

    assert (app_init_repo.outdir / "output.txt").exists()
    content = (app_init_repo.outdir / "output.txt").read_text()

    assert "Not Found for url: https://www.google.com/thisisabadurl" in content
    assert content.count(".rst") == 1


@pytest.mark.sphinx("linkcheckdiff", testroot="non-src-file-changed")
def test_non_src_file_changes(app_init_repo):
    app_init_repo.build()
    assert (app_init_repo.outdir / "output.txt").exists()
    content = (app_init_repo.outdir / "output.txt").read_text()
    assert len(content) == 0
