# Brand and print tokens

Reuse the user's supplied brand assets or the existing edition's approved identity.
Look first at project files and the corresponding assets/brands example; use available
site CSS as evidence of the identity. Do not assume a particular repository, database,
or approval state exists.

Record selected tokens in the build's brand.json or CSS: paper, ink, accent, secondary,
muted text, rules, display/body/data faces. Retain the hue family while checking actual
contrast and reproduction. White paper is valid, particularly for economical printing.
A pale decorative rule must not carry essential information.

For a new project, choose a restrained provisional system and show a rendered specimen
with the first useful draft. Ask about branding only when it is a real unresolved user
choice; do not block research or writing while waiting for routine token approval.

Fonts must be available in the build, correctly licensed, and contain the required
characters and actual weights. Avoid artificial bold on a face with no bold file.
Use local files during rendering; record their source and license. The default CSS uses
system serif/sans fallbacks so missing custom fonts do not cause a broken starter build,
but inspect the actual final face and embeddings before claiming the brand is matched.

Use assets/design-system.md and assets/print-base.css for type and layout defaults.
Do not copy another destination's entire visual identity because it is the first JSON
file in the examples. Remove accidental production/debug labels from reader-facing output.
