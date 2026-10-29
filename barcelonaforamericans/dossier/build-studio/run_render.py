import sys, os
sys.argv = ['render-paged.py', '.']
# reduce feather passes and timeout to avoid hang; import and call render directly
import importlib.util
spec = importlib.util.spec_from_file_location("rp", "render-paged.py")
rp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rp)
