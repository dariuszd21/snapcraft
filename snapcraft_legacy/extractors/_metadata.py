# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2017, 2018 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import Any, Dict, List, Optional, Set, Union

from snapcraft_legacy import yaml_utils


class ExtractedMetadata(yaml_utils.SnapcraftYAMLObject):
    """Collection of metadata extracted from a part."""

    yaml_tag = "!ExtractedMetadata"

    def __init__(
        self,
        *,
        common_id: Optional[str] = None,
        title: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        version: Optional[str] = None,
        grade: Optional[str] = None,
        icon: Optional[str] = None,
        desktop_file_paths: Optional[List[str]] = None,
    ) -> None:
        """Create a new ExtractedMetadata instance.

        :param str: common_id: The common identifier across multiple packaging
            formats
        :param str title: Extracted title
        :param str summary: Extracted summary
        :param str description: Extracted description
        :param str version: Extracted version
        :param str grade: Extracted grade
        :param str icon: Extracted icon
        :param list desktop_file_paths: Extracted desktop file paths
        """  # noqa

        self._data = {}  # type: Dict[str, Union[str, List[str]]]
        self.common_id_list = []  # type: List[str]

        if common_id:
            self._data["common_id"] = common_id
        if title:
            self._data["title"] = title
        if summary:
            self._data["summary"] = summary
        if description:
            self._data["description"] = description
        if version:
            self._data["version"] = version
        if grade:
            self._data["grade"] = grade
        if icon:
            self._data["icon"] = icon
        if desktop_file_paths:
            self._data["desktop_file_paths"] = desktop_file_paths

    def update(self, other: "ExtractedMetadata") -> None:
        """Update this metadata with other metadata.

        Note that the other metadata will take precedence, and may overwrite
        data contained here.

        :param ExtractedMetadata other: Metadata from which to update
        """
        self._data.update(other.to_dict())
        common_id = self.get_common_id()
        if common_id:
            self.common_id_list.append(common_id)

    def get_common_id(self) -> Optional[str]:
        """Return extracted common_id.

        :returns: Extracted common_id
        :rtype: str
        """
        common_id = self._data.get("common_id")
        return str(common_id) if common_id else None

    def get_title(self) -> Optional[str]:
        """Return extracted title.

        :returns: Extracted title
        :rtype: str
        """
        title = self._data.get("title")
        return str(title) if title else None

    def get_summary(self) -> Optional[str]:
        """Return extracted summary.

        :returns: Extracted summary
        :rtype: str
        """
        summary = self._data.get("summary")
        return str(summary) if summary else None

    def get_description(self) -> Optional[str]:
        """Return extracted description.

        :returns: Extracted description
        :rtype: str
        """
        description = self._data.get("description")
        return str(description) if description else None

    def get_version(self) -> Optional[str]:
        """Return extracted version.

        :returns: Extracted version
        :rtype: str
        """
        version = self._data.get("version")
        return str(version) if version else None

    def get_grade(self) -> Optional[str]:
        """Return extracted grade.

        :returns: Extracted grade
        :rtype: str
        """
        grade = self._data.get("grade")
        return str(grade) if grade else None

    def get_icon(self) -> Optional[str]:
        """Return extracted icon.

        :returns: Extracted icon
        :rtype: str
        """
        icon = self._data.get("icon")
        return str(icon) if icon else None

    def get_desktop_file_paths(self) -> Optional[List[str]]:
        """Return extracted desktop files paths.

        :returns: Extracted desktop files paths
        :rtype: list
        """
        desktop_file_paths = self._data.get("desktop_file_paths")
        return list(desktop_file_paths) if desktop_file_paths else None

    def to_dict(self) -> Dict[str, Union[str, List[str]]]:
        """Return all extracted metadata.

        :returns: All extracted metadata in dict form.
        :rtype: dict
        """
        return self._data.copy()

    def overlap(self, other: "ExtractedMetadata") -> Set[str]:
        """Return all overlapping keys between this and other.

        :returns: All overlapping keys between this and other
        :rtype: set
        """
        return set(self._data.keys() & other.to_dict().keys())

    def __str__(self) -> str:
        return str(self._data)

    def __eq__(self, other: Any) -> bool:
        if type(other) is type(self):
            return self._data == other._data

        return False

    def __len__(self) -> int:
        return self._data.__len__()
