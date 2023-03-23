import os
import sys

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", 'tests', "infra"))
if template_dir not in sys.path:
    sys.path.append(template_dir)

try:
    from smoke_test_template import run_smoke
except ImportError:
    raise Exception("Failed to import tools")

envname = "AzureML-Tutorial" if os.environ.get("ENV_TEST_GLOBAL_MODE") else "test-AzureML-Tutorial"
run_smoke(envname)
