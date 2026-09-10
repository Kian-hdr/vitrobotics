# Route planning and software

A cleaning route has to bring the nozzle across the surface while accounting for the aircraft and the hose. The project explored façade and roof coverage paths as part of that work.

## Historical route planning

The project archive includes a December 2024 screenshot of coverage paths around a Hamburg building. It shows alternating routes across the façade and roof, with editable vertical anchors.

The image preserves the planned geometry. It does not show a mission being executed or identify the planner version. A complete account of the original autopilot configuration requires the saved mission files, application details and matching flight records. The repository therefore keeps the planning image separate from the physical flight demonstrations.

The project's existing control code is not released here.

## Offline coverage planner

The [coverage planner](../software/coverage_planner/README.md) was added in September 2026 to make a basic planning step reproducible. It generates alternating horizontal sweeps for a rectangular façade in a local coordinate frame.

The tool provides:

- Uniform sweep spacing with both façade edges included.
- JSON geometry and an SVG front-view preview.
- Total route length and ideal travel time at constant speed.
- Tests for geometry, numerical limits and command-line behavior.

This module is separate from the software used during the original flights. It has no aircraft connection or flight-controller mission export.

## Model boundaries

The planner handles geometry only. It does not choose a safe standoff distance or speed, and it does not account for obstacles, wind, hose forces, rotor clearance, braking, spray footprint or cleaning quality. Its time estimate excludes takeoff, approach, turns, landing and interruptions.
