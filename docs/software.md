# Flight planning and software

The software work addressed a practical question: how to move a cleaning tool across a façade while an operator supervises the aircraft and manages the ground equipment.

## Original prototype work

Prototype testing included autopilot-assisted flight planning. The project archive also contains a December 2024 visualization of coverage paths around a Hamburg building, with alternating routes across the façade and roof and editable vertical anchors.

This repository is a hardware and flight-test case study, not a reproduction of the original flight-control stack. The historical control implementation and saved missions are not available in this archive. The flight demonstrations and mechanical designs stand separately from the software released here.

## Reproducible coverage planning

The [offline coverage planner](../software/coverage_planner/README.md) was added in September 2026. It turns the geometry of a rectangular façade into an alternating sweep path that readers can generate, inspect and test.

The tool provides:

- Uniform sweep spacing, including both façade edges.
- A local Cartesian path with a constant standoff from the surface.
- JSON geometry and an SVG front-view preview.
- Total route length and ideal travel time at constant speed.
- Tests for geometry, numerical limits and command-line behavior.

The included 10 × 7 m example produces five sweep rows, ten waypoints and a 57 m path. At the illustrative speed of 0.5 m/s, ideal travel time is 114 seconds. These values describe the example geometry, not a historical flight or a recommended operating configuration.

```sh
python3 -m software.coverage_planner \
  --width 10 --height 7 --spacing 2 --standoff 3 --speed 0.5
```

Run this from the repository root. The command prints the path and its summary as JSON. The module README shows how to save JSON and SVG files and run the tests.

## Integration boundary

The planner is an offline engineering tool. It does not connect to an aircraft or export a flight-controller mission. It does not select a safe standoff or speed, and it does not model obstacles, wind, hose forces, rotor clearance, braking, spray footprint or cleaning quality. Its time estimate excludes takeoff, approach, turns, landing and interruptions.

Hardware-specific mission conversion and aircraft validation are separate work. This keeps the published example reproducible without presenting a geometric path as a flight-ready control system.
