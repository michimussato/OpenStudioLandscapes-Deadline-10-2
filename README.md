[![ Logo OpenStudioLandscapes ](https://github.com/michimussato/OpenStudioLandscapes/raw/main/media/images/logo128.png)](https://github.com/michimussato/OpenStudioLandscapes)

***

1. [Feature: OpenStudioLandscapes-Deadline-10-2](#feature-openstudiolandscapes-deadline-10-2)
   1. [Brief](#brief)
   2. [Clone](#clone)
      1. [Clone and Install](#clone-and-install)
   3. [Configure](#configure)
      1. [Default Configuration](#default-configuration)
   4. [Local Development/Unit Testing/Debugging](#local-developmentunit-testingdebugging)
2. [External Resources](#external-resources)
   1. [Get Deadline](#get-deadline)
      1. [Get Deadline 10.2](#get-deadline-102)
      2. [Instructions](#instructions)
   2. [Documentation](#documentation)
      1. [User Manual](#user-manual)
      2. [Scripting Reference](#scripting-reference)
      3. [Python Reference](#python-reference)
      4. [Information on Usage Based Licensing (UBL)](#information-on-usage-based-licensing-ubl)
   3. [Known Issues](#known-issues)
      1. [Could not find the Qt platform plugin "wayland"](#could-not-find-the-qt-platform-plugin-wayland)
3. [Community](#community)

***

This `README.md` was dynamically created with [OpenStudioLandscapesUtil-ReadmeGenerator](https://github.com/michimussato/OpenStudioLandscapesUtil-ReadmeGenerator).

***

# Feature: OpenStudioLandscapes-Deadline-10-2

## Brief

This is an extension to the OpenStudioLandscapes ecosystem. The full documentation of OpenStudioLandscapes is available [here](https://github.com/michimussato/OpenStudioLandscapes).

> [!NOTE]
> 
> You feel like writing your own Feature? Go and check out the 
> [OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template).

## Clone

Clone this repository into `OpenStudioLandscapes/.features` (assuming the current working directory to be the Git repository root `./OpenStudioLandscapes`):

```shell
# cd OpenStudioLandscapes
source .venv/bin/activate
openstudiolandscapes clone-feature --repo=https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2.git
deactivate
# Check the resulting console output for installation instructions
```

### Clone and Install

```shell
# cd OpenStudioLandscapes
source .venv/bin/activate
openstudiolandscapes clone-feature --repo=https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2.git \
    && pip install --editable ./.features/OpenStudioLandscapes-Deadline-10-2
deactivate
```

For more info on `pip` see [VCS Support of `pip`](https://pip.pypa.io/en/stable/topics/vcs-support/).

## Configure

OpenStudioLandscapes will search for a local config store. The default location is `~/.config/OpenStudioLandscapes/config-store/` but you can specify a different location if you need to.

> [!TIP]
> 
> To specify a config store location different from
> the default location, check out the OpenStudioLandscapes 
> [CLI Section](https://github.com/michimussato/OpenStudioLandscapes#cli)
> to find out how to do that.

A local config store location will be created if it doesn't exist, together with the `config.yml` files for each individual Feature.

> [!TIP]
> 
> The config store root will be initialized as a local Git
> controlled repository. This makes it easy to track changes
> you made to the `config.yml`.

The following settings are available in `OpenStudioLandscapes-Deadline-10-2` and are based on [`OpenStudioLandscapes-Deadline-10-2/tree/main/src/OpenStudioLandscapes/Deadline_10_2/config/models.py`](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2/tree/main/src/OpenStudioLandscapes/Deadline_10_2/config/models.py).

### Default Configuration

<details open>
<summary><code>config.yml</code></summary>


```yaml
apt_packages:
  default:
  - bzip2
  items: {}
  title: Apt Packages
  type: array
compose_scope:
  default: default
  examples:
  - default
  - license_server
  - worker
  title: Compose Scope
  type: string
deadline_10_2_APPLICATION_STARTUP_PORT:
  default: 17006
  exclusiveMinimum: 0
  title: Deadline 10 2 Application Startup Port
  type: integer
deadline_10_2_AUTO_CONFIGURATION_PORT:
  default: 17001
  exclusiveMinimum: 0
  title: Deadline 10 2 Auto Configuration Port
  type: integer
deadline_10_2_DEFAULT_DBPATH_CONTAINER:
  default: /data/db
  format: path
  title: Deadline 10 2 Default Dbpath Container
  type: string
deadline_10_2_DISABLE_LOCAL_PULSE:
  default: false
  title: Deadline 10 2 Disable Local Pulse
  type: boolean
deadline_10_2_DISABLE_LOCAL_WORKER:
  default: true
  title: Deadline 10 2 Disable Local Worker
  type: boolean
deadline_10_2_LAUNCHER_LISTENING_PORT:
  default: 17000
  exclusiveMinimum: 0
  title: Deadline 10 2 Launcher Listening Port
  type: integer
deadline_10_2_LICENSE_FORWARDER_LISTENING_PORT:
  default: 17003
  exclusiveMinimum: 0
  title: Deadline 10 2 License Forwarder Listening Port
  type: integer
deadline_10_2_ME_CONFIG_BASICAUTH_PASSWORD:
  default: web
  title: Deadline 10 2 Me Config Basicauth Password
  type: string
deadline_10_2_ME_CONFIG_BASICAUTH_USERNAME:
  default: web
  title: Deadline 10 2 Me Config Basicauth Username
  type: string
deadline_10_2_ME_CONFIG_MONGODB_PORT:
  default: 21017
  exclusiveMinimum: 0
  title: Deadline 10 2 Me Config Mongodb Port
  type: integer
deadline_10_2_ME_CONFIG_MONGODB_SERVER:
  default: mongodb-10-2
  title: Deadline 10 2 Me Config Mongodb Server
  type: string
deadline_10_2_ME_CONFIG_MONGODB_URL:
  default: mongodb://admin:pass@localhost:21017/db?ssl=false
  title: Deadline 10 2 Me Config Mongodb Url
  type: string
deadline_10_2_ME_CONFIG_OPTIONS_EDITORTHEME:
  default: darcula
  title: Deadline 10 2 Me Config Options Editortheme
  type: string
deadline_10_2_MONGODB_INSIDE_CONTAINER:
  default: false
  title: Deadline 10 2 Mongodb Inside Container
  type: boolean
deadline_10_2_MONGO_DB_HOST:
  default: mongodb-10-2
  title: Deadline 10 2 Mongo Db Host
  type: string
deadline_10_2_MONGO_DB_NAME:
  default: deadline10db
  title: Deadline 10 2 Mongo Db Name
  type: string
deadline_10_2_MONGO_DB_PORT_CONTAINER:
  default: 21017
  exclusiveMinimum: 0
  title: Deadline 10 2 Mongo Db Port Container
  type: integer
deadline_10_2_MONGO_DB_PORT_HOST:
  default: 21017
  exclusiveMinimum: 0
  title: Deadline 10 2 Mongo Db Port Host
  type: integer
deadline_10_2_MONGO_EXPRESS_PORT_CONTAINER:
  default: 8081
  exclusiveMinimum: 0
  title: Deadline 10 2 Mongo Express Port Container
  type: integer
deadline_10_2_MONGO_EXPRESS_PORT_HOST:
  default: 8181
  exclusiveMinimum: 0
  title: Deadline 10 2 Mongo Express Port Host
  type: integer
deadline_10_2_RCS_HTTP_PORT_CONTAINER:
  default: 8888
  exclusiveMinimum: 0
  title: Deadline 10 2 Rcs Http Port Container
  type: integer
deadline_10_2_RCS_HTTP_PORT_HOST:
  default: 8888
  exclusiveMinimum: 0
  title: Deadline 10 2 Rcs Http Port Host
  type: integer
deadline_10_2_SLAVE_STARTUP_PORT:
  default: 17003
  exclusiveMinimum: 0
  title: Deadline 10 2 Slave Startup Port
  type: integer
deadline_10_2_WEBSERVICE_HTTP_PORT_CONTAINER:
  default: 8899
  exclusiveMinimum: 0
  title: Deadline 10 2 Webservice Http Port Container
  type: integer
deadline_10_2_WEBSERVICE_HTTP_PORT_HOST:
  default: 8899
  exclusiveMinimum: 0
  title: Deadline 10 2 Webservice Http Port Host
  type: integer
deadline_10_2_database_install_destination:
  default: '{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/data/opt/Thinkbox/DeadlineDatabase10'
  format: path
  title: Deadline 10 2 Database Install Destination
  type: string
deadline_10_2_installer_aws_portal_link:
  default: <NOT_SET__CHANGE_ME>
  description: The full path to the downloaded `AWSPortalLink-1.2.x.x-linux-x64-installer.run`
    file. The installer itself is not part of this Feature. For more information,
    see https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2?tab=readme-ov-file#get-deadline
  format: path
  title: Deadline 10 2 Installer Aws Portal Link
  type: string
deadline_10_2_installer_deadline_client:
  default: <NOT_SET__CHANGE_ME>
  description: The full path to the downloaded `DeadlineClient-10.2.x.x-linux-x64-installer.run`
    file. The installer itself is not part of this Feature. For more information,
    see https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2?tab=readme-ov-file#get-deadline
  format: path
  title: Deadline 10 2 Installer Deadline Client
  type: string
deadline_10_2_installer_deadline_repository:
  default: <NOT_SET__CHANGE_ME>
  description: The full path to the downloaded `DeadlineRepository-10.2.x.x-linux-x64-installer.run`
    file. The installer itself is not part of this Feature. For more information,
    see https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2?tab=readme-ov-file#get-deadline
  format: path
  title: Deadline 10 2 Installer Deadline Repository
  type: string
deadline_10_2_mongodb_docker_image:
  default: docker.io/mongodb/mongodb-community-server:4.4-ubuntu2004
  title: Deadline 10 2 Mongodb Docker Image
  type: string
deadline_10_2_repository_install_destination:
  default: '{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/data/opt/Thinkbox/DeadlineRepository10'
  description: For an OverlayFS, this is the lowest (read-only) lowerdir.
  format: path
  title: Deadline 10 2 Repository Install Destination
  type: string
deadline_10_2_repository_work_dir:
  default: '{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/data/opt/Thinkbox/DeadlineRepository10'
  description: If not using OverlayFS, this is usually the same value as deadline_10_2_repository_install_destination.
    If the repository resides on an OverlayFS, this is the resulting mount point of
    the overlay.
  format: path
  title: Deadline 10 2 Repository Work Dir
  type: string
docker_compose:
  default: '{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/docker_compose/docker-compose.yml'
  description: The path to the `docker-compose.yml` file.
  format: path
  title: Docker Compose
  type: string
enabled:
  default: false
  description: Not enabled by default because this Feature has some basic requirements,
    such as the installers.
  title: Enabled
  type: boolean
env:
  additionalProperties: true
  title: Env
  type: object
feature_name:
  default: OpenStudioLandscapes-Deadline-10-2
  title: Feature Name
  type: string
group_name:
  default: OpenStudioLandscapes_Deadline_10_2
  title: Group Name
  type: string
key_prefixes:
  default:
  - OpenStudioLandscapes_Deadline_10_2
  items:
    type: string
  title: Key Prefixes
  type: array
local_bind_volumes:
  description: Here you can define Feature specific, arbitrary, absolute bind volume
    mappings.
  items:
    type: string
  title: Local Bind Volumes
  type: array
local_environment_variables:
  additionalProperties:
    type: string
  description: Here you can define Feature specific, arbitrary environment variables.
  title: Local Environment Variables
  type: object
pip_packages:
  default:
  - gazu[cli]
  items: {}
  title: Pip Packages
  type: array

```

</details>


## Local Development/Unit Testing/Debugging

This is for isolated development, unit testing and debugging. Instead of the [`OpenStudioLandscapes-Deadline-10-2/tree/main/src/OpenStudioLandscapes/Deadline_10_2/definitions.py`](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2/tree/main/src/OpenStudioLandscapes/Deadline_10_2/definitions.py), the accompanying [`OpenStudioLandscapes-Deadline-10-2/tree/main/workspace.yaml`](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2/tree/main/workspace.yaml) loads the [`OpenStudioLandscapes-Deadline-10-2/tree/main/src/OpenStudioLandscapes/Deadline_10_2/_definitions_with_upstream_specs.py`](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2/tree/main/src/OpenStudioLandscapes/Deadline_10_2/_definitions_with_upstream_specs.py) which also contains [`AssetSpec`](https://release-1-9-13.archive.dagster-docs.io/api/dagster/assets#dagster.AssetSpec) definitions for upstream dependencies as [external assets](https://release-1-9-13.archive.dagster-docs.io/guides/build/assets/external-assets).

```shell
# cd ./.features/OpenStudioLandscapes-Deadline-10-2
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools setuptools_scm wheel
pip install --editable .[dev]
dagster dev --workspace workspace.yaml
```

***

# External Resources

[![The Deadline Installers are not part of the `OpenStudioLandscapes-Deadline` Feature. You will have to download the installers manually before you can use this Feature. ](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/_static/Product_Button_Deadline.png)](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html)

> [!IMPORTANT]
> 
> Disclaimer:
> 
> Deadline is in [**Maintenance Mode**](https://docs.thinkboxsoftware.com/products/deadline/10.4/1_User%20Manual/manual/maintenance-mode-faq.html).
> I try to avoid Deadline customization wherever possible (custom plugins and events for example).
> Instead, I want to lower the dependency to external (especially
> closed source) applications and migrate as many post-steps to
> free/open dependencies as possible (or dependencies I own - like
> [OpenStudioLandscapes-DagsterCodeLocation-ShotProcessor](https://github.com/michimussato/OpenStudioLandscapes-DagsterCodeLocation-ShotProcessor)).

## Get Deadline

- https://aws.amazon.com/thinkbox-deadline
- https://aws.amazon.com/media-services/thinkbox/

### Get Deadline 10.2

Deadline is free, however, an AWS account is required to access the download area as well as to use all Deadline Cloud features. Register here:

- [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup)

Once logged in, you can download the Deadline tar archive from this website:

- [https://us-east-1.console.aws.amazon.com/deadlinecloud/home#/thinkbox](https://us-east-1.console.aws.amazon.com/deadlinecloud/home#/thinkbox)

If you prefer to just download Deadline and use it without any AWS Cloud features, here you can get the `tar` archive and the `sha256` directly:

- [https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.tar](https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.tar)
- [https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.sha256](https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.sha256)

### Instructions

Extract all contents for the `tar` archive to your local drive - for example to `~/Downloads/Deadline_10_2_Installers`.

```generic
$ tree ~/Downloads/Deadline_10_2_Installers
├── AWSPortalLink-1.2.1.0-linux-x64-installer.run
├── AWSPortalLink-1.2.1.0-linux-x64-installer.run.sig
├── DeadlineClient-10.2.1.1-linux-x64-installer.run
├── DeadlineClient-10.2.1.1-linux-x64-installer.run.sig
├── DeadlineRepository-10.2.1.1-linux-x64-installer.run
└── DeadlineRepository-10.2.1.1-linux-x64-installer.run.sig
```

Then, specify the full paths of the `*.run` files in the `config.yml` file (usually `~/.config/OpenStudioLandscapes/config-store/OpenStudioLandscapes-Deadline-10-2/config.yml` if not specified otherwise):

```yaml
# deadline_10_2_installer_aws_portal_link: REQUIRED (CHANGE_ME)
deadline_10_2_installer_aws_portal_link: "~/Downloads/Deadline_10_2_Installers/AWSPortalLink-1.2.1.0-linux-x64-installer.run"
# deadline_10_2_installer_deadline_client: REQUIRED (CHANGE_ME)
deadline_10_2_installer_deadline_client: "~/Downloads/Deadline_10_2_Installers/DeadlineClient-10.2.1.1-linux-x64-installer.run"
# deadline_10_2_installer_deadline_repository: REQUIRED (CHANGE_ME)
deadline_10_2_installer_deadline_repository: "~/Downloads/Deadline_10_2_Installers/DeadlineRepository-10.2.1.1-linux-x64-installer.run"
```

After doing so, you can enable the **OpenStudioLandscapes-Deadline-10-2** and **OpenStudioLandscapes-Deadline-10-2-Worker** Features in their `config.yml` files:

```yaml
enabled: true
```

## Documentation

### User Manual

- [https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html)

### Scripting Reference

- [https://docs.thinkboxsoftware.com/products/deadline/10.2/2_Scripting%20Reference/index.html](https://docs.thinkboxsoftware.com/products/deadline/10.2/2_Scripting%20Reference/index.html)

### Python Reference

- [https://docs.thinkboxsoftware.com/products/deadline/10.2/3_Python%20Reference/index.html](https://docs.thinkboxsoftware.com/products/deadline/10.2/3_Python%20Reference/index.html)

### Information on Usage Based Licensing (UBL)

- [https://marketplace.thinkboxsoftware.com](https://marketplace.thinkboxsoftware.com)
- [https://awsthinkbox.zendesk.com/hc/en-us/articles/22883209044759-AWS-Deadline-Cloud-UBL-for-Deadline-10-on-AWS](https://awsthinkbox.zendesk.com/hc/en-us/articles/22883209044759-AWS-Deadline-Cloud-UBL-for-Deadline-10-on-AWS)

## Known Issues

### Could not find the Qt platform plugin "wayland"

#### Error Message

```generic
# $ /opt/Thinkbox/Deadline10/bin/deadlinemonitor
qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: linuxfb, minimal, offscreen, vnc, webgl, xcb.

Aborted                    (core dumped) /opt/Thinkbox/Deadline10/bin/deadlinemonitor
```

#### Solution

```shell
export QT_QPA_PLATFORM=xcb
```

***

# Community

| Feature                                   | GitHub                                                                                                                                                 | Discord                                                                      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| OpenStudioLandscapes                      | [https://github.com/michimussato/OpenStudioLandscapes](https://github.com/michimussato/OpenStudioLandscapes)                                           | [# openstudiolandscapes-general](https://discord.gg/F6bDRWsHac)              |
| OpenStudioLandscapes-Ayon                 | [https://github.com/michimussato/OpenStudioLandscapes-Ayon](https://github.com/michimussato/OpenStudioLandscapes-Ayon)                                 | [# openstudiolandscapes-ayon](https://discord.gg/gd6etWAF3v)                 |
| OpenStudioLandscapes-Dagster              | [https://github.com/michimussato/OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster)                           | [# openstudiolandscapes-dagster](https://discord.gg/jwB3DwmKvs)              |
| OpenStudioLandscapes-Deadline-10-2        | [https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2)               | [# openstudiolandscapes-deadline-10-2](https://discord.gg/p2UjxHk4Y3)        |
| OpenStudioLandscapes-Deadline-10-2-Worker | [https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2-Worker](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2-Worker) | [# openstudiolandscapes-deadline-10-2-worker](https://discord.gg/ttkbfkzUmf) |
| OpenStudioLandscapes-Flamenco             | [https://github.com/michimussato/OpenStudioLandscapes-Flamenco](https://github.com/michimussato/OpenStudioLandscapes-Flamenco)                         | [# openstudiolandscapes-flamenco](https://discord.gg/EPrX5fzBCf)             |
| OpenStudioLandscapes-Flamenco-Worker      | [https://github.com/michimussato/OpenStudioLandscapes-Flamenco-Worker](https://github.com/michimussato/OpenStudioLandscapes-Flamenco-Worker)           | [# openstudiolandscapes-flamenco-worker](https://discord.gg/Sa2zFqSc4p)      |
| OpenStudioLandscapes-Grafana              | [https://github.com/michimussato/OpenStudioLandscapes-Grafana](https://github.com/michimussato/OpenStudioLandscapes-Grafana)                           | [# openstudiolandscapes-grafana](https://discord.gg/gEDQ8vJWDb)              |
| OpenStudioLandscapes-Kitsu                | [https://github.com/michimussato/OpenStudioLandscapes-Kitsu](https://github.com/michimussato/OpenStudioLandscapes-Kitsu)                               | [# openstudiolandscapes-kitsu](https://discord.gg/6cc6mkReJ7)                |
| OpenStudioLandscapes-LikeC4               | [https://github.com/michimussato/OpenStudioLandscapes-LikeC4](https://github.com/michimussato/OpenStudioLandscapes-LikeC4)                             | [# openstudiolandscapes-likec4](https://discord.gg/qAYYsKYF6V)               |
| OpenStudioLandscapes-OpenCue              | [https://github.com/michimussato/OpenStudioLandscapes-OpenCue](https://github.com/michimussato/OpenStudioLandscapes-OpenCue)                           | [# openstudiolandscapes-opencue](https://discord.gg/3DdCZKkVyZ)              |
| OpenStudioLandscapes-OpenCue-Worker       | [https://github.com/michimussato/OpenStudioLandscapes-OpenCue-Worker](https://github.com/michimussato/OpenStudioLandscapes-OpenCue-Worker)             | [# openstudiolandscapes-opencue-worker](https://discord.gg/n9fxxhHa3V)       |
| OpenStudioLandscapes-RustDeskServer       | [https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer](https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer)             | [# openstudiolandscapes-rustdeskserver](https://discord.gg/nJ8Ffd2xY3)       |
| OpenStudioLandscapes-Syncthing            | [https://github.com/michimussato/OpenStudioLandscapes-Syncthing](https://github.com/michimussato/OpenStudioLandscapes-Syncthing)                       | [# openstudiolandscapes-syncthing](https://discord.gg/upb9MCqb3X)            |
| OpenStudioLandscapes-Template             | [https://github.com/michimussato/OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template)                         | [# openstudiolandscapes-template](https://discord.gg/J59GYp3Wpy)             |
| OpenStudioLandscapes-VERT                 | [https://github.com/michimussato/OpenStudioLandscapes-VERT](https://github.com/michimussato/OpenStudioLandscapes-VERT)                                 | [# openstudiolandscapes-vert](https://discord.gg/EPrX5fzBCf)                 |
| OpenStudioLandscapes-filebrowser          | [https://github.com/michimussato/OpenStudioLandscapes-filebrowser](https://github.com/michimussato/OpenStudioLandscapes-filebrowser)                   | [# openstudiolandscapes-filebrowser](https://discord.gg/stzNsZBmwk)          |
| OpenStudioLandscapes-n8n                  | [https://github.com/michimussato/OpenStudioLandscapes-n8n](https://github.com/michimussato/OpenStudioLandscapes-n8n)                                   | [# openstudiolandscapes-n8n](https://discord.gg/yFYrG999wE)                  |

To follow up on the previous LinkedIn publications, visit:

- [OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/company/106731439/).
- [Search for tag #OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/search/results/all/?keywords=%23openstudiolandscapes).

***

Last changed: **2026-06-18 21:59:15 UTC**