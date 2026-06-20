# 03 — Windows Security Baseline



## Overview



This lab documents a basic Windows security baseline review performed in a controlled and authorized environment.



The objective was to assess the initial security posture of a Windows system from an operational and defensive perspective, focusing on identity, local users, privileges, network configuration, active services, firewall status, Microsoft Defender, security events, network connections and process correlation.



This lab does not include exploitation, offensive activity or unauthorized testing.



## Objectives



* Review basic Windows system information.

* Identify local users and administrative privileges.

* Check network configuration and active adapters.

* Review relevant running services.

* Verify Windows Firewall status.

* Verify Microsoft Defender status.

* Review basic security events related to authentication.

* Correlate listening ports with PID and processes.

* Document findings using a defensive and operational approach.



## Scope



The review was performed on an owned Windows system used for training purposes.



The activity was limited to observation, documentation and defensive analysis. No processes were terminated and no critical system configuration was modified.



## Areas Reviewed



### System and Identity



The system identity, active user context and general operating system information were reviewed to establish an initial baseline.



### Local Users and Privileges



Local users and local administrator membership were reviewed to understand the privilege model of the system.



This is relevant because excessive administrative privileges can increase the impact of a compromised account.



### Network Configuration



Network interfaces and local network configuration were reviewed to identify active adapters and distinguish physical interfaces from virtual or lab-related interfaces.



### Services and Defensive Components



Relevant running services were reviewed, including Windows security components.



Windows Firewall and Microsoft Defender were checked as part of the defensive baseline.



### Security Events



Windows security events related to authentication were reviewed, including successful and failed logon event categories.



The goal was to understand how Windows records authentication activity and how these events can support basic security monitoring.



### Network Connections and Process Correlation



Listening ports and active connections were reviewed and correlated with process identifiers.



The analysis followed this chain:



Port → PID → Process → Operational interpretation



This helps avoid premature conclusions. A listening port should be interpreted in context by identifying the owning process and understanding its role in the system.



## Defensive Interpretation



The system showed basic defensive capabilities enabled, including Windows Firewall and Microsoft Defender.



No obvious indicator of compromise was identified during this basic review. However, local users, administrative privileges, active services, listening ports and security events should be reviewed periodically as part of a defensive operations process.



The lab reinforces a key principle for security operations: technical evidence must be interpreted in context before assigning risk or recommending action.



## Skills Practiced



* Windows baseline review

* Local user and privilege assessment

* Defensive service review

* Firewall and endpoint protection verification

* Security event review

* Network connection analysis

* Port, PID and process correlation

* Evidence-based documentation

* Operational interpretation of findings



## Key Takeaways



* A Windows security review should begin with a clear baseline.

* Local administrators should be controlled and periodically reviewed.

* Firewall and endpoint protection status are basic defensive indicators.

* Security events provide useful authentication evidence.

* Open ports require context: the owning process must be identified.

* A security operator should document observations, interpret findings and recommend proportionate actions.



## Status



Completed.

