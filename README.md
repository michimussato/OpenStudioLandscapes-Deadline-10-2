[![ Logo OpenStudioLandscapes ](https://github.com/michimussato/OpenStudioLandscapes/raw/main/media/images/logo128.png)](https://github.com/michimussato/OpenStudioLandscapes)

***

1. [Feature: OpenStudioLandscapes-Deadline-10-2](#feature-openstudiolandscapes-deadline-10-2)
   1. [Brief](#brief)
   2. [Configuration](#configuration)
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
4. [Technical Reference](#technical-reference)
   1. [Requirements](#requirements)
   2. [Install](#install)
      1. [This Feature](#this-feature)
   3. [Testing](#testing)
      1. [pre-commit](#pre-commit)
      2. [nox](#nox)

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

## Configuration

OpenStudioLandscapes will search for a local config store. The default location is `~/.config/OpenStudioLandscapes/config-store/` but you can specify a different location if you need to.

A local config store location will be created if it doesn't exist, together with the `config.yml` files for each individual Feature.

> [!TIP]
> 
> The config store root will be initialized as a local Git
> controlled repository. This makes it easy to track changes
> you made to the `config.yml`.

> [!TIP]
> 
> To specify a config store location different than
> the default, you can do so be setting the environment variable
> `OPENSTUDIOLANDSCAPES__CONFIGSTORE_ROOT`:
> 
> ```shell
> OPENSTUDIOLANDSCAPES__CONFIGSTORE_ROOT="~/.config/OpenStudioLandscapes/my-custom-config-store"
> ```

The following settings are available in `OpenStudioLandscapes-Deadline-10-2` and are accessible throughout the [`OpenStudioLandscapes-Deadline-10-2`](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2/tree/main/OpenStudioLandscapes/Deadline_10_2/config/models.py) package.

```yaml
# ===
# env
# ---
#
# Type: typing.Dict
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# =============
# config_engine
# -------------
#
# Type: <class 'OpenStudioLandscapes.engine.config.models.ConfigEngine'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# =============
# config_parent
# -------------
#
# Type: <class 'OpenStudioLandscapes.engine.config.models.FeatureBaseModel'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# ============
# distribution
# ------------
#
# Type: <class 'importlib.metadata.Distribution'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# ==========
# group_name
# ----------
#
# Type: <class 'str'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# ============
# key_prefixes
# ------------
#
# Type: typing.List[str]
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# =======
# enabled
# -------
#
# Type: <class 'bool'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         Whether the Feature is enabled or not.
#     Default value:
#         True
# Description:
#     Not enabled by default because this Feature has some basic requirements, such as the installers.
# Required:
#     False
# Examples:
#     None
enabled: false


# =============
# compose_scope
# -------------
#
# Type: <class 'str'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         default
# Description:
#     None
# Required:
#     False
# Examples:
#     ['default', 'license_server', 'worker']


# ============
# feature_name
# ------------
#
# Type: <class 'str'>
# Base Class Info:
#     Required:
#         True
#     Description:
#         The name of the feature. It is derived from the `OpenStudioLandscapes.<Feature>.dist` attribute.
#     Default value:
#         PydanticUndefined
# Description:
#     None
# Required:
#     False
# Examples:
#     None
feature_name: OpenStudioLandscapes-Deadline-10-2


# ==============
# docker_compose
# --------------
#
# Type: <class 'pathlib.Path'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         The path to the `docker-compose.yml` file.
#     Default value:
#         {DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/docker_compose/docker-compose.yml
# Description:
#     The path to the `docker-compose.yml` file.
# Required:
#     False
# Examples:
#     None


# =======================================
# deadline_10_2_installer_aws_portal_link
# ---------------------------------------
#
# Type: <class 'pathlib.Path'>
# Description:
#     The full path to the `AWSPortalLink-1.2.x.x-linux-x64-installer.run` file.
# Required:
#     True
# Examples:
#     None
deadline_10_2_installer_aws_portal_link: PydanticUndefined


# =======================================
# deadline_10_2_installer_deadline_client
# ---------------------------------------
#
# Type: <class 'pathlib.Path'>
# Description:
#     The full path to the `DeadlineClient-10.2.x.x-linux-x64-installer.run` file.
# Required:
#     True
# Examples:
#     None
deadline_10_2_installer_deadline_client: PydanticUndefined


# ===========================================
# deadline_10_2_installer_deadline_repository
# -------------------------------------------
#
# Type: <class 'pathlib.Path'>
# Description:
#     The full path to the `DeadlineRepository-10.2.x.x-linux-x64-installer.run` file.
# Required:
#     True
# Examples:
#     None
deadline_10_2_installer_deadline_repository: PydanticUndefined


# ============================================
# deadline_10_2_repository_install_destination
# --------------------------------------------
#
# Type: <class 'pathlib.Path'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_repository_install_destination: '{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/data/opt/Thinkbox/DeadlineRepository10'


# ==========================================
# deadline_10_2_database_install_destination
# ------------------------------------------
#
# Type: <class 'pathlib.Path'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_database_install_destination: '{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/data/opt/Thinkbox/DeadlineDatabase10'


# ================================
# deadline_10_2_RCS_HTTP_PORT_HOST
# --------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_RCS_HTTP_PORT_HOST: 8888


# =====================================
# deadline_10_2_RCS_HTTP_PORT_CONTAINER
# -------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_RCS_HTTP_PORT_CONTAINER: 8888


# =======================================
# deadline_10_2_WEBSERVICE_HTTP_PORT_HOST
# ---------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_WEBSERVICE_HTTP_PORT_HOST: 8899


# ============================================
# deadline_10_2_WEBSERVICE_HTTP_PORT_CONTAINER
# --------------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_WEBSERVICE_HTTP_PORT_CONTAINER: 8899


# =====================================
# deadline_10_2_LAUNCHER_LISTENING_PORT
# -------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_LAUNCHER_LISTENING_PORT: 17000


# =====================================
# deadline_10_2_AUTO_CONFIGURATION_PORT
# -------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_AUTO_CONFIGURATION_PORT: 17001


# ================================
# deadline_10_2_SLAVE_STARTUP_PORT
# --------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_SLAVE_STARTUP_PORT: 17003


# ==============================================
# deadline_10_2_LICENSE_FORWARDER_LISTENING_PORT
# ----------------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_LICENSE_FORWARDER_LISTENING_PORT: 17003


# ======================================
# deadline_10_2_APPLICATION_STARTUP_PORT
# --------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_APPLICATION_STARTUP_PORT: 17006


# =================================
# deadline_10_2_DISABLE_LOCAL_PULSE
# ---------------------------------
#
# Type: <class 'bool'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_DISABLE_LOCAL_PULSE: false


# ==================================
# deadline_10_2_DISABLE_LOCAL_WORKER
# ----------------------------------
#
# Type: <class 'bool'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_DISABLE_LOCAL_WORKER: true


# ==================================
# deadline_10_2_mongodb_docker_image
# ----------------------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_mongodb_docker_image: docker.io/mongodb/mongodb-community-server:4.4-ubuntu2004


# ======================================
# deadline_10_2_MONGODB_INSIDE_CONTAINER
# --------------------------------------
#
# Type: <class 'bool'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_MONGODB_INSIDE_CONTAINER: false


# ===========================
# deadline_10_2_MONGO_DB_HOST
# ---------------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_MONGO_DB_HOST: mongodb-10-2


# ===========================
# deadline_10_2_MONGO_DB_NAME
# ---------------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_MONGO_DB_NAME: deadline10db


# ======================================
# deadline_10_2_DEFAULT_DBPATH_CONTAINER
# --------------------------------------
#
# Type: <class 'pathlib.Path'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_DEFAULT_DBPATH_CONTAINER: /data/db


# =====================================
# deadline_10_2_MONGO_EXPRESS_PORT_HOST
# -------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_MONGO_EXPRESS_PORT_HOST: 8181


# ==========================================
# deadline_10_2_MONGO_EXPRESS_PORT_CONTAINER
# ------------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_MONGO_EXPRESS_PORT_CONTAINER: 8081


# ================================
# deadline_10_2_MONGO_DB_PORT_HOST
# --------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_MONGO_DB_PORT_HOST: 21017


# =====================================
# deadline_10_2_MONGO_DB_PORT_CONTAINER
# -------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_MONGO_DB_PORT_CONTAINER: 21017


# ==========================================
# deadline_10_2_ME_CONFIG_BASICAUTH_USERNAME
# ------------------------------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_ME_CONFIG_BASICAUTH_USERNAME: web


# ==========================================
# deadline_10_2_ME_CONFIG_BASICAUTH_PASSWORD
# ------------------------------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_ME_CONFIG_BASICAUTH_PASSWORD: web


# ===========================================
# deadline_10_2_ME_CONFIG_OPTIONS_EDITORTHEME
# -------------------------------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_ME_CONFIG_OPTIONS_EDITORTHEME: darcula


# ======================================
# deadline_10_2_ME_CONFIG_MONGODB_SERVER
# --------------------------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_ME_CONFIG_MONGODB_SERVER: mongodb-10-2


# ===================================
# deadline_10_2_ME_CONFIG_MONGODB_URL
# -----------------------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_ME_CONFIG_MONGODB_URL: mongodb://admin:pass@localhost:21017/db?ssl=false


# ====================================
# deadline_10_2_ME_CONFIG_MONGODB_PORT
# ------------------------------------
#
# Type: <class 'int'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
deadline_10_2_ME_CONFIG_MONGODB_PORT: 21017



```

***

# External Resources

[![The Deadline Installers are not part of the `OpenStudioLandscapes-Deadline` Feature. You will have to download the installers manually before you can use this Feature. ](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/_static/Product_Button_Deadline.png)](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html)

## Get Deadline

- https://aws.amazon.com/thinkbox-deadline
- https://aws.amazon.com/media-services/thinkbox/

### Get Deadline 10.2

Deadline is free, however (legally), an AWS account is required to access the download area. Also, the account is required to use all Deadline features. Register here:

- [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup)

Once logged in, you can download the Deadline tar archive from this website:

- [https://us-east-1.console.aws.amazon.com/deadlinecloud/home#/thinkbox](https://us-east-1.console.aws.amazon.com/deadlinecloud/home#/thinkbox)

If you prefer to just download Deadline and use it without any AWS Cloud features, here you can get the `tar` archive and the `sha256` directly:

- [https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.tar](https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.tar)
- [https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.sha256](https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.sha256)

### Instructions

Extract all contents for the `tar` archive to `OpenStudioLandscapes-Deadline-10-2/.payload/bin`.

```generic
$ tree .payload
.payload
├── bin
│   ├── AWSPortalLink-1.2.1.0-linux-x64-installer.run
│   ├── AWSPortalLink-1.2.1.0-linux-x64-installer.run.sig
│   ├── DeadlineClient-10.2.1.1-linux-x64-installer.run
│   ├── DeadlineClient-10.2.1.1-linux-x64-installer.run.sig
│   ├── DeadlineRepository-10.2.1.1-linux-x64-installer.run
│   └── DeadlineRepository-10.2.1.1-linux-x64-installer.run.sig
├── config
└── data

4 directories, 6 files
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

| Feature                              | GitHub                                                                                                                                       | Discord                                                                 |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| OpenStudioLandscapes                 | [https://github.com/michimussato/OpenStudioLandscapes](https://github.com/michimussato/OpenStudioLandscapes)                                 | [# openstudiolandscapes-general](https://discord.gg/F6bDRWsHac)         |
| OpenStudioLandscapes-Ayon            | [https://github.com/michimussato/OpenStudioLandscapes-Ayon](https://github.com/michimussato/OpenStudioLandscapes-Ayon)                       | [# openstudiolandscapes-ayon](https://discord.gg/gd6etWAF3v)            |
| OpenStudioLandscapes-Dagster         | [https://github.com/michimussato/OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster)                 | [# openstudiolandscapes-dagster](https://discord.gg/jwB3DwmKvs)         |
| OpenStudioLandscapes-Flamenco        | [https://github.com/michimussato/OpenStudioLandscapes-Flamenco](https://github.com/michimussato/OpenStudioLandscapes-Flamenco)               | [# openstudiolandscapes-flamenco](https://discord.gg/EPrX5fzBCf)        |
| OpenStudioLandscapes-Flamenco-Worker | [https://github.com/michimussato/OpenStudioLandscapes-Flamenco-Worker](https://github.com/michimussato/OpenStudioLandscapes-Flamenco-Worker) | [# openstudiolandscapes-flamenco-worker](https://discord.gg/Sa2zFqSc4p) |
| OpenStudioLandscapes-Kitsu           | [https://github.com/michimussato/OpenStudioLandscapes-Kitsu](https://github.com/michimussato/OpenStudioLandscapes-Kitsu)                     | [# openstudiolandscapes-kitsu](https://discord.gg/6cc6mkReJ7)           |
| OpenStudioLandscapes-RustDeskServer  | [https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer](https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer)   | [# openstudiolandscapes-rustdeskserver](https://discord.gg/nJ8Ffd2xY3)  |
| OpenStudioLandscapes-Template        | [https://github.com/michimussato/OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template)               | [# openstudiolandscapes-template](https://discord.gg/J59GYp3Wpy)        |
| OpenStudioLandscapes-VERT            | [https://github.com/michimussato/OpenStudioLandscapes-VERT](https://github.com/michimussato/OpenStudioLandscapes-VERT)                       | [# openstudiolandscapes-twingate](https://discord.gg/FYaFRUwbYr)        |

To follow up on the previous LinkedIn publications, visit:

- [OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/company/106731439/).
- [Search for tag #OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/search/results/all/?keywords=%23openstudiolandscapes).

***

# Technical Reference

## Requirements

- `python-3.11`
- `OpenStudioLandscapes`

## Install

### This Feature

Clone this repository into `OpenStudioLandscapes/.features`:

```shell
# cd .features
git clone https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2.git
```

Create `venv`:

```shell
# cd .features/OpenStudioLandscapes-Deadline-10-2
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools
```

Configure `venv`:

```shell
# cd .features/OpenStudioLandscapes-Deadline-10-2
pip install -e "../../[dev]"
pip install -e ".[dev]"
```

For more info see [VCS Support of pip](https://pip.pypa.io/en/stable/topics/vcs-support/).

## Testing

### pre-commit

- https://pre-commit.com
- https://pre-commit.com/hooks.html

```shell
pre-commit install
```

### nox

#### Generate Report

```shell
nox --no-error-on-missing-interpreters --report .nox/nox-report.json
```

#### Re-Generate this README

```shell
nox -v --add-timestamp --session readme
```

#### pylint

```shell
nox -v --add-timestamp --session lint
```

##### pylint: disable=redefined-outer-name

- [`W0621`](https://pylint.pycqa.org/en/latest/user_guide/messages/warning/redefined-outer-name.html): Due to Dagsters way of piping arguments into assets.

#### SBOM

Acronym for Software Bill of Materials

```shell
nox -v --add-timestamp --session sbom
```

We create the following SBOMs:

- [`cyclonedx-bom`](https://pypi.org/project/cyclonedx-bom/)
- [`pipdeptree`](https://pypi.org/project/pipdeptree/) (Dot)
- [`pipdeptree`](https://pypi.org/project/pipdeptree/) (Mermaid)

SBOMs for the different Python interpreters defined in [`.noxfile.VERSIONS`](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2/tree/main/noxfile.py) will be created in the [`.sbom`](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2/tree/main/.sbom) directory of this repository.

- `cyclone-dx`
- `pipdeptree` (Dot)
- `pipdeptree` (Mermaid)

Currently, the following Python interpreters are enabled for testing:

- `python3.11`

***

Last changed: **2025-12-23 12:53:57 UTC**