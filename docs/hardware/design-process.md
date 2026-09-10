# Generative design and mechanical engineering

Topology optimization and generative design were central to Vitrobotics. We started with an existing aircraft and developed the parts needed to turn it into a cleaning platform: nozzle adapters, hose holders, propeller guards and their mounting hardware. Later work extended into successor aircraft assemblies.

The interesting part was taking a generated shape through printing, assembly and flight. The nozzle had to sit in a useful position. The hose needed to be secured. The guards had to fit around the rotors and remain stable on their mounts. These practical requirements continued to shape the parts after the first design pass.

## From geometry to hardware

The adapter designs use branching forms, with separate plates and brackets for integration. Print preparation added another set of choices: material, orientation, supports and layer profile. The saved adapter slicer setup records both the model material and the additional material needed for supports.

The guards developed through v1, v2 and v2.1 families. Separate CW and CCW versions, segmented rings and revised mounting plates show the work at component and assembly level. Heated inserts and the joining sequence were part of the manufacturing plan.

## Learning from the tests

Flight testing brought attention to details that mattered in use. We changed the nozzle position and hose fixation after the first test. Guard movement on a mount led to changes in fastening. Water exposure, clearance and repairability became part of the mechanical work alongside the geometry.

The component stories follow that progression:

- [Nozzle and hose integration](nozzle-and-hose.md): positioning the cleaning tool and managing the ground-fed hose.
- [Propeller guards](propeller-guards.md): segmented geometry, manufacturing and attachment refinement.
- [Successor hexacopter](successor-hexacopter.md): carrying the component work into a six-rotor assembly.

## Completing the design record

The original Fusion studies will add the loads, constraints, generated alternatives and selection decisions behind these parts. Matching those studies to manufactured revisions and test photographs is the next step. Quantitative comparisons, such as mass savings or structural margins, belong with those studies and measurements.

The [CAD register](cad-register.md) lists the design families covered here.
