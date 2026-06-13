import bpy

# =========================================================================
#  Decimate + export the whole Z-Anatomy scene to one GLB for Three.js.
#  Non-destructive: it adds modifiers (doesn't bake into your .blend) and
#  the exporter applies them on the way out. Change RATIO and re-run freely.
#
#  HOW TO RUN:
#   1. Open the full Z-Anatomy .blend (the one with all the named muscles).
#   2. Switch to the "Scripting" tab at the top of Blender.
#   3. New -> paste this whole file -> press "Run Script" (the play button).
#   4. Wait. The export freezes Blender for a bit on a model this big - normal.
#      Output lands next to your .blend as "decimated_body.glb".
# =========================================================================

# ---- settings ----
RATIO  = 0.1                       # keep 10% of triangles, for EVERYTHING for now
OUTPUT = "//decimated_body.glb"    # "//" = same folder as your .blend file

# ---- put a Decimate modifier on every mesh object ----
count = 0
for obj in bpy.data.objects:
    if obj.type != 'MESH':
        continue  # skip lights, empties, cameras, etc.

    # if we already added one on a previous run, just update its ratio
    existing = obj.modifiers.get('AutoDecimate')
    if existing:
        existing.ratio = RATIO
    else:
        mod = obj.modifiers.new(name='AutoDecimate', type='DECIMATE')
        mod.decimate_type = 'COLLAPSE'
        mod.ratio = RATIO
    count += 1

print(f"AutoDecimate set on {count} mesh objects (ratio = {RATIO})")

# ---- export the whole scene to GLB, baking modifiers, keeping object names ----
bpy.ops.export_scene.gltf(
    filepath      = bpy.path.abspath(OUTPUT),
    export_format = 'GLB',
    export_apply  = True,    # bake the Decimate modifier into exported geometry
    use_selection = False,   # export the entire scene, not just selected objects
)

print("Done. Exported to:", bpy.path.abspath(OUTPUT))
