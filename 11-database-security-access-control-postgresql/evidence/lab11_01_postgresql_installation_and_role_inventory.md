# LAB 11.1 — PostgreSQL Installation and Initial Role Inventory

## Scope

Local PostgreSQL installation in controlled Ubuntu lab.

- No external targets.
- No third-party systems.
- No public IPs.
- No real credentials.
- No unauthorized activity.

## Objective

Install PostgreSQL locally and perform the first role inventory.

## Why this matters

Database security starts with identity, role and privilege inventory before granting access to data.

This first mission confirms that the database engine exists, the service is active, a PostgreSQL cluster is online, and the initial administrative role inventory can be reviewed.

## Network note

APT update initially failed because the Ubuntu VM had no default route and no DHCP lease. Network connectivity was restored before installing PostgreSQL.

## Commands covered

```bash
cat /etc/os-release
hostname
whoami
ip -br addr
ip route
which psql
dpkg -l | grep -i postgresql
sudo systemctl status postgresql --no-pager
pg_lsclusters
sudo -iu postgres psql -c "SELECT version();"
sudo -iu postgres psql -c "SELECT current_user;"
sudo -iu postgres psql -c "\du"
```

## Evidence generation time

```text
$ date

Thu Jul  2 11:35:31 AM UTC 2026

[exit_status=0]
```

## Hostname

```text
$ hostname

vbox

[exit_status=0]
```

## Current Linux user

```text
$ whoami

vbox

[exit_status=0]
```

## Operating system

```text
$ cat /etc/os-release

PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy

[exit_status=0]
```

## Network interfaces

```text
$ ip -br addr

lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp0s3           UP             fe80::a00:27ff:feaa:c91f/64 
enp0s8           UP             10.0.3.15/24 fd17:625c:f037:3:a00:27ff:feda:8f47/64 fe80::a00:27ff:feda:8f47/64 

[exit_status=0]
```

## Routing table

```text
$ ip route

default via 10.0.3.2 dev enp0s8 
10.0.3.0/24 dev enp0s8 proto kernel scope link src 10.0.3.15 

[exit_status=0]
```

## PostgreSQL binary

```text
$ which psql

/usr/bin/psql

[exit_status=0]
```

## Installed PostgreSQL packages

```text
$ dpkg -l | grep -i postgresql || true

ii  libpq5:amd64                           14.23-0ubuntu0.22.04.1                  amd64        PostgreSQL C client library
ii  postgresql-14                          14.23-0ubuntu0.22.04.1                  amd64        The World's Most Advanced Open Source Relational Database
ii  postgresql-client                      14+238                                  all          front-end programs for PostgreSQL (supported version)
ii  postgresql-client-14                   14.23-0ubuntu0.22.04.1                  amd64        front-end programs for PostgreSQL 14
ii  postgresql-client-common               238                                     all          manager for multiple PostgreSQL client versions
ii  postgresql-common                      238                                     all          PostgreSQL database-cluster manager
ii  postgresql-contrib                     14+238                                  all          additional facilities for PostgreSQL (supported version)

[exit_status=0]
```

## PostgreSQL service status

```text
$ sudo systemctl status postgresql --no-pager

● postgresql.service - PostgreSQL RDBMS
     Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
     Active: active (exited) since Wed 2026-07-01 16:38:49 UTC; 18h ago
    Process: 4672 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
   Main PID: 4672 (code=exited, status=0/SUCCESS)
        CPU: 13ms

Jul 01 16:38:49 vbox systemd[1]: Starting PostgreSQL RDBMS...
Jul 01 16:38:49 vbox systemd[1]: Finished PostgreSQL RDBMS.

[exit_status=0]
```

## PostgreSQL cluster status

```text
$ pg_lsclusters

Ver Cluster Port Status Owner    Data directory              Log file
14  main    5432 online postgres /var/lib/postgresql/14/main /var/log/postgresql/postgresql-14-main.log

[exit_status=0]
```

## PostgreSQL version

```text
$ sudo -iu postgres psql -c "SELECT version();"

                                                                 version                                                                  
------------------------------------------------------------------------------------------------------------------------------------------
 PostgreSQL 14.23 (Ubuntu 14.23-0ubuntu0.22.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0, 64-bit
(1 row)


[exit_status=0]
```

## Current database user

```text
$ sudo -iu postgres psql -c "SELECT current_user;"

 current_user 
--------------
 postgres
(1 row)


[exit_status=0]
```

## Initial role inventory

```text
$ sudo -iu postgres psql -c "\du"

                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}


[exit_status=0]
```

## Analyst interpretation

- PostgreSQL is installed locally in the Ubuntu lab if the PostgreSQL binary exists.
- The database service is valid if systemctl shows the PostgreSQL service as active.
- The cluster is valid if pg_lsclusters shows an online cluster.
- The administrative database context is valid if current_user returns postgres.
- The first security task is identity and role inventory.
- No custom lab database has been created yet.
- No custom application users, analyst users or auditor users have been created yet.
- No permissions have been granted to lab users yet.

## Security lesson

Database security is not only about SQL queries. It is about proving who connects, which role is active, which object is accessed, which privilege authorizes the action, and how the result is evidenced.

## Status

Lab 11.1 completed if PostgreSQL is installed, the service is active, the cluster is online, and the initial role inventory is visible.

Next step: create the bank_lab database, define secure ownership, create schemas and build the first access-control model.
