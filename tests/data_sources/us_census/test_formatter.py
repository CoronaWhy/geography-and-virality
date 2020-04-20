from unittest import TestCase

import pandas as pd

from task_geo.data_sources.demographics.us_census.us_census import us_census_formatter
from task_geo.testing import check_dataset_format


class TestUsCensusFormatter(TestCase):

    def test_formatter(self):
        """Validate formatter output for datasource US census."""
        # Setup
        fixture = pd.read_json('tests/fixtures/us_census.json')

        # Run
        data = us_census_formatter(fixture)

        # Check
        check_dataset_format(data)
