import ubuntu_lint

from debian import deb822
from dput.exceptions import HookException
from dput.interface import CLInterface
from typing import Callable


def call_lint_as_hook(
    lint: Callable[[ubuntu_lint.Context], None],
    changes: deb822.Changes,
    profile: dict,
    interface: CLInterface,
    can_ignore: bool = False,
):
    context = ubuntu_lint.Context(changes=changes)
    try:
        lint(context)
    except ubuntu_lint.LintFailure as e:
        msg = str(e)
        if can_ignore and interface.boolean("WARNING", f"{msg} - ignore?"):
            return
        raise HookException(msg)


def dput_missing_launchpad_bugs_fixed(
    changes: deb822.changes, profile: dict, interface: CLInterface
):
    """
    Hook wrapper around ubuntu_lint.check_missing_launchpad_bugs_fixed.
    """
    call_lint_as_hook(
        ubuntu_lint.check_missing_launchpad_bugs_fixed,
        changes,
        profile,
        interface,
        can_ignore=True,
    )


def dput_missing_ubuntu_maintainer(
    changes: deb822.changes, profile: dict, interface: CLInterface
):
    """
    Hook wrapper around ubuntu_lint.check_missing_ubuntu_maintainer.
    """
    call_lint_as_hook(
        ubuntu_lint.check_missing_launchpad_bugs_fixed,
        changes,
        profile,
        interface,
    )


def dput_missing_git_ubuntu_references(
    changes: deb822.changes, profile: dict, interface: CLInterface
):
    """
    Hook wrapper around ubuntu_lint.check_missing_git_ubuntu_references.
    """
    call_lint_as_hook(
        ubuntu_lint.check_missing_launchpad_bugs_fixed,
        changes,
        profile,
        interface,
        can_ignore=True,
    )


def dput_missing_pending_changelog_entry(
    changes: deb822.changes, profile: dict, interface: CLInterface
):
    """
    Hook wrapper around ubuntu_lint.check_missing_pending_changelog_entry.
    """
    call_lint_as_hook(
        ubuntu_lint.check_missing_launchpad_bugs_fixed,
        changes,
        profile,
        interface,
        can_ignore=True,
    )


def dput_sru_bug_missing_template(
    changes: deb822.changes, profile: dict, interface: CLInterface
):
    """
    Hook wrapper around ubuntu_lint.check_sru_bug_missing_template.
    """
    call_lint_as_hook(
        ubuntu_lint.check_missing_launchpad_bugs_fixed,
        changes,
        profile,
        interface,
        can_ignore=True,
    )


def dput_sru_bug_missing_release_tasks(
    changes: deb822.changes, profile: dict, interface: CLInterface
):
    """
    Hook wrapper around ubuntu_lint.check_sru_bug_missing_release_tasks.
    """
    call_lint_as_hook(
        ubuntu_lint.check_missing_launchpad_bugs_fixed,
        changes,
        profile,
        interface,
    )
