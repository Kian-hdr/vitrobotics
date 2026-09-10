# Vitrobotics

**The engineering story of a drone-based façade-cleaning project, formerly Aeroshine.**

Vitrobotics began with a modified DJI Inspire 1 Pro and a practical question: could a drone carry a cleaning system to a building façade and reduce the need for people to work at height?

The initial aircraft was sponsored by Drone Masters Academy, according to project founder Kian Konrad Tajbakhsh. The team tested cleaning at its headquarters, Factory Hammerbrooklyn in Hamburg. The project developed beyond a single prototype, with an emphasis on topology optimization, generative design and custom mechanical engineering.

This repository documents that development: the problem, prototypes, design decisions, physical tests and lessons. It is currently an **incomplete historical engineering record**. It is not a flight-ready build kit or a released autonomous-control system.

![Sampled frames showing the cleaning prototype spraying a building façade](media/flight-4-sampled-frames.jpg)

*Frames sampled from the archived Flight 4 edit. The sequence shows spraying in flight; it does not establish the control mode or cleaning performance.*

## Start here

- [Why the project existed](docs/project-story.md)
- [System architecture and development stages](docs/architecture.md)
- [Generative design and mechanical engineering](docs/hardware/design-process.md)
- [Hardware and CAD register](docs/hardware/cad-register.md)
- [Flight history](docs/flights/README.md)
- [Autopilot and software](docs/software.md)
- [Results, limitations and lessons](docs/results-and-limitations.md)
- [Documentation roadmap](docs/roadmap.md)
- [Evidence and attribution](docs/sources-and-attribution.md)

## What the surviving evidence supports

Original archived video metadata groups the four named test sessions into **4, 15, 19 and 21 December 2024** (camera-metadata dates; clocks were not independently calibrated). The second session's written review says takeoff was aborted. The Flight 4 edited video shows the aircraft airborne, with a hanging hose, spraying the building's windows and façade.

Kian recalls autopilot use through a flight planner. The exact software, automated flight segments and associated session have not yet been recovered. Electrical ground power and swarm operation must not be inferred from the hose or the word “autopilot.”

Kian also reports successor builds and additional flights. Their configuration and chronology remain to be reconciled with the surviving CAD and media.

## Scope

The emphasis is hardware and design documentation. Existing control code and third-party firmware are not released here. Editable CAD will be added selectively after checking design ownership, revision and correspondence with the actual builds. Source papers, contracts and private business records remain in the project archive.

Last documentation update: 11 September 2026.
