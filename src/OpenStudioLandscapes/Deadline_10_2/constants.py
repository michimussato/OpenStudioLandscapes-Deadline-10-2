__all__ = [
    "DOCKER_USE_CACHE",
    "MONGODB_INSIDE_CONTAINER",
    "DISABLE_LOCAL_PULSE",
    "DISABLE_LOCAL_WORKER",
    "ASSET_HEADER",
    "FEATURE_CONFIGS",
]

import pathlib
from pathlib import Path
from typing import Generator, Any

from dagster import (
    multi_asset,
    AssetOut,
    AssetMaterialization,
    AssetExecutionContext,
    Output,
    MetadataValue,
    get_dagster_logger,
)

LOGGER = get_dagster_logger(__name__)

from OpenStudioLandscapes.engine.constants import DOCKER_USE_CACHE_GLOBAL
from OpenStudioLandscapes.engine.enums import OpenStudioLandscapesConfig

DOCKER_USE_CACHE = DOCKER_USE_CACHE_GLOBAL or False
MONGODB_INSIDE_CONTAINER = False


DISABLE_LOCAL_PULSE = False
DISABLE_LOCAL_WORKER = True


GROUP = "Deadline_10_2"
KEY = [GROUP]
FEATURE = f"OpenStudioLandscapes-{GROUP}".replace("_", "-")

ASSET_HEADER = {
    "group_name": GROUP,
    "key_prefix": KEY,
}

