from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.Deadline_10_2.assets
import OpenStudioLandscapes.Deadline_10_2.constants

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
