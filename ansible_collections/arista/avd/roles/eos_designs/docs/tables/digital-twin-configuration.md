<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>digital_twin</samp>](## "digital_twin") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;environment</samp>](## "digital_twin.environment") | String |  | `act` | Valid Values:<br>- <code>act</code> | Targeted Digital Twin environment. Available options:<br>  - act |
    | [<samp>&nbsp;&nbsp;platform</samp>](## "digital_twin.platform") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric</samp>](## "digital_twin.platform.fabric") | String |  | `veos` | Valid Values:<br>- <code>veos</code><br>- <code>cloudeos</code> | Desired virtual platform for Fabric nodes.<br>Available option for ACT:<br>  - veos<br>  - cloudeos |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "digital_twin.platform.endpoints") | String |  | `veos` | Valid Values:<br>- <code>veos</code><br>- <code>cloudeos</code><br>- <code>generic</code> | Desired virtual platform for Endpoints.<br>Available option for act:<br>  - veos<br>  - cloudeos<br>  - generic (Ubuntu Linux) |
    | [<samp>&nbsp;&nbsp;os_version</samp>](## "digital_twin.os_version") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric</samp>](## "digital_twin.os_version.fabric") | String |  |  |  | Desired OS version for Fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "digital_twin.os_version.endpoints") | String |  |  |  | Desired OS version for Endpoints. |
    | [<samp>&nbsp;&nbsp;mgmt_ipv4_pool</samp>](## "digital_twin.mgmt_ipv4_pool") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric</samp>](## "digital_twin.mgmt_ipv4_pool.fabric") | String |  |  | Format: ipv4_pool | IPv4 address pool to automatically generate MGMT IPv4 addreesses for Fabric nodes.<br>Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "digital_twin.mgmt_ipv4_pool.endpoints") | String |  |  | Format: ipv4_pool | IPv4 address pool to automatically generate MGMT IPv4 addreesses for Endpoints.<br>Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address). |
    | [<samp>&nbsp;&nbsp;username</samp>](## "digital_twin.username") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric</samp>](## "digital_twin.username.fabric") | String |  |  |  | Username for Fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "digital_twin.username.endpoints") | String |  |  |  | Username for Endpoints. |
    | [<samp>&nbsp;&nbsp;password</samp>](## "digital_twin.password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric</samp>](## "digital_twin.password.fabric") | String |  |  |  | Password for Fabric nodes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "digital_twin.password.endpoints") | String |  |  |  | Password for Endpoints. |
    | [<samp>digital_twin_mode</samp>](## "digital_twin_mode") | Boolean |  | `False` |  | Globally enable generation of the Digital Twin metadata (topology, configuration, etc.). |

=== "YAML"

    ```yaml
    digital_twin:

      # Targeted Digital Twin environment. Available options:
      #   - act
      environment: <str; "act"; default="act">
      platform:

        # Desired virtual platform for Fabric nodes.
        # Available option for ACT:
        #   - veos
        #   - cloudeos
        fabric: <str; "veos" | "cloudeos"; default="veos">

        # Desired virtual platform for Endpoints.
        # Available option for act:
        #   - veos
        #   - cloudeos
        #   - generic (Ubuntu Linux)
        endpoints: <str; "veos" | "cloudeos" | "generic"; default="veos">
      os_version:

        # Desired OS version for Fabric nodes.
        fabric: <str>

        # Desired OS version for Endpoints.
        endpoints: <str>
      mgmt_ipv4_pool:

        # IPv4 address pool to automatically generate MGMT IPv4 addreesses for Fabric nodes.
        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        fabric: <str>

        # IPv4 address pool to automatically generate MGMT IPv4 addreesses for Endpoints.
        # Comma separated list of prefixes (IPv4 address/Mask) or ranges (IPv4_address-IPv4_address).
        endpoints: <str>
      username:

        # Username for Fabric nodes.
        fabric: <str>

        # Username for Endpoints.
        endpoints: <str>
      password:

        # Password for Fabric nodes.
        fabric: <str>

        # Password for Endpoints.
        endpoints: <str>

    # Globally enable generation of the Digital Twin metadata (topology, configuration, etc.).
    digital_twin_mode: <bool; default=False>
    ```
