"""Deterministic local-coordinate geometry, with no aircraft interface."""
from dataclasses import asdict, dataclass
import math
from typing import Tuple

MAX_WAYPOINTS = 10_000


@dataclass(frozen=True)
class FacadeSpec:
    width_m: float
    height_m: float
    line_spacing_m: float
    standoff_m: float
    speed_m_s: float


@dataclass(frozen=True)
class Point:
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class Plan:
    spec: FacadeSpec
    points: Tuple[Point, ...]
    row_count: int
    actual_spacing_m: float
    route_length_m: float
    ideal_travel_time_s: float

    def to_dict(self):
        return {
            "schema": "vitrobotics-offline-facade-geometry-v1",
            "provenance": "New engineering work authored 2026-09-11; not historical flight software",
            "purpose": "Offline conceptual geometry only; not an executable aircraft mission",
            "coordinate_frame": {
                "units": "metres", "origin": "facade bottom-left",
                "x": "right along facade", "y": "outward normal from facade",
                "z": "up along facade", "facade_plane": "y=0",
            },
            "spec": asdict(self.spec),
            "row_count": self.row_count,
            "actual_spacing_m": self.actual_spacing_m,
            "route_length_m": self.route_length_m,
            "ideal_travel_time_s": self.ideal_travel_time_s,
            "waypoints": [asdict(p) for p in self.points],
            "limitations": [
                "No takeoff, landing, approach or return path",
                "No obstacles, tether dynamics, wind, braking, turn time or rotor envelope",
                "Line spacing is geometric; no spray footprint or cleaning effectiveness model",
                "No flight controller, GPS, global coordinates or executable mission export",
            ],
        }


def plan_facade(spec: FacadeSpec) -> Plan:
    """Sweep horizontally, alternating direction, with equally spaced edge rows.

    Requested spacing is an upper bound. Redistribute rows uniformly so both
    z=0 and z=height are represented without exceeding the rectangle.
    """
    for field, value in asdict(spec).items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{field} must be a finite positive number")
        try:
            valid = math.isfinite(value) and value > 0
        except OverflowError:
            valid = False
        if not valid:
            raise ValueError(f"{field} must be a finite positive number")
    # Reject excessive allocation before calling ceil or constructing a list.
    ratio = spec.height_m / spec.line_spacing_m
    if not math.isfinite(ratio) or ratio > MAX_WAYPOINTS // 2 - 1:
        raise ValueError(f"Requested spacing exceeds the {MAX_WAYPOINTS}-waypoint limit")
    intervals = max(1, math.ceil(ratio))
    row_count = intervals + 1
    spacing = spec.height_m / intervals
    if spacing <= 0:
        raise ValueError("Dimensions are below representable numeric precision")
    points = []
    for row in range(row_count):
        z = spec.height_m if row == intervals else spec.height_m * (row / intervals)
        ends = (0.0, spec.width_m) if row % 2 == 0 else (spec.width_m, 0.0)
        points.extend(Point(x, spec.standoff_m, z) for x in ends)
    # Covers every horizontal row, with vertical connectors totaling height.
    length = spec.width_m * row_count + spec.height_m
    time = length / spec.speed_m_s
    if not math.isfinite(length) or not math.isfinite(time) or time <= 0:
        raise ValueError("Inputs produce an unrepresentable route length or travel time")
    if any(a == b for a, b in zip(points, points[1:])):
        raise ValueError("Dimensions produce duplicate waypoints at floating-point precision")
    return Plan(spec, tuple(points), row_count, spacing, length, time)


def render_svg(plan: Plan) -> str:
    """Return a front-view schematic, preserving the facade aspect ratio."""
    width, height = plan.spec.width_m, plan.spec.height_m
    # Choose the limiting axis without dividing by a tiny normalized ratio.
    if width >= height:
        w, h = 700.0, 700.0 * (height / width)
        if h > 440:
            w, h = w * (440 / h), 440.0
    else:
        w, h = 440.0 * (width / height), 440.0
    left, top = (800 - w) / 2, 80 + (440 - h) / 2
    def pixel(p):
        return left + (p.x / width) * w, top + h - (p.z / height) * h
    coords = " ".join(f"{x:.3f},{y:.3f}" for x, y in map(pixel, plan.points))
    start_x, start_y = pixel(plan.points[0])
    end_x, end_y = pixel(plan.points[-1])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="640" viewBox="0 0 800 640" role="img" aria-labelledby="title desc">
<title id="title">Offline facade coverage path</title>
<desc id="desc">Front view in x and z. All points at y={plan.spec.standoff_m:g} metres. Alternating horizontal sweeps, bottom to top. Conceptual geometry only.</desc>
<rect width="800" height="640" fill="#f6f8fa"/>
<g font-family="system-ui, sans-serif" fill="#172b4d">
<text x="32" y="35" font-size="22">Offline facade coverage geometry</text>
<text x="32" y="59" font-size="13">NEW WORK · 2026-09-11 · Not an aircraft mission</text>
<rect x="{left:.3f}" y="{top:.3f}" width="{w:.3f}" height="{h:.3f}" fill="#e8eef5" stroke="#687888"/>
<polyline points="{coords}" fill="none" stroke="#0969da" stroke-width="2"/>
<circle cx="{start_x:.3f}" cy="{start_y:.3f}" r="5" fill="#198754"/>
<circle cx="{end_x:.3f}" cy="{end_y:.3f}" r="5" fill="#d1242f"/>
<text x="32" y="552" font-size="14">Facade {width:g} × {height:g} m · standoff {plan.spec.standoff_m:g} m · {plan.row_count} rows</text>
<text x="32" y="576" font-size="14">Path {plan.route_length_m:.3f} m · ideal constant-speed time {plan.ideal_travel_time_s:.3f} s</text>
<text x="32" y="600" font-size="12">Green: start · Red: end · x → · z ↑ · y points out of facade</text>
<text x="32" y="622" font-size="12">No obstacle, tether, wind, turn-time, rotor-envelope or cleaning-performance model.</text>
</g></svg>'''
