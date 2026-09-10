# Vitrobotics

**Drone-based façade cleaning, from a modified aircraft to custom mechanical design.**

[![Watch Aeroshine’s fourth test flight](https://i.ytimg.com/vi/VmThMd9uGMc/hqdefault.jpg)](https://www.youtube.com/watch?v=VmThMd9uGMc)

**[Watch the flight at Factory Hammerbrooklyn](https://www.youtube.com/watch?v=VmThMd9uGMc)** · 58 seconds

Our fourth test-flight video shows the cleaning drone working beside the building, with water supplied from the ground.

## The project

Vitrobotics began as Aeroshine. We wanted to move the cleaning equipment to the façade while keeping the operator and water supply on the ground.

We started with a DJI Inspire 1 Pro sponsored by Drone Masters Academy and modified it for cleaning tests at our headquarters, Factory Hammerbrooklyn in Hamburg. The work extended into custom nozzle mounts, hose attachments, rotor guards and successor aircraft designs. Topology optimization and generative design were central to the mechanical development.

This repository brings together the build story, CAD development, test records and engineering tools.

## Explore the work

| Area | What to explore |
|---|---|
| [Project story](docs/project-story.md) | The problem, starting platform and development direction |
| [Nozzle and hose integration](docs/hardware/nozzle-and-hose.md) | Bringing ground-supplied water to the aircraft |
| [Propeller guards](docs/hardware/propeller-guards.md) | Generated geometry, segmented construction and attachment design |
| [Successor hexacopter](docs/hardware/successor-hexacopter.md) | The later six-rotor CAD assembly |
| [Design process and CAD](docs/hardware/design-process.md) | Design exploration, manufacturing preparation and component families |
| [Component geometry](hardware/inspection/README.md) | STL inspection exports of the nozzle adapter and guard component |
| [Flight and test history](docs/flights/README.md) | December 2024 test sessions and flight footage |
| [Ground power](docs/hardware/ground-power.md) | Power conversion, cable transmission and ground/hover testing |
| [Architecture](docs/architecture.md) | Aircraft, cleaning equipment and ground systems |
| [Software](docs/software.md) | Route planning and the offline coverage tool |

## Engineering tools

The [offline coverage planner](software/coverage_planner/README.md), added in September 2026, generates rectangular façade sweep paths, JSON geometry and an SVG preview. It includes tests for spacing, boundaries, route length and input validation.

It is a planning tool, not aircraft-control software. It does not model obstacles, tether forces, aircraft dynamics or cleaning effectiveness.

## Documentation scope

The flight footage, CAD models and planning tools describe different parts of the project. Flight records cover physical tests; CAD views show design development; the coverage planner is a later software addition. The repository does not provide a flight-ready build package or release the project's control code.

[Engineering results and limits](docs/results-and-limitations.md) · [Documentation roadmap](docs/roadmap.md) · [Project archive and credits](docs/sources-and-attribution.md)
