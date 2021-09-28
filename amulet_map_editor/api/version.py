from __future__ import annotations

import re
from dataclasses import dataclass
from enum import IntEnum
from typing import Tuple

"""
VERSION_REGEX Documentation

    This is not a documentation of regular expression syntax, just documentation on the subsequences that this regular expression looks for
    For an in-depth guide on regular expressions, see here: https://www.debuggex.com/cheatsheet/regex/python
    
    Our version scheme allows for an optional "v" prefix, so that subsequence is tested by "v?"
    
    Since we use the Semantic Versioning scheme, our version numbers follow this format: <major>.<minor>.<patch>
    with the <patch> number being optional (only if it's value would be 0 for that version)
    That is tested by "(?P<major>\d+)\.(?P<minor>\d+)(\.(?P<patch>\d+))?"
    
    - For the major and minor numbers, "(?P<major>\d+)" will match any non-zero number of digits and group them under the
        "major" group (in this instance)
    - "\." will then match the separating "." character
    - Since the patch number is optional, "(\.(?P<patch>\d+))?" is used instead, the second "." is included in the 
        optional group, but other wise the capturing group is the same as the major/minor numbers
        
    We then use an optional release type flag to denote whether the release is a beta or alpha release and it's number:
    "((a(?P<alpha>\d+))|(b(?P<beta>\d+)))?"
    
    For our nightly builds, we also denote a unique build number with the prefix of ".dev": "(\.dev(?P<devnum>\d{12}))?"
    
    Finally, our version scheme also denotes when Amulet is being ran from source, while this information isn't
    necessarily used for update checking, we use it to determine if the update dialog should be shown. If a commit 
    hash/count is found in the version string of the current Amulet instance, the dialog is not shown. Our regular 
    expression uses the following to detect that subsequence: 
        "(\+(?P<commit_count>\d+)\.g(?P<commit_hash>[a-z\d]+)(\.dirty)?)?"
        
    - "commit_count" group signifies the number of commits since the last release
    - "commit_hash" group is the current commit hash
    - ".dirty" denotes whether uncommitted changes have been made 
"""
VERSION_REGEX = re.compile(
    r"^v?(?P<major>\d+)\.(?P<minor>\d+)(\.(?P<patch>\d+))?(\.(?P<bug_fix>\d+))?((a(?P<alpha>\d+))|(b(?P<beta>\d+)))?(\.dev(?P<devnum>\d{12}))?(\+(?P<commit_count>\d+)\.g(?P<commit_hash>[a-z\d]+)(\.dirty)?)?$"
)


class Release(IntEnum):
    FULL = 0
    BETA = -1
    ALPHA = -2


@dataclass
class Version:
    release_stage: int
    major: int
    minor: int
    patch: int
    bug_fix: int = -1  # Don't use this.
    alpha_number: int = -1
    beta_number: int = -1
    nightly_timestamp: int = -1
    has_commit_hash: bool = False

    @classmethod
    def from_string(cls, version_string: str) -> Version:
        """Parse the version into a more usable format

        :param version_string: The version string. Eg 1.2 or 1.2.3.4 or 1.2.3.4b0
        :return: A Version object from the parsed version string
        """
        version_match = VERSION_REGEX.match(version_string)
        if version_match:
            v = version_match.groupdict()
            major, minor = int(v["major"]), int(v["minor"])
            if v["patch"] is None:
                patch = 0
            else:
                patch = int(v["patch"])
            version = cls(Release.FULL, major, minor, patch)

            if v.get("bug_fix") is not None:
                version.bug_fix = int(v["bug_fix"])
            if v.get("alpha") is not None:
                version.release_stage = Release.ALPHA
                version.alpha_number = int(v["alpha"])
            elif v.get("beta") is not None:
                version.release_stage = Release.BETA
                version.beta_number = int(v["beta"])
                if v.get("devnum") is not None:
                    version.nightly_timestamp = int(v["devnum"])

            if v.get("commit_hash") is not None:
                version.has_commit_hash = True
            return version

        raise Exception(f"Invalid version string {version_string}")

    def __gt__(self, other: Version):
        if self.version_tuple > other.version_tuple:
            return True
        elif self.version_tuple == other.version_tuple:
            if self.release_stage > other.release_stage:
                return True
            elif self.release_stage == other.release_stage:
                if self.release_stage == Release.ALPHA:
                    return self.alpha_number > other.alpha_number
                elif self.release_stage == Release.BETA:
                    if self.beta_number > other.beta_number:
                        return True
                    elif (
                        self.beta_number == other.beta_number and self.beta_number != -1
                    ):
                        return self.nightly_timestamp > other.nightly_timestamp
        return False

    def __ge__(self, other: Version):
        return self > other or self == other

    @property
    def version_triplet(self) -> Tuple[int, int, int]:
        return self.major, self.minor, self.patch

    @property
    def version_tuple(self) -> Tuple[int, ...]:
        if self.bug_fix >= 0:
            return self.major, self.minor, self.patch, self.bug_fix
        else:
            return self.major, self.minor, self.patch

    def __str__(self):
        v = ".".join(str(n) for n in self.version_tuple)
        if self.release_stage == Release.ALPHA:
            v += f"a{self.alpha_number}"
        elif self.release_stage == Release.BETA:
            v += f"b{self.beta_number}"
        if self.nightly_timestamp >= 0:
            v += f".dev{self.nightly_timestamp}"
        return v
