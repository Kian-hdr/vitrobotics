# Component geometry

These files expose two custom component designs as standard STL meshes: a generated nozzle adapter and one segment of the clockwise propeller guard. They let readers inspect the geometry alongside the [adapter](../../docs/hardware/nozzle-and-hose.md) and [guard](../../docs/hardware/propeller-guards.md) design stories.

| Component | File | Triangles | Mesh bounds, X × Y × Z |
|---|---|---:|---|
| Nozzle adapter, gd11 s1m1 | [Open STL](nozzle-adapter-gd11-s1m1.stl) | 111,702 | 55.000 × 162.000 × 126.782 mm |
| CW guard, v2.1, component 1 | [Open STL](cw-guard-v2_1-component-1.stl) | 61,006 | 129.170 × 217.940 × 40.098 mm |

## Units and export

**All coordinates are in millimetres.** STL does not store a unit declaration, so select millimetres when importing.

The STL files were exported in September 2026 from the archived `gd11_s1m1.3mf` and `Prop_Guard (1).3mf` meshes. The source packages use centimetres; coordinates were multiplied by ten. The exports preserve the original origin, orientation, triangle order and complete mesh without decimation or repair. Slicer settings, thumbnails and package metadata are not included.

The dimensions above are the meshes' axis-aligned bounds, not manufacturing tolerances or an assembled aircraft envelope. Component 1 is one part of the guard, not the complete guard assembly.

## Design scope

These are geometry files for inspection and comparison. They do not contain the original parametric timeline, generative study, material properties, load cases or print setup. They are not a released manufacturing specification or a flight-qualified component package.

The reference airframe is not included. Public distribution terms for the component files will be settled before the repository's public release.
