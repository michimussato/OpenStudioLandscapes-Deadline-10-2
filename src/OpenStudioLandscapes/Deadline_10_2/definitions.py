from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.Deadline_10_2.assets
from OpenStudioLandscapes.Deadline_10_2 import *

LOGGER.info(f"Loading {dist.name} assets...")

assets_base = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Deadline_10_2.assets],
)

constants_base = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Deadline_10_2.constants],
)


defs = Definitions(
    assets=[
        *assets_base,
        *constants_base,
    ],
)
