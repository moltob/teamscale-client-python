from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

from teamscale_client import TeamscaleClient
from teamscale_client.constants import AssessmentMetricColors
from teamscale_client.data import Baseline


TEAMSCALE_URL = "http://localhost:8080"

USERNAME = "admin"
PASSWORD = "admin"

PROJECT_NAME = "test"

def show_baselines(client):
    baselines = client.get_baselines()
    print([str(baseline) for baseline in baselines])

if __name__ == '__main__':
    client = TeamscaleClient(TEAMSCALE_URL, USERNAME, PASSWORD, PROJECT_NAME)

    baseline = Baseline("Test Baseline", "This is a test description", datetime.datetime.now())

    client.add_baseline(baseline)

    show_baselines(client)

    baseline = Baseline("Test Baseline", "This is a test description", datetime.datetime.now())
    client.add_baseline(baseline)

    baseline2 = Baseline("Test Baseline 2", "This is a test description", datetime.datetime.now())
    client.add_baseline(baseline2)

    show_baselines(client)

    client.delete_baseline(baseline2.name)

    show_baselines(client)



