# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2024 Canonical Ltd.
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

"""Tests for Components in Snapcraft's Lifecycle service."""

import pytest

from snapcraft import errors


@pytest.fixture
def lifecycle_service(default_project, fake_services, setup_project):
    setup_project(
        fake_services,
        {**default_project.marshal(), "parts": {"my-part": {"plugin": "nil"}}},
    )
    return fake_services.get("lifecycle")


@pytest.fixture
def extra_project_params(extra_project_params):
    extra_project_params["components"] = {
        "firstcomponent": {
            "type": "test",
            "summary": "first component",
            "description": "lorem ipsum",
            "version": "1.0",
        },
        "secondcomponent": {
            "type": "test",
            "summary": "second component",
            "description": "lorem ipsum",
            "version": "1.0",
        },
    }

    return extra_project_params


@pytest.mark.usefixtures("enable_partitions_feature")
@pytest.mark.usefixtures("default_project")
@pytest.mark.parametrize(
    "component,expected_prime",
    [
        ("firstcomponent", "partitions/component/firstcomponent/prime"),
        ("secondcomponent", "partitions/component/secondcomponent/prime"),
        (None, "prime"),
    ],
)
def test_lifecycle_get_prime_dir(lifecycle_service, component, expected_prime):
    assert (
        lifecycle_service.get_prime_dir(component=component)
        == lifecycle_service._work_dir / expected_prime
    )


@pytest.mark.usefixtures("enable_partitions_feature")
@pytest.mark.usefixtures("default_project")
def test_lifecycle_get_prime_dir_non_existent_component(lifecycle_service):
    """Raise an error when getting the prime directory of a non-existent component."""
    with pytest.raises(errors.SnapcraftError) as raised:
        lifecycle_service.get_prime_dir("bad")

    assert str(raised.value) == (
        "Could not get prime directory for component 'bad' because it does not exist."
    )


@pytest.mark.usefixtures("enable_partitions_feature")
@pytest.mark.usefixtures("default_project")
def test_lifecycle_prime_dirs(lifecycle_service):
    assert lifecycle_service.prime_dirs == {
        None: lifecycle_service._work_dir / "prime",
        "firstcomponent": lifecycle_service._work_dir
        / "partitions/component/firstcomponent/prime",
        "secondcomponent": lifecycle_service._work_dir
        / "partitions/component/secondcomponent/prime",
    }
