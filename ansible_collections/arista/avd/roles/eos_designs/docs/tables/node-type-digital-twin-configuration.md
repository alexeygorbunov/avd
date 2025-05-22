<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.defaults.digital_twin") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.digital_twin.enabled") | Boolean |  | `False` |  | Include node(s) in the generated Digital Twin metadata.<br>Digital Twin generation must be globally enabled for this key to take effect. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "<node_type_keys.key>.defaults.digital_twin.platform") | String |  |  | Valid Values:<br>- <code>veos</code><br>- <code>cloudeos</code> | Desired virtual platform.<br>Available option for ACT:<br>  - veos<br>  - cloudeos |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "<node_type_keys.key>.defaults.digital_twin.os_version") | String |  |  |  | Desired version of the Arista EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.defaults.digital_twin.mgmt_ip") | String |  |  | Format: cidr | Management interface IPv4 address of the virtual node.<br>Use this key to override the dynamically generated MGMT IP. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.enabled") | Boolean |  | `False` |  | Include node(s) in the generated Digital Twin metadata.<br>Digital Twin generation must be globally enabled for this key to take effect. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.platform") | String |  |  | Valid Values:<br>- <code>veos</code><br>- <code>cloudeos</code> | Desired virtual platform.<br>Available option for ACT:<br>  - veos<br>  - cloudeos |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.os_version") | String |  |  |  | Desired version of the Arista EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Management interface IPv4 address of the virtual node.<br>Use this key to override the dynamically generated MGMT IP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.enabled") | Boolean |  | `False` |  | Include node(s) in the generated Digital Twin metadata.<br>Digital Twin generation must be globally enabled for this key to take effect. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.platform") | String |  |  | Valid Values:<br>- <code>veos</code><br>- <code>cloudeos</code> | Desired virtual platform.<br>Available option for ACT:<br>  - veos<br>  - cloudeos |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.os_version") | String |  |  |  | Desired version of the Arista EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Management interface IPv4 address of the virtual node.<br>Use this key to override the dynamically generated MGMT IP. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digital_twin</samp>](## "<node_type_keys.key>.nodes.[].digital_twin") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.enabled") | Boolean |  | `False` |  | Include node(s) in the generated Digital Twin metadata.<br>Digital Twin generation must be globally enabled for this key to take effect. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.platform") | String |  |  | Valid Values:<br>- <code>veos</code><br>- <code>cloudeos</code> | Desired virtual platform.<br>Available option for ACT:<br>  - veos<br>  - cloudeos |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;os_version</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.os_version") | String |  |  |  | Desired version of the Arista EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.nodes.[].digital_twin.mgmt_ip") | String |  |  | Format: cidr | Management interface IPv4 address of the virtual node.<br>Use this key to override the dynamically generated MGMT IP. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:
        digital_twin:

          # Include node(s) in the generated Digital Twin metadata.
          # Digital Twin generation must be globally enabled for this key to take effect.
          enabled: <bool; default=False>

          # Desired virtual platform.
          # Available option for ACT:
          #   - veos
          #   - cloudeos
          platform: <str; "veos" | "cloudeos">

          # Desired version of the Arista EOS.
          os_version: <str>

          # Management interface IPv4 address of the virtual node.
          # Use this key to override the dynamically generated MGMT IP.
          mgmt_ip: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>
              digital_twin:

                # Include node(s) in the generated Digital Twin metadata.
                # Digital Twin generation must be globally enabled for this key to take effect.
                enabled: <bool; default=False>

                # Desired virtual platform.
                # Available option for ACT:
                #   - veos
                #   - cloudeos
                platform: <str; "veos" | "cloudeos">

                # Desired version of the Arista EOS.
                os_version: <str>

                # Management interface IPv4 address of the virtual node.
                # Use this key to override the dynamically generated MGMT IP.
                mgmt_ip: <str>
          digital_twin:

            # Include node(s) in the generated Digital Twin metadata.
            # Digital Twin generation must be globally enabled for this key to take effect.
            enabled: <bool; default=False>

            # Desired virtual platform.
            # Available option for ACT:
            #   - veos
            #   - cloudeos
            platform: <str; "veos" | "cloudeos">

            # Desired version of the Arista EOS.
            os_version: <str>

            # Management interface IPv4 address of the virtual node.
            # Use this key to override the dynamically generated MGMT IP.
            mgmt_ip: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>
          digital_twin:

            # Include node(s) in the generated Digital Twin metadata.
            # Digital Twin generation must be globally enabled for this key to take effect.
            enabled: <bool; default=False>

            # Desired virtual platform.
            # Available option for ACT:
            #   - veos
            #   - cloudeos
            platform: <str; "veos" | "cloudeos">

            # Desired version of the Arista EOS.
            os_version: <str>

            # Management interface IPv4 address of the virtual node.
            # Use this key to override the dynamically generated MGMT IP.
            mgmt_ip: <str>
    ```
