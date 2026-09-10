# Offline facade coverage planner

**New engineering work authored September 11, 2026.** This module was created for this repository. It is not recovered historical flight software, and it has not been flown or connected to aircraft.

The standard-library Python library creates a deterministic alternating horizontal sweep for a rectangular facade. The result is a geometric study for documentation and design discussion. There is no controller connection, GPS positioning, global coordinate system or executable mission export.

## Run

From the repository root with Python 3.9 or newer:

```sh
python3 -m software.coverage_planner \
  --width 10 --height 7 --spacing 2 --standoff 3 --speed 0.5 \
  --json software/coverage_planner/examples/facade-10x7.json \
  --svg software/coverage_planner/examples/facade-10x7.svg
```

Omit `--json` to print JSON to standard output. Output directories must already exist. Specified output files are replaced. There are no third-party dependencies.

The included example produces **5 sweep rows, 10 waypoints, a 57 m path and 114 s ideal travel time**. All dimensions are illustrative, not recommended operating settings.

## Geometry and interpretation

The local frame places the facade bottom-left corner at the origin. x runs right, z runs up, and +y runs outward from the facade plane y=0. Every path point is at the supplied positive standoff y. Each row spans x=0 to x=width; alternating rows reverse direction. Vertical segments connect adjacent rows.

The requested spacing is a maximum gap between centerlines. The planner uses `ceil(height / spacing)` intervals and redistributes them uniformly so both bottom and top edges are included. For the 7 m example with maximum 2 m spacing, the actual spacing is 1.75 m. Spacing larger than the height still produces two edge rows. No path point extends beyond the facade rectangle in x/z.

Length includes all horizontal sweeps and vertical connectors. Time is length divided by constant speed. It excludes approach, takeoff, landing, return, acceleration, deceleration, turns, dwell, refills and interruptions. Edge-to-edge centerlines do not establish safe aircraft clearance or complete cleaning coverage.

## Library

```python
from software.coverage_planner import FacadeSpec, plan_facade, render_svg

plan = plan_facade(FacadeSpec(
    width_m=10, height_m=7, line_spacing_m=2,
    standoff_m=3, speed_m_s=0.5,
))
print(plan.route_length_m)
geometry = plan.to_dict()
preview = render_svg(plan)
```

Inputs must be finite positive numbers. The planner rejects more than 10,000 waypoints before allocating a path and rejects nonrepresentable numeric outputs. SVG is an x/z front view with standoff stated in its labels. Extremely narrow aspect ratios may render as a visually collapsed facade at screen resolution.

## Limits

This model does not account for obstacles, openings, people, building irregularity, hose/tether forces, wind, braking, rotor envelope, navigation error, fluid pressure, spray footprint or cleaning effectiveness. It does not select safe standoff or speed. No autonomy, flightworthiness or historical flight behavior follows from these outputs. The JSON contains local design geometry only; it is not a flight-controller mission format.

## Validation

```sh
python3 -m unittest discover -s software/coverage_planner/tests -v
```

Tests check edge inclusion, maximum spacing, alternating direction, rectangular bounds, positive axis-aligned segments, route length against independent segment distances, deterministic results, invalid/nonnumeric/nonfinite input rejection, numeric overflow/underflow, bounded allocation, parseable JSON/SVG and actual CLI file generation/error handling.
