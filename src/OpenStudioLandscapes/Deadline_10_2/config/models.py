import pathlib
from typing import List

from OpenStudioLandscapes.engine.config.models import FeatureBaseModel
from OpenStudioLandscapes.engine.logging.loggers import FEATURE_LOGGER as LOGGER
from pydantic import (
    Field,
    PositiveInt,
)

from OpenStudioLandscapes.Deadline_10_2 import constants, dist


class Config(FeatureBaseModel):
    feature_name: str = dist.name

    group_name: str = constants.ASSET_HEADER["group_name"]

    key_prefixes: List[str] = constants.ASSET_HEADER["key_prefix"]

    enabled: bool = Field(
        default=False,
        description="Not enabled by default because this Feature "
        "has some basic requirements, such as the installers.",
    )

    deadline_10_2_installer_aws_portal_link: pathlib.Path = Field(
        default="<NOT_SET__CHANGE_ME>",
        description="The full path to the downloaded `AWSPortalLink-1.2.x.x-linux-x64-installer.run` "
        "file. The installer itself is not part of this Feature. For more information, "
        "see https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2?tab=readme-ov-file#get-deadline",
    )

    deadline_10_2_installer_deadline_client: pathlib.Path = Field(
        default="<NOT_SET__CHANGE_ME>",
        description="The full path to the downloaded `DeadlineClient-10.2.x.x-linux-x64-installer.run` "
        "file. The installer itself is not part of this Feature. For more information, "
        "see https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2?tab=readme-ov-file#get-deadline",
    )

    deadline_10_2_installer_deadline_repository: pathlib.Path = Field(
        default="<NOT_SET__CHANGE_ME>",
        description="The full path to the downloaded `DeadlineRepository-10.2.x.x-linux-x64-installer.run` "
        "file. The installer itself is not part of this Feature. For more information, "
        "see https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2?tab=readme-ov-file#get-deadline",
    )

    deadline_10_2_repository_install_destination: pathlib.Path = Field(
        default=pathlib.Path(
            "{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/data/opt/Thinkbox/DeadlineRepository10"
        ),
        description="For an OverlayFS, this is the lowest (read-only) lowerdir.",
    )

    deadline_10_2_repository_work_dir: pathlib.Path = Field(
        default=pathlib.Path(
            "{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/data/opt/Thinkbox/DeadlineRepository10"
        ),
        description="If not using OverlayFS, this is usually the same value "
        "as deadline_10_2_repository_install_destination. If "
        "the repository resides on an OverlayFS, this is the "
        "resulting mount point of the overlay.",
    )

    deadline_10_2_database_install_destination: pathlib.Path = Field(
        default=pathlib.Path(
            "{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/data/opt/Thinkbox/DeadlineDatabase10"
        ),
    )

    deadline_10_2_RCS_HTTP_PORT_HOST: PositiveInt = Field(
        default=8888,
        # description="The Kitsu container port.",
        frozen=True,
    )

    deadline_10_2_RCS_HTTP_PORT_CONTAINER: PositiveInt = Field(
        default=8888,
        # description="The Kitsu container port.",
        frozen=True,
    )

    deadline_10_2_WEBSERVICE_HTTP_PORT_HOST: PositiveInt = Field(
        default=8899,
        # description="The Kitsu container port.",
        frozen=True,
    )

    deadline_10_2_WEBSERVICE_HTTP_PORT_CONTAINER: PositiveInt = Field(
        default=8899,
        # description="The Kitsu container port.",
        frozen=True,
    )

    deadline_10_2_LAUNCHER_LISTENING_PORT: PositiveInt = Field(
        default=17000,
        # description="The Kitsu container port.",
        frozen=True,
    )

    deadline_10_2_AUTO_CONFIGURATION_PORT: PositiveInt = Field(
        default=17001,
        # description="The Kitsu container port.",
        frozen=True,
    )

    deadline_10_2_SLAVE_STARTUP_PORT: PositiveInt = Field(
        default=17003,
        # description="The Kitsu container port.",
        frozen=True,
    )

    deadline_10_2_LICENSE_FORWARDER_LISTENING_PORT: PositiveInt = Field(
        # Todo:
        #  - [ ] Check if this port setting is correct (clash with
        #        deadline_10_2_SLAVE_STARTUP_PORT?
        default=17003,
        # description="The Kitsu container port.",
        frozen=True,
    )

    deadline_10_2_APPLICATION_STARTUP_PORT: PositiveInt = Field(
        default=17006,
        frozen=True,
    )

    deadline_10_2_DISABLE_LOCAL_PULSE: bool = Field(
        default=False,
    )

    deadline_10_2_DISABLE_LOCAL_WORKER: bool = Field(
        default=True,
    )

    # MongoDB

    deadline_10_2_mongodb_docker_image: str = Field(
        default="docker.io/mongodb/mongodb-community-server:4.4-ubuntu2004",
        frozen=True,
    )

    deadline_10_2_MONGODB_INSIDE_CONTAINER: bool = Field(
        default=False,
        frozen=True,
    )

    deadline_10_2_MONGO_DB_HOST: str = Field(
        default="mongodb-10-2",
        frozen=True,
    )

    deadline_10_2_MONGO_DB_NAME: str = Field(
        default="deadline10db",
        frozen=True,
    )

    # Todo
    #  - [ ] is there's really a need to expose this?
    deadline_10_2_DEFAULT_DBPATH_CONTAINER: pathlib.Path = Field(
        default=pathlib.Path("/data/db"),
        frozen=True,
    )

    deadline_10_2_MONGO_EXPRESS_PORT_HOST: PositiveInt = Field(
        default=8181,
        frozen=True,
    )

    deadline_10_2_MONGO_EXPRESS_PORT_CONTAINER: PositiveInt = Field(
        default=8081,
        frozen=True,
    )

    deadline_10_2_MONGO_DB_PORT_HOST: PositiveInt = Field(
        default=21017,
        frozen=True,
    )

    deadline_10_2_MONGO_DB_PORT_CONTAINER: PositiveInt = Field(
        default=21017,
        frozen=True,
    )

    # Mongo Express
    # https://hub.docker.com/_/mongo-express/

    deadline_10_2_ME_CONFIG_BASICAUTH_USERNAME: str = Field(
        default="web",
    )

    deadline_10_2_ME_CONFIG_BASICAUTH_PASSWORD: str = Field(
        default="web",
    )

    deadline_10_2_ME_CONFIG_OPTIONS_EDITORTHEME: str = Field(
        default="darcula",
    )

    deadline_10_2_ME_CONFIG_MONGODB_SERVER: str = Field(
        default="mongodb-10-2",
    )

    # Todo:
    #  - [ ] Verify whether MONGO_DB_PORT_CONTAINER or MONGO_DB_PORT_HOST
    #        is actually correct
    deadline_10_2_ME_CONFIG_MONGODB_URL: str = Field(
        default="mongodb://admin:pass@localhost:21017/db?ssl=false",
        # default="mongodb://admin:pass@localhost:{MONGO_DB_PORT_CONTAINER}/db?ssl=false",
        # default="mongodb://admin:pass@localhost:{MONGO_DB_PORT_HOST}/db?ssl=false",
    )

    deadline_10_2_ME_CONFIG_MONGODB_PORT: PositiveInt = Field(
        default=21017,
        frozen=True,
    )

    apt_packages: List = Field(
        default=[
            "bzip2",
        ],
        frozen=True,
    )

    pip_packages: List = Field(
        default=[
            # Todo:
            #  - [ ] (LOW) OpenStudioLandscapes SSL authentication
            # "git+https://github.com/michimussato/SSLGeneration.git@packaging",
            # https://pypi.org/project/gazu/
            "gazu[cli]",
        ],
        frozen=True,
    )

    # my_test_attr: str = Field(
    #     default="hello world",
    # )

    # EXPANDABLE PATHS
    @property
    def deadline_10_2_installer_aws_portal_link_expanded(self) -> pathlib.Path:
        LOGGER.debug(f"{self.env = }")
        if self.env is None:
            raise KeyError("`env` is `None`.")

        LOGGER.debug(f"Expanding {self.deadline_10_2_installer_aws_portal_link}...")
        ret = pathlib.Path(
            self.deadline_10_2_installer_aws_portal_link.expanduser()  # pylint: disable=E1101
            .as_posix()
            .format(
                **{
                    "FEATURE": self.feature_name,
                    **self.env,
                }
            )
        )
        return ret

    @property
    def deadline_10_2_installer_deadline_client_expanded(self) -> pathlib.Path:
        LOGGER.debug(f"{self.env = }")
        if self.env is None:
            raise KeyError("`env` is `None`.")

        LOGGER.debug(f"Expanding {self.deadline_10_2_installer_deadline_client}...")
        ret = pathlib.Path(
            self.deadline_10_2_installer_deadline_client.expanduser()  # pylint: disable=E1101
            .as_posix()
            .format(
                **{
                    "FEATURE": self.feature_name,
                    **self.env,
                }
            )
        )
        return ret

    @property
    def deadline_10_2_installer_deadline_repository_expanded(self) -> pathlib.Path:
        LOGGER.debug(f"{self.env = }")
        if self.env is None:
            raise KeyError("`env` is `None`.")

        LOGGER.debug(f"Expanding {self.deadline_10_2_installer_deadline_repository}...")
        ret = pathlib.Path(
            self.deadline_10_2_installer_deadline_repository.expanduser()  # pylint: disable=E1101
            .as_posix()
            .format(
                **{
                    "FEATURE": self.feature_name,
                    **self.env,
                }
            )
        )
        return ret

    @property
    def deadline_10_2_repository_install_destination_expanded(self) -> pathlib.Path:
        LOGGER.debug(f"{self.env = }")
        if self.env is None:
            raise KeyError("`env` is `None`.")

        LOGGER.debug(
            f"Expanding {self.deadline_10_2_repository_install_destination}..."
        )
        ret = pathlib.Path(
            self.deadline_10_2_repository_install_destination.expanduser()  # pylint: disable=E1101
            .as_posix()
            .format(
                **{
                    "FEATURE": self.feature_name,
                    **self.env,
                }
            )
        )
        return ret

    @property
    def deadline_10_2_repository_work_dir_expanded(self) -> pathlib.Path:
        LOGGER.debug(f"{self.env = }")
        if self.env is None:
            raise KeyError("`env` is `None`.")

        LOGGER.debug(f"Expanding {self.deadline_10_2_repository_work_dir}...")
        ret = pathlib.Path(
            self.deadline_10_2_repository_work_dir.expanduser()  # pylint: disable=E1101
            .as_posix()
            .format(
                **{
                    "FEATURE": self.feature_name,
                    **self.env,
                }
            )
        )
        return ret

    @property
    def deadline_10_2_database_install_destination_expanded(self) -> pathlib.Path:
        LOGGER.debug(f"{self.env = }")
        if self.env is None:
            raise KeyError("`env` is `None`.")

        LOGGER.debug(f"Expanding {self.deadline_10_2_database_install_destination}...")
        ret = pathlib.Path(
            self.deadline_10_2_database_install_destination.expanduser()  # pylint: disable=E1101
            .as_posix()
            .format(
                **{
                    "FEATURE": self.feature_name,
                    **self.env,
                }
            )
        )
        return ret


if __name__ == "__main__":
    CONFIG_STR = Config.get_docs()
else:
    import yaml

    CONFIG_STR = yaml.dump(
        Config.model_json_schema(mode="serialization"),
    )
