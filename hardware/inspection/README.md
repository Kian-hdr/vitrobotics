# Component geometry

These files expose the latest gd34 nozzle adapter, an earlier gd11 alternative and one segment of the clockwise propeller guard as standard STL meshes. They let readers inspect the geometry alongside the [adapter](../../docs/hardware/nozzle-and-hose.md) and [guard](../../docs/hardware/propeller-guards.md) design stories.

| Component | File | Triangles | Mesh bounds, X × Y × Z |
|---|---|---:|---|
| **Latest nozzle adapter, gd34** | [Open STL](nozzle-adapter-gd34.stl) | 113,288 | 55.263 × 162.000 × 127.560 mm |
| Earlier nozzle adapter, gd11 s1m1 | [Open STL](nozzle-adapter-gd11-s1m1.stl) | 111,702 | 55.000 × 162.000 × 126.782 mm |
| CW guard, v2.1, component 1 | [Open STL](cw-guard-v2_1-component-1.stl) | 61,006 | 129.170 × 217.940 × 40.098 mm |

The latest adapter is also available as a [STEP solid](nozzle-adapter-gd34.step), exported directly from the native gd34 design in Fusion in September 2026. It contains one solid and explicitly declares centimetres; a STEP importer reads this unit declaration. The STEP and archived 3MF-derived STL are separate exports; their tessellation and coordinate frames should not be assumed identical.

## Units and export

**All STL coordinates are in millimetres.** STL does not store a unit declaration, so select millimetres when importing.

The STL files were exported in September 2026 from the archived `gd34.3mf`, `gd11_s1m1.3mf` and `Prop_Guard (1).3mf` meshes. The source packages use centimetres; coordinates were multiplied by ten. The exports preserve the original origin, orientation, triangle order and complete mesh without decimation or repair. Slicer settings, thumbnails and package metadata are not included.

The dimensions above are the meshes' axis-aligned bounds, not manufacturing tolerances or an assembled aircraft envelope. Component 1 is one part of the guard, not the complete guard assembly.

## Design scope

These are geometry files for inspection and comparison. The meshes do not contain a parametric timeline, generative study, material properties, load cases or print setup. The [gd34 study documentation](../../docs/hardware/gd34-study.md) records the linked original design inputs separately. They are not a released manufacturing specification or a flight-qualified component package.

The reference airframe is not included. The component files are published for inspection; no open-hardware license has been assigned. See [files and reuse](../../docs/sources-and-attribution.md#files-and-reuse).