# @formatter:off
FEATURE_CONFIGS = {
    OpenStudioLandscapesConfig.DEFAULT: {
        "DOCKER_USE_CACHE": DOCKER_USE_CACHE,
        "DEADLINE_VERSION": "10.2.1.1",
        "CONFIGS_ROOT": pathlib.Path(
            "{DOT_FEATURES}",
            FEATURE,
            ".payload",
            "config",
        )
        .expanduser()
        .as_posix(),
        f"INSTALLER_AWSPortalLink": pathlib.Path(
            "{DOT_FEATURES}",
            FEATURE,
            ".payload",
            "bin",
            "AWSPortalLink-1.2.1.0-linux-x64-installer.run",
        )
        .expanduser()
        .as_posix(),
        f"INSTALLER_DeadlineClient": pathlib.Path(
            "{DOT_FEATURES}",
            FEATURE,
            ".payload",
            "bin",
            "DeadlineClient-10.2.1.1-linux-x64-installer.run",
        )
        .expanduser()
        .as_posix(),
        f"INSTALLER_DeadlineRepository": pathlib.Path(
            "{DOT_FEATURES}",
            FEATURE,
            ".payload",
            "bin",
            "DeadlineRepository-10.2.1.1-linux-x64-installer.run",
        )
        .expanduser()
        .as_posix(),

        # Env Repository
        # This is where DeadlineRepository10 will get installed to:
        f"REPOSITORY_INSTALL_DESTINATION_{'__'.join(ASSET_HEADER['key_prefix'])}": pathlib.Path(
            "{DOT_LANDSCAPES}",
            "{LANDSCAPE}",
            f"{ASSET_HEADER['group_name']}__{'__'.join(ASSET_HEADER['key_prefix'])}",
            "data",
            "opt",
            "Thinkbox",
            "DeadlineRepository10",
        ).as_posix(),
        # This is where DeadlineDatabase10 will get installed to:
        # (provided MONGODB_INSIDE_CONTAINER is set to False)
        #
        # The Python script that comes with the mongodb docker image
        # initializes a DB if none is found at installation time.
        # That means, if DATABASE_INSTALL_DESTINATION_{ASSET_HEADER['key_prefix']}
        # already points to an existing DB, this one will be used.
        # Make sure that the DB path has ownership of 101:65534.
        # Default would be inside a Landscape:
        # f"DATABASE_INSTALL_DESTINATION_{ASSET_HEADER['key_prefix']}": pathlib.Path(
        #         DOT_DOCKER_ROOT,
        #         env_base.get("LANDSCAPE", "default"),
        #         ASSET_HEADER['key_prefix'],
        #         "data",
        #         "opt",
        #         "Thinkbox",
        #         "DeadlineDatabase10",
        #     ).as_posix(),
        f"DATABASE_INSTALL_DESTINATION_{'__'.join(ASSET_HEADER['key_prefix'])}":
        #################################################################
        # Inside Landscape:
        pathlib.Path(
            "{DOT_LANDSCAPES}",
            "{LANDSCAPE}",
            f"{ASSET_HEADER['group_name']}__{'__'.join(ASSET_HEADER['key_prefix'])}",
            "data",
            "opt",
            "Thinkbox",
            "DeadlineDatabase10",
        ).as_posix(),
        # #################################################################
        # # Test DB:
        # "test_db_10_2": pathlib.Path(
        #     env_in["GIT_ROOT"],
        #     "tests",
        #     "fixtures",
        #     "__".join(context.asset_key.path),
        #     "DeadlineDatabase10",
        # ).as_posix(),

        # Env Deadline
        "RCS_HTTP_PORT_HOST": "8888",
        "RCS_HTTP_PORT_CONTAINER": "8888",
        "WEBSERVICE_HTTP_PORT_HOST": "8899",
        "WEBSERVICE_HTTP_PORT_CONTAINER": "8899",
        "LAUNCHER_LISTENING_PORT": "17000",
        "AUTO_CONFIGURATION_PORT": "17001",
        "SLAVE_STARTUP_PORT": "17003",
        "LICENSE_FORWARDER_LISTENING_PORT": "17003",
        "APPLICATION_STARTUP_PORT": "17006",
        # OpenStudioLandscapesConfig.PRODUCTION: {
        #     "RCS_HTTP_PORT_HOST": "8889",
        #     "RCS_HTTP_PORT_CONTAINER": "8888",
        #     "WEBSERVICE_HTTP_PORT_HOST": "8900",
        #     "WEBSERVICE_HTTP_PORT_CONTAINER": "8899",
        #     "LAUNCHER_LISTENING_PORT": "17010",
        #     "AUTO_CONFIGURATION_PORT": "17011",
        #     "SLAVE_STARTUP_PORT": "17013",
        #     "LICENSE_FORWARDER_LISTENING_PORT": "17013",
        #     "APPLICATION_STARTUP_PORT": "17016",
        # },
        # OpenStudioLandscapesConfig.DEVELOPMENT: {
        #     "RCS_HTTP_PORT_HOST": "8890",
        #     "RCS_HTTP_PORT_CONTAINER": "8888",
        #     "WEBSERVICE_HTTP_PORT_HOST": "8901",
        #     "WEBSERVICE_HTTP_PORT_CONTAINER": "8899",
        #     "LAUNCHER_LISTENING_PORT": "17020",
        #     "AUTO_CONFIGURATION_PORT": "17021",
        #     "SLAVE_STARTUP_PORT": "17023",
        #     "LICENSE_FORWARDER_LISTENING_PORT": "17023",
        #     "APPLICATION_STARTUP_PORT": "17026",
        # },

        # Env MongoDB
        "MONGO_DB_HOST": "mongodb-10-2",
        "MONGO_EXPRESS_PORT_HOST": "8181",
        "MONGO_EXPRESS_PORT_CONTAINER": "8081",
        "MONGO_DB_NAME": "deadline10db",
        "MONGO_DB_PORT_HOST": "21017",
        "MONGO_DB_PORT_CONTAINER": "21017",
        "DEFAULT_DBPATH_CONTAINER": "/data/db",
        # OpenStudioLandscapesConfig.PRODUCTION: {
        #     "MONGO_DB_HOST": "mongodb-10-2",
        #     "MONGO_EXPRESS_PORT_HOST": "8182",
        #     "MONGO_EXPRESS_PORT_CONTAINER": "8081",
        #     "MONGO_DB_NAME": "deadline10db",
        #     "MONGO_DB_PORT_HOST": "21018",
        #     "MONGO_DB_PORT_CONTAINER": "21017",
        #     "DEFAULT_DBPATH_CONTAINER": "/data/db",
        # },
        # OpenStudioLandscapesConfig.DEVELOPMENT: {
        #     "MONGO_DB_HOST": "mongodb-10-2",
        #     "MONGO_EXPRESS_PORT_HOST": "8183",
        #     "MONGO_EXPRESS_PORT_CONTAINER": "8081",
        #     "MONGO_DB_NAME": "deadline10db",
        #     "MONGO_DB_PORT_HOST": "21019",
        #     "MONGO_DB_PORT_CONTAINER": "21017",
        #     "DEFAULT_DBPATH_CONTAINER": "/data/db",
        # },

        # Env Mongo Express
        # https://hub.docker.com/_/mongo-express/
        "ME_CONFIG_BASICAUTH_USERNAME": "web",
        "ME_CONFIG_BASICAUTH_PASSWORD": "web",
        "ME_CONFIG_OPTIONS_EDITORTHEME": "darcula",
        "ME_CONFIG_MONGODB_SERVER": "mongodb-10-2",
        "ME_CONFIG_MONGODB_PORT": "21017",  # "{MONGO_DB_PORT_CONTAINER}",
        # Todo:
        #  - [ ] Verify whether MONGO_DB_PORT_CONTAINER or MONGO_DB_PORT_HOST
        #        is actually correct
        "ME_CONFIG_MONGODB_URL": "mongodb://admin:pass@localhost:21017/db?ssl=false",  # "mongodb://admin:pass@localhost:{MONGO_DB_PORT_CONTAINER}/db?ssl=false",
    }
}


