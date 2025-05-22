# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._utils import default

if TYPE_CHECKING:
    from . import AvdStructuredConfigMetadataProtocol


class DigitalTwinMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_digital_twin(self: AvdStructuredConfigMetadataProtocol) -> None:
        """
        Set the metadata for Digital Twin feature.

        Only relevant to the use cases where generation of the Digital Twin infrastructure is globally enabled.
        """
        self.structured_config.metadata.digital_twin._update(
            environment=self.inputs.digital_twin.environment,
            node_type=default(self.shared_utils.node_config.digital_twin.platform, self.inputs.digital_twin.platform.fabric, self.shared_utils.platform),
            ip_addr=default(self.shared_utils.node_config.digital_twin.mgmt_ip, self.shared_utils.node_config.mgmt_ip),
            version=default(self.shared_utils.node_config.digital_twin.os_version, self.inputs.digital_twin.os_version.fabric),
            username=default(self.inputs.digital_twin.username.fabric),
            password=default(self.inputs.digital_twin.password.fabric),
        )
