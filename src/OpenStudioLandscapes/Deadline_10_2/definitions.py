from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.Deadline_10_2.assets
import OpenStudioLandscapes.Deadline_10_2.constants
from OpenStudioLandscapes.engine.features.upstream_asset_specs import assets_external

assets = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Deadline_10_2.assets],
)

constants = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Deadline_10_2.constants],
)


defs = Definitions(
    assets=[
        *assets,
        *constants,
        *assets_external,
    ],
)
