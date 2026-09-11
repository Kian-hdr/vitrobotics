# CAD register

The mechanical work is organised around adapters, guards, mounting hardware and aircraft assemblies. Fusion contains the native designs; the archive also includes manufacturing exports and frame references.

| Family | Design files and revisions | Role |
|---|---|---|
| Nozzle adapters | `gd11_s1m1.3mf`, `gd21_v1.3mf`, `gd34.3mf`, MK2 brackets | Attach the cleaning nozzle to the aircraft |
| Hose holder | `Hose_Holder_v2.3mf` | Support and secure the hose |
| Propeller guards | v1, v2, v2.1; CW and CCW variants | Guard geometry and assembly development |
| Mounting hardware | Plates v1, v3 and 3.1; top and bottom brackets | Connect the custom parts to the aircraft |
| Spool components | `Spool_Holder_v2.3mf`, `Shaft_v2.3mf` | Spool assembly parts |
| Frame references | JMMRC image and Tarot 680 assembly exports | Reference geometry, kept separate from custom component designs |
| Hexacopter assembly | `20021-000-01_frame-assembly`, `20021-000-01_frame-assembly_v2` | Six-rotor development branch |
| Hexacopter attachments | `Hexacopter_Nozzle_Mount_v2.2`, `Hexacopter_Rotor_Guard_v1.0.0` | Nozzle mount and guards for the later layout |

## Component stories

- [Nozzle and hose](nozzle-and-hose.md)
- [Propeller guards](propeller-guards.md)
- [Successor hexacopter](successor-hexacopter.md)

## Geometry files

The [component geometry folder](../../hardware/inspection/README.md) contains STL inspection exports of the generated nozzle adapter and one clockwise guard component. Coordinates are in millimetres. The [gd34 study record](gd34-study.md) links the latest adapter to its original optimization inputs; the meshes remain separate from editable histories and solver results.

Third-party frame geometry is not included in the component package.

The remaining documentation work is to connect the native studies, manufacturing exports and installed parts for each build. A 3MF mesh alone does not contain the full parametric or optimization history.