# Docs
# - https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/client-config.html
# - https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/install-client.html#command-line-or-silent-installation

# if multiple instances of the same docker compose need to be run
# this is an easy place to make sure we don't end up with allocated ports
# Todo:
#  - [ ] LauncherListeningPort, AutoConfigurationPort, LicenseForwarderListeningPort
#  WebServiceHttpListenPort=8890
#  WebServiceTlsListenPort=0
#  WebServiceTlsServerCert=
#  WebServiceTlsCaCert=
#  WebServiceTlsAuth=False
#  WebServiceClientSSLAuthentication=NotRequired
#  HttpListenPort=8889
#  TlsListenPort=0
#  LicenseMode=LicenseFree
#  Region=
#  LauncherListeningPort=17000
#  LauncherServiceStartupDelay=60
#  AutoConfigurationPort=17001
#  SlaveStartupPort=17003
#  LicenseForwarderListeningPort=17004
#  SlaveDataRoot=
#  NoGuiMode=false
#  AutoUpdateOverride=false
#  IncludeRCSInLauncherMenu=true
#  DbSSLCertificate=
#  AutoUpdateBlock=NotBlocked


@multi_asset(
    name=f"constants_{ASSET_HEADER['group_name']}",
    outs={
        "NAME": AssetOut(
            **ASSET_HEADER,
            dagster_type=str,
            description="",
        ),
        "FEATURE_CONFIGS": AssetOut(
            **ASSET_HEADER,
            dagster_type=dict,
            description="",
        ),
        "DOCKER_COMPOSE": AssetOut(
            **ASSET_HEADER,
            dagster_type=pathlib.Path,
            description="",
        ),
    },
)
def constants_multi_asset(
    context: AssetExecutionContext,
) -> Generator[Output[dict[OpenStudioLandscapesConfig, dict[str | Any, bool | str | Any]]] | AssetMaterialization | Output[Any] | Output[Path] | Any, None, None]:
    """ """

    yield Output(
        output_name="FEATURE_CONFIGS",
        value=FEATURE_CONFIGS,
    )

    yield AssetMaterialization(
        asset_key=context.asset_key_for_output("FEATURE_CONFIGS"),
        metadata={
            "__".join(
                context.asset_key_for_output("FEATURE_CONFIGS").path
            ): MetadataValue.json(FEATURE_CONFIGS),
        },
    )

    yield Output(
        output_name="NAME",
        value=__name__,
    )

    yield AssetMaterialization(
        asset_key=context.asset_key_for_output("NAME"),
        metadata={
            "__".join(context.asset_key_for_output("NAME").path): MetadataValue.path(
                __name__
            ),
        },
    )

    docker_compose = pathlib.Path(
        "{DOT_LANDSCAPES}",
        "{LANDSCAPE}",
        f"{ASSET_HEADER['group_name']}__{'_'.join(ASSET_HEADER['key_prefix'])}",
        "__".join(context.asset_key_for_output("DOCKER_COMPOSE").path),
        "docker_compose",
        "docker-compose.yml",
    )

    yield Output(
        output_name="DOCKER_COMPOSE",
        value=docker_compose,
    )

    yield AssetMaterialization(
        asset_key=context.asset_key_for_output("DOCKER_COMPOSE"),
        metadata={
            "__".join(
                context.asset_key_for_output("DOCKER_COMPOSE").path
            ): MetadataValue.path(docker_compose),
        },
    )
