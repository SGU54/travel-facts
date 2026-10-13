# Select images that belong in this guide

Use relevant images to show a place, object, view, or situation that helps the reader.
Atmosphere can be a valid purpose, provided it is not presented as evidence of a factual
claim. There is no required photo count, coverage percentage, or landscape-only rule.

## Source and permissions

Inspect available project assets first; use a labeled contact sheet when there are many.
A filename is not sufficient evidence of the subject. Reuse supplied and authorized assets
when appropriate. Check source/license/permission for the intended commercial use,
including any required credit. Do not assume all files from a platform share identical
rights or make broad legal claims about entire services without checking their terms.

Maintain a build asset record with slot ID, local file, actual subject/location,
source URL or supplied-file origin, license/permission basis, credit, intended crop,
and caption. Confirm that the subject and location are actually known.

Do not generate or substitute a fictional landmark, route condition, crowd, restaurant,
or field observation as if photographed on location. If an illustration is requested or
appropriate, follow the active image-generation instructions and distinguish it clearly
from documentary photography. Use exact plotting/vector tools for factual charts/maps.

If a necessary image is missing, advance the independent work and provide a specific
brief. Ask the user only for the unavailable asset/rights/choice that actually blocks use.
Do not impose a blanket image-approval stop when the assets are already available.

## Slot and crop

A stable slot ID identifies a build asset (for example A07); the reader's figure number
follows appearance order. Keep one generated slot → figure → page → caption mapping.
Never identify a file only by an ambiguous printed plate letter.

Choose orientation and crop for the subject and page. A portrait can work as a narrow
figure or a deliberately designed full page; it need not be rejected as a file defect.
A wide banner must be composed as a wide crop, not blindly cover-fit until the subject
disappears. Keep originals. Inspect the crop at final display size.

Choose sufficient pixel dimensions for the intended printed dimensions; resizing cannot
restore missing detail. Check the actual decoded image and final PDF, not just file size.
Use local files during rendering and list them in release.json assets. Large base64
payloads can make a build harder to inspect and debug.

## Caption and placement

The caption must be true of the picture. A photograph of one city cannot illustrate
another city's route; a generic busy square cannot substantiate a measured queue time.
Avoid repeated similar photos unless the comparison requires both. Give the analytical
diagram priority when it carries the decision.

Place images near the relevant paragraph, with a readable caption. Do not fill a page's
tail with an unrelated image, crop away the significant subject to save a page, or stack
redundant photo/caption/pull-quote blocks that push the answer onto another page.

## Acceptance

Check every used image at least once, its source record, crop, caption, subject, and
license/credit. Verify successful decoding and no placeholders/broken images. Review
its effect on nearby text after rendering. The legacy validate-images.py has
landscape/size assumptions: use it only when that slot's actual design requires them;
its automatic crop is never a substitute for looking at the image.
