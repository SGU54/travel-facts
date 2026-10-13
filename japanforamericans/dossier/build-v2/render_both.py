import importlib.util, sys, os
spec = importlib.util.spec_from_file_location("rp", os.path.join(os.path.dirname(os.path.abspath(__file__)), "render-paged.py"))
rp = importlib.util.module_from_spec(spec)
sys.modules["rp"] = rp
# the module renders on import (its __main__ guard is a bare call at the bottom);
# read it and strip that so we control both passes
src = open("render-paged.py").read().replace("\nrender()\n", "\n")
exec(compile(src, "render-paged.py", "exec"), rp.__dict__)
print("── BOOK ──");  rp.render("dossier3.html", "dossier.pdf")
print("── SHEET ──"); rp.render("fieldsheet.html", "fieldsheet.pdf")
