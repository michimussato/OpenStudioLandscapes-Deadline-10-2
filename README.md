[![ Logo OpenStudioLandscapes ](https://github.com/michimussato/OpenStudioLandscapes/raw/main/media/images/logo128.png)](https://github.com/michimussato/OpenStudioLandscapes)

***

1. [Feature: OpenStudioLandscapes-Deadline-10-2](#feature-openstudiolandscapes-deadline-10-2)
   1. [Brief](#brief)
   2. [Requirements](#requirements)
   3. [Install](#install)
      1. [This Feature](#this-feature)
   4. [Add to OpenStudioLandscapes](#add-to-openstudiolandscapes)
   5. [Testing](#testing)
      1. [pre-commit](#pre-commit)
      2. [nox](#nox)
   6. [Variables](#variables)
      1. [Feature Configs](#feature-configs)
2. [Community](#community)
3. [Get Deadline](#get-deadline)
   1. [Get Deadline 10.2](#get-deadline-102)
   2. [Instructions](#instructions)
   1. [Documentation](#documentation)
      1. [User Manual](#user-manual)
      2. [Scripting Reference](#scripting-reference)
      3. [Python Reference](#python-reference)
      4. [Information on Usage Based Licensing (UBL)](#information-on-usage-based-licensing-ubl)

***

This `README.md` was dynamically created with [OpenStudioLandscapesUtil-ReadmeGenerator](https://github.com/michimussato/OpenStudioLandscapesUtil-ReadmeGenerator).

***

# Feature: OpenStudioLandscapes-Deadline-10-2

## Brief

This is an extension to the OpenStudioLandscapes ecosystem. The full documentation of OpenStudioLandscapes is available [here](https://github.com/michimussato/OpenStudioLandscapes).

You feel like writing your own Feature? Go and check out the [OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template).

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

## Add to OpenStudioLandscapes

Add the following code to `OpenStudioLandscapes.engine.features.FEATURES`:

```python

FEATURES.update(
    "OpenStudioLandscapes-Deadline-10-2": {
        "enabled": True|False,
        # - from ENVIRONMENT VARIABLE (.env):
        #   "enabled": get_bool_env("ENV_VAR")
        # - combined:
        #   "enabled": True|False or get_bool_env(
        #       "OPENSTUDIOLANDSCAPES__ENABLE_FEATURE_OPENSTUDIOLANDSCAPES_DEADLINE_10_2"
        #   )
        "module": "OpenStudioLandscapes.Deadline_10_2.definitions",
        "compose_scope": ComposeScope.DEFAULT,
        "feature_config": OpenStudioLandscapesConfig.DEFAULT,
    }
)

```

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

#### Generate Sphinx Documentation

```shell

nox -v --add-timestamp --session docs

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
- `python3.12`

## Variables

The following variables are being declared in `OpenStudioLandscapes.Deadline_10_2.constants` and are accessible throughout the [`OpenStudioLandscapes-Deadline-10-2`](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2/tree/main/src/OpenStudioLandscapes/Deadline_10_2/constants.py) package.

| Variable                   | Type   |
| :------------------------- | :----- |
| `DOCKER_USE_CACHE`         | `bool` |
| `MONGODB_INSIDE_CONTAINER` | `bool` |
| `DISABLE_LOCAL_PULSE`      | `bool` |
| `DISABLE_LOCAL_WORKER`     | `bool` |
| `ASSET_HEADER`             | `dict` |
| `FEATURE_CONFIGS`          | `dict` |

### Feature Configs

#### Feature Config: default

| Variable                                       | Type   | Value                                                                                                                |
| :--------------------------------------------- | :----- | :------------------------------------------------------------------------------------------------------------------- |
| `DOCKER_USE_CACHE`                             | `bool` | `False`                                                                                                              |
| `DEADLINE_VERSION`                             | `str`  | `10.2.1.1`                                                                                                           |
| `CONFIGS_ROOT`                                 | `str`  | `{DOT_FEATURES}/OpenStudioLandscapes-Deadline-10-2/.payload/config`                                                  |
| `INSTALLER_AWSPortalLink`                      | `str`  | `{DOT_FEATURES}/OpenStudioLandscapes-Deadline-10-2/.payload/bin/AWSPortalLink-1.2.1.0-linux-x64-installer.run`       |
| `INSTALLER_DeadlineClient`                     | `str`  | `{DOT_FEATURES}/OpenStudioLandscapes-Deadline-10-2/.payload/bin/DeadlineClient-10.2.1.1-linux-x64-installer.run`     |
| `INSTALLER_DeadlineRepository`                 | `str`  | `{DOT_FEATURES}/OpenStudioLandscapes-Deadline-10-2/.payload/bin/DeadlineRepository-10.2.1.1-linux-x64-installer.run` |
| `REPOSITORY_INSTALL_DESTINATION_Deadline_10_2` | `str`  | `{DOT_LANDSCAPES}/{LANDSCAPE}/Deadline_10_2__Deadline_10_2/data/opt/Thinkbox/DeadlineRepository10`                   |
| `DATABASE_INSTALL_DESTINATION_Deadline_10_2`   | `str`  | `{DOT_LANDSCAPES}/{LANDSCAPE}/Deadline_10_2__Deadline_10_2/data/opt/Thinkbox/DeadlineDatabase10`                     |
| `RCS_HTTP_PORT_HOST`                           | `str`  | `8888`                                                                                                               |
| `RCS_HTTP_PORT_CONTAINER`                      | `str`  | `8888`                                                                                                               |
| `WEBSERVICE_HTTP_PORT_HOST`                    | `str`  | `8899`                                                                                                               |
| `WEBSERVICE_HTTP_PORT_CONTAINER`               | `str`  | `8899`                                                                                                               |
| `LAUNCHER_LISTENING_PORT`                      | `str`  | `17000`                                                                                                              |
| `AUTO_CONFIGURATION_PORT`                      | `str`  | `17001`                                                                                                              |
| `SLAVE_STARTUP_PORT`                           | `str`  | `17003`                                                                                                              |
| `LICENSE_FORWARDER_LISTENING_PORT`             | `str`  | `17003`                                                                                                              |
| `APPLICATION_STARTUP_PORT`                     | `str`  | `17006`                                                                                                              |
| `MONGO_DB_HOST`                                | `str`  | `mongodb-10-2`                                                                                                       |
| `MONGO_EXPRESS_PORT_HOST`                      | `str`  | `8181`                                                                                                               |
| `MONGO_EXPRESS_PORT_CONTAINER`                 | `str`  | `8081`                                                                                                               |
| `MONGO_DB_NAME`                                | `str`  | `deadline10db`                                                                                                       |
| `MONGO_DB_PORT_HOST`                           | `str`  | `21017`                                                                                                              |
| `MONGO_DB_PORT_CONTAINER`                      | `str`  | `21017`                                                                                                              |
| `DEFAULT_DBPATH_CONTAINER`                     | `str`  | `/data/db`                                                                                                           |
| `ME_CONFIG_BASICAUTH_USERNAME`                 | `str`  | `web`                                                                                                                |
| `ME_CONFIG_BASICAUTH_PASSWORD`                 | `str`  | `web`                                                                                                                |
| `ME_CONFIG_OPTIONS_EDITORTHEME`                | `str`  | `darcula`                                                                                                            |
| `ME_CONFIG_MONGODB_SERVER`                     | `str`  | `mongodb-10-2`                                                                                                       |
| `ME_CONFIG_MONGODB_PORT`                       | `str`  | `21017`                                                                                                              |
| `ME_CONFIG_MONGODB_URL`                        | `str`  | `mongodb://admin:pass@localhost:21017/db?ssl=false`                                                                  |

# Community

| Feature                      | GitHub                                                                                                                       | Discord                                                               |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| OpenStudioLandscapes         | [https://github.com/michimussato/OpenStudioLandscapes](https://github.com/michimussato/OpenStudioLandscapes)                 | [# openstudiolandscapes-general](https://discord.com/invite/aYnJnaqE) |
| OpenStudioLandscapes-Ayon    | [https://github.com/michimussato/OpenStudioLandscapes-Ayon](https://github.com/michimussato/OpenStudioLandscapes-Ayon)       | [# openstudiolandscapes-ayon](https://discord.gg/D4XrG99G)            |
| OpenStudioLandscapes-Dagster | [https://github.com/michimussato/OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster) | [# openstudiolandscapes-dagster](https://discord.gg/qFGWTWu4)         |
| OpenStudioLandscapes-Kitsu   | [https://github.com/michimussato/OpenStudioLandscapes-Kitsu](https://github.com/michimussato/OpenStudioLandscapes-Kitsu)     | [# openstudiolandscapes-kitsu](https://discord.gg/4UqHdsan)           |

To follow up on the previous LinkedIn publications, visit:

- [OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/company/106731439/).
- [Search for tag #OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/search/results/all/?keywords=%23openstudiolandscapes).

***

# Get Deadline

[![ The Deadline Installers are not part of the `OpenStudioLandscapes-Deadline` Feature. You will have to download the installers manually before you can use this Feature. ](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/_static/Product_Button_Deadline.png)](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html)

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

```shell

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