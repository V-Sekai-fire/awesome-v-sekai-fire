# Awesome V-Sekai-fire [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of the public projects in the [V-Sekai-fire](https://github.com/V-Sekai-fire) organization: the multiplayer fabric, Godot sandbox guests, Lean 4 contracts, Taskweft planning, avatar and garment tools, and the experiments around them. It is the companion to [Awesome V-Sekai](https://github.com/V-Sekai/awesome-v-sekai).

## How the names work

Most repositories carry a prefix that places them on one side of the workspace hexagon (see [contract-manifest-taskweft](https://github.com/V-Sekai-fire/contract-manifest-taskweft)):

- `contract-` - a specification or interface: Lean proofs, wire formats, shared headers.
- `datasource-` - data the system reads: datasets, avatars, fixtures.
- `entities-` - engines, game projects and domain cores.
- `interactor-` - a unit of work: a plane, a guest, a library or a model image.
- `repository-` - storage interfaces and prebuilt artifacts.
- `service-` - something that runs: a deployment, a container, a build service.
- `transport-` - an edge that carries requests in or out: gateways, CLIs, MCP servers.

This list sorts by subject, not by prefix. Private repositories are not listed.

## Contents

- [Engine and client](#engine-and-client)
- [Workspace, decisions and agreements](#workspace-decisions-and-agreements)
- [Multiplayer fabric: planes, transports and zones](#multiplayer-fabric-planes-transports-and-zones)
- [Game rules as Lean 4 hexagons](#game-rules-as-lean-4-hexagons)
- [godot-sandbox guests (RISC-V)](#godot-sandbox-guests-risc-v)
- [Taskweft and planning](#taskweft-and-planning)
- [Avatars, motion and inverse kinematics](#avatars-motion-and-inverse-kinematics)
- [Godot modules, addons and test projects](#godot-modules-addons-and-test-projects)
- [Garments and 3D content generation](#garments-and-3d-content-generation)
- [Machine learning and inference](#machine-learning-and-inference)
- [MCP servers and agent tools](#mcp-servers-and-agent-tools)
- [Video, audio and broadcast](#video-audio-and-broadcast)
- [Infrastructure, secrets and delivery](#infrastructure-secrets-and-delivery)
- [Worlds, scenes, stories and art](#worlds-scenes-stories-and-art)
- [Datasets and test corpora](#datasets-and-test-corpora)
- [Forks we maintain](#forks-we-maintain)
- [Related](#related)
- [Contributing](#contributing)

## Engine and client

_The Godot engine branch the fabric runs on, and the build that assembles it._

- [entities-assembly](https://github.com/V-Sekai-fire/entities-assembly) - The recipe and driver that assemble the multiplayer-fabric engine branch from feature branches and push it to `entities-godot`. (Elixir)
- [entities-curvenet-godot](https://github.com/V-Sekai-fire/entities-curvenet-godot) (C++)
- [entities-godot](https://github.com/V-Sekai-fire/entities-godot) (C++)
- [entities-images](https://github.com/V-Sekai-fire/entities-images) - Prebuilt Godot engine binaries for the v-sekai-fabric stack, so downstream projects consume a pinned build rather than compile their own. (Just)
- [entities-multiplayer-fabric-rx](https://github.com/V-Sekai-fire/entities-multiplayer-fabric-rx) (GDScript)
- [entities-multiplayer-fabric-xr-dev](https://github.com/V-Sekai-fire/entities-multiplayer-fabric-xr-dev) - Monorepo: Godot engine + XR interaction system + test project.
- [transport-client](https://github.com/V-Sekai-fire/transport-client) - The desktop test client for one zone of the multiplayer fabric: it draws what the zone service sends and sends back a head and two hands. (GDScript)

## Workspace, decisions and agreements

_How the workspace is laid out, decided and checked. Start here._

- [.github](https://github.com/V-Sekai-fire/.github) (Shell)
- [.vscode](https://github.com/V-Sekai-fire/.vscode) - A code editor configuration that builds and debugs the Godot editor from a workspace whose engine source sits in `godot/`.
- [awesome-v-sekai-fire](https://github.com/V-Sekai-fire/awesome-v-sekai-fire) - Awesome list of V-Sekai-fire projects. (Python)
- [contract-bootstrap](https://github.com/V-Sekai-fire/contract-bootstrap) - Workspace bootstrap: pixi env, bootstrap/install scripts and pins, separated from the manifest. (Python)
- [contract-manifest-taskweft](https://github.com/V-Sekai-fire/contract-manifest-taskweft) - The workspace's goal manifest: `default.xml` places every project on a side of the hexagon. (Elixir)
- [contract-multiplayer-fabric-archive](https://github.com/V-Sekai-fire/contract-multiplayer-fabric-archive) - Archived decision records for the v-sekai-fabric stack: rejected and superseded MADRs, and superseded RFDs.
- [contract-multiplayer-fabric-skills](https://github.com/V-Sekai-fire/contract-multiplayer-fabric-skills) - Skills library for V-Sekai multiplayer-fabric agents. (TeX)
- [contract-taskweft-proposals](https://github.com/V-Sekai-fire/contract-taskweft-proposals) - Feature proposals and roadmap for the taskweft project — not for bug reports.
- [dot-claude](https://github.com/V-Sekai-fire/dot-claude) - The agent configuration for the weftspun workspace. (Python)
- [dot-vscode](https://github.com/V-Sekai-fire/dot-vscode) - The editor configuration for the weftspun workspace.
- [fabric](https://github.com/V-Sekai-fire/fabric) - meta repo grouping the gyre dependencies.
- [interactor-infrastructure-logbook](https://github.com/V-Sekai-fire/interactor-infrastructure-logbook) - The fabric's record of itself: the conventions every project works to, the ledger that books the hours, the gates that decide whether the documents are… (Elixir)
- [interactor-study-data-vsk](https://github.com/V-Sekai-fire/interactor-study-data-vsk) - A parquet datalake of the V-Sekai organizations' repositories, issues and decision records, with the studies that rank them. (Python)
- [interactor-tropes-removal-model](https://github.com/V-Sekai-fire/interactor-tropes-removal-model) - A pre-commit and CI gate that finds Simplified Technical English violations in prose and suggests a rewrite for each one. (Python)
- [manuals-weftspun](https://github.com/V-Sekai-fire/manuals-weftspun) - Request for Discussion: the workspace's design and logbook register. (Elixir)
- [repository-witness-cpp](https://github.com/V-Sekai-fire/repository-witness-cpp) - Exception-free property-testing ladder for C++ (doctest-compatible). (C++)
- [weftspun-agreements](https://github.com/V-Sekai-fire/weftspun-agreements) - Weftspun workspace agreements: CLAUDE.md, BLOCKLIST.md, KEYPOINTS.md, PITFALLS.md. (Shell)

## Multiplayer fabric: planes, transports and zones

_The shared-world server stack: the iceoryx2 bus, the authority and fan-out planes, the QUIC/WebTransport edges, and zone hosting._

- [contract-bus](https://github.com/V-Sekai-fire/contract-bus) - The weft plane harness: the iceoryx2 C ABI as a dlsym dispatch table, the shared limits, and the payload types. (C++)
- [contract-command](https://github.com/V-Sekai-fire/contract-command) - The interactor contract: a command in, reply bytes out, and nothing about how it arrived. (C)
- [contract-connection-fsm](https://github.com/V-Sekai-fire/contract-connection-fsm) - Lean4+Plausible model proving the connection FSM is sound and recovers within a 5s transaction limit. (Lean)
- [contract-entity-packet](https://github.com/V-Sekai-fire/contract-entity-packet) - Lean4+Plausible source-of-truth for the integral 100-byte fabric entity packet. (Lean)
- [contract-http3-queue](https://github.com/V-Sekai-fire/contract-http3-queue) - Lean4+Plausible model of the WebTransport/http3 transport concurrency: a mutex-guarded inbound queue (proven size-honest) and a starvation-free… (Lean)
- [contract-interest-mgmt](https://github.com/V-Sekai-fire/contract-interest-mgmt) - Authority-interest + solve-order hexagon: who-sees-whom and solve sequencing. (Lean)
- [contract-protocol](https://github.com/V-Sekai-fire/contract-protocol) - Fabric networking / SLA hexagon: saturation, waypoint bounds, abyssal SLA. (Lean)
- [contract-wt](https://github.com/V-Sekai-fire/contract-wt) - The second opinion: a Python WebTransport client and server used to test the Godot H3/WT implementation by swapping roles. (Python)
- [contract-zone-backend](https://github.com/V-Sekai-fire/contract-zone-backend) - Uro, the Phoenix service that registers zone servers, stores and serves uploaded assets, and signs users in. (Lean)
- [datasource-queen](https://github.com/V-Sekai-fire/datasource-queen) - A text-only settlement game whose world is an embedded SQL database paged into a distributed key-value store, so each turn is durable. (C)
- [entities-enet-godot](https://github.com/V-Sekai-fire/entities-enet-godot) - A complete re-implementation of the ENet protocol in Erlang/OTP. (Erlang)
- [entities-godot-patrol-client](https://github.com/V-Sekai-fire/entities-godot-patrol-client) - A Godot test project that checks the scene synchronizer's packet format against an Elixir spatial node store. (GDScript)
- [interactor-aria-patrol-client](https://github.com/V-Sekai-fire/interactor-aria-patrol-client) - An Elixir client that connects to the Spatial Node Store server and walks an entity along a patrol route. (Elixir)
- [interactor-aria-patrol-solver](https://github.com/V-Sekai-fire/interactor-aria-patrol-solver) - An Elixir application that plans patrol routes through scattered waypoints with a hierarchical task planner and writes the trajectory as JSON. (Elixir)
- [interactor-authority](https://github.com/V-Sekai-fire/interactor-authority) - The authority plane: one zone's single writer, ticking at 20 Hz on the harness ring. (C)
- [interactor-crowd](https://github.com/V-Sekai-fire/interactor-crowd) - The weft crowd plane: a thousand people in one venue, simulated at 60 Hz and published at 20 Hz, one entity for each joint. (Python)
- [interactor-elixir-enet](https://github.com/V-Sekai-fire/interactor-elixir-enet) - An Elixir implementation of the ENet reliable UDP protocol, with DTLS, ported from Erlang. (Elixir)
- [interactor-elixir-entity-database](https://github.com/V-Sekai-fire/interactor-elixir-entity-database) - An Elixir prototype that receives entity states over UDP and passes them through a dataflow pipeline that hashes them. (Elixir)
- [interactor-fabric-zone](https://github.com/V-Sekai-fire/interactor-fabric-zone) - The fabric's zones, client, CA and casync assets as godot-sandbox guest ELFs, with Lean tests beside them. (C++)
- [interactor-janet](https://github.com/V-Sekai-fire/interactor-janet) - The scripted plane: policy in Janet, on iceoryx2.
- [interactor-motion](https://github.com/V-Sekai-fire/interactor-motion) - The active plane: ARDY generates the reference a body follows, and the tracker makes it physical.
- [interactor-physics](https://github.com/V-Sekai-fire/interactor-physics) - The physics interactor: a command in, reply bytes out, over MuJoCo. (C)
- [interactor-quickstart](https://github.com/V-Sekai-fire/interactor-quickstart) - An Elixir tool that brings up the fabric's orchestration engine and its key-value store as local containers under systemd. (Elixir)
- [interactor-spatial-oracle](https://github.com/V-Sekai-fire/interactor-spatial-oracle) - Predictive spatial-oracle hexagon: ghost-expansion + SAH proofs, emitting predictive_bvh.h via AmoLean codegen. (Lean)
- [interactor-tla-game-networking-model](https://github.com/V-Sekai-fire/interactor-tla-game-networking-model) - TLA+ specifications that model-check networking, consensus and storage designs for multiplayer games before they are built. (TLA)
- [interactor-tool](https://github.com/V-Sekai-fire/interactor-tool) - The tool plane: MCP framing over iceoryx2, Godot by dlopen.
- [interactor-vertex](https://github.com/V-Sekai-fire/interactor-vertex) - Experimental backend that serves custom game content. (Elixir)
- [interactor-voice](https://github.com/V-Sekai-fire/interactor-voice) - Voice as sequenced Opus packets in a godot-sandbox guest. (C++)
- [interactor-ward](https://github.com/V-Sekai-fire/interactor-ward) - A server-authoritative networked physics service for one ward, whose state is a SQLite database over a FoundationDB-backed VFS. (C)
- [interactor-weft](https://github.com/V-Sekai-fire/interactor-weft) - The Elixir and OTP control plane of the multiplayer fabric: single-writer actors, a pool reconciler and durable per-actor storage. (Elixir)
- [repository-entity-store](https://github.com/V-Sekai-fire/repository-entity-store) - Side 5: an interface that gets, creates and changes a 100-byte entity over the iceoryx2 ring. (Python)
- [service-behaviour](https://github.com/V-Sekai-fire/service-behaviour) - A domain: the planner decides what a body does, ARDY decides how it moves.
- [service-docker-multiplayer-fabric](https://github.com/V-Sekai-fire/service-docker-multiplayer-fabric) - Container images and a compose file for a zone-server stack: a database, object storage, the Uro API server and scalable zone processes.
- [service-multiplayer-fabric-generate-secrets](https://github.com/V-Sekai-fire/service-multiplayer-fabric-generate-secrets) - Secret and cert generation for the multiplayer-fabric stack. (Shell)
- [service-multiplayer-fabric-hosting](https://github.com/V-Sekai-fire/service-multiplayer-fabric-hosting) - Local simulation stack for multiplayer-fabric (CockroachDB, S3-compatible file system, Caddy). (Just)
- [service-phoenix-uro-webrtc-signaling](https://github.com/V-Sekai-fire/service-phoenix-uro-webrtc-signaling) - An Elixir web service that relays WebRTC offers, answers and candidates between the peers in a lobby. (Elixir)
- [service-zone](https://github.com/V-Sekai-fire/service-zone) - A domain: the zone packing.
- [transport-asset](https://github.com/V-Sekai-fire/transport-asset) - The asset edge: a content-addressed casync chunk CDN. (C)
- [transport-bus-cli](https://github.com/V-Sekai-fire/transport-bus-cli) - The command line as a transport layer: one command over the weft command bus, the interactor's CBOR reply printed. (Python)
- [transport-fanout](https://github.com/V-Sekai-fire/transport-fanout) - The fan-out edge: interest-filtered entity packets out to subscribers, batched by division. (C++)
- [transport-gateway-c](https://github.com/V-Sekai-fire/transport-gateway-c) - The gateway transport layer, in C over picoquic. (C)
- [transport-gateway-python](https://github.com/V-Sekai-fire/transport-gateway-python) - Control streams, terminated a second time, on a stack that shares nothing with the first. (Python)
- [transport-ingest-c](https://github.com/V-Sekai-fire/transport-ingest-c) - The ingest transport layer, in C over picoquic. (C)
- [transport-ingest-python](https://github.com/V-Sekai-fire/transport-ingest-python) - Input datagrams, terminated a second time, on a stack that shares nothing with the first. (Python)

## Game rules as Lean 4 hexagons

_Gameplay and engine rules stated and checked in Lean 4, often with Plausible property tests, then emitted to C or Slang._

- [contract-anny-kernels](https://github.com/V-Sekai-fire/contract-anny-kernels) - The ANNY body model's forward and backward kernels in Lean, emitted through Slang for the in-guest fits. (C++)
- [contract-bone-kernels](https://github.com/V-Sekai-fire/contract-bone-kernels) - The animation mixer's per-frame bone work as Lean kernels, emitted through Slang for GPU clients and servers. (C++)
- [contract-combat](https://github.com/V-Sekai-fire/contract-combat) - Combat hexagon — Lean reducer (combo/invuln/damage), core/ports/adapters triad, wire parity. (Lean)
- [contract-hm08-partition](https://github.com/V-Sekai-fire/contract-hm08-partition) - What hm08 vertex groups cover, stated in Lean. (Python)
- [contract-lbfgsb](https://github.com/V-Sekai-fire/contract-lbfgsb) - L-BFGS-B written in Lean and emitted through Slang to CPU and SPIR-V, with the guest driver drape, cage and headfit share. (C++)
- [contract-lean-deform-exact](https://github.com/V-Sekai-fire/contract-lean-deform-exact) - Proof that bounded-offset deformable sampling is exactly bilinear sampling — Lean 4, 0 sorry. (Lean)
- [contract-lean-hinge-exact](https://github.com/V-Sekai-fire/contract-lean-hinge-exact) - A hinge-sum piecewise linear approximation has slope exactly s m on segment m. (Lean)
- [contract-lean-slang](https://github.com/V-Sekai-fire/contract-lean-slang) - A Lean 4 library that builds a Slang shader AST and prints it as source text, with a check that the text compiles to SPIR-V. It lets a compute kernel be… (Lean)
- [contract-loot](https://github.com/V-Sekai-fire/contract-loot) - Loot hexagon — Lean core + lean-slang SPIR-V kernel, core/ports/adapters triad, SPIR-V parity. (Lean)
- [contract-materialx-shaders-lean](https://github.com/V-Sekai-fire/contract-materialx-shaders-lean) - A Lean 4 model of physically based, toon and vector shaders, all expressed as MaterialX node graphs. (Lean)
- [contract-progression](https://github.com/V-Sekai-fire/contract-progression) - Progression hexagon — profile/inventory rules, affinity gate, sqlite commit valve. (Lean)
- [contract-sinew-align](https://github.com/V-Sekai-fire/contract-sinew-align) - The rotation fitter: its Lean specification and its C port, linked by the drape and headfit guests. (Lean)
- [contract-swing-twist-kusudama](https://github.com/V-Sekai-fire/contract-swing-twist-kusudama) - Lean4+Plausible sim of SwingTwistIK3D + kusudama limitations on a Godot scene tree (JSON-LD input); reproduces the (0,0,5)->(0,5,0) forbidden-area sweep. (Lean)
- [contract-trellis2-mesh-vae-slang](https://github.com/V-Sekai-fire/contract-trellis2-mesh-vae-slang) - Portable Slang + Lean 4 reimplementation of the TRELLIS.2 mesh-VAE encoder forward (mesh -> SLAT tokens).
- [contract-triangulation](https://github.com/V-Sekai-fire/contract-triangulation) - Why a mesher that must keep its boundary cannot also bound its triangle quality, proved in Lean 4 against Mathlib. (Lean)
- [contract-vsekai-materialx](https://github.com/V-Sekai-fire/contract-vsekai-materialx) - PBR/NPR/Slug as stock MaterialX nodes → Slang; ThorVG→Slug vectorization; differentiable via SlangPy. (Lean)
- [entities-humanoid-rom](https://github.com/V-Sekai-fire/entities-humanoid-rom) - Humanoid range-of-motion / IK-constraint hexagon: ROM math, Kusudama, muscle/prismatic constraints. (Lean)
- [entities-lean-combat](https://github.com/V-Sekai-fire/entities-lean-combat) - Standalone Lean 4 workspace for the combat core (canonical hexagon: v-sekai-fabric/combat). (Lean)
- [entities-lean-loot](https://github.com/V-Sekai-fire/entities-lean-loot) - Standalone Lean 4 workspace for the loot core (canonical hexagon: v-sekai-fabric/loot). (Lean)
- [entities-lean-progression](https://github.com/V-Sekai-fire/entities-lean-progression) - Standalone Lean 4 workspace for the progression core (canonical hexagon: v-sekai-fabric/progression). (Lean)
- [entities-lean-rebac](https://github.com/V-Sekai-fire/entities-lean-rebac) - Relationship-based access-control hexagon (NoGod / ReBAC): dependency-free authorization core. (Lean)
- [entities-lean-shared](https://github.com/V-Sekai-fire/entities-lean-shared) - Shared primitive types — the dependency-free common vocabulary every v-sekai-fabric hexagon core builds on. (Lean)

## godot-sandbox guests (RISC-V)

_Programs that run as sandboxed RISC-V ELF guests inside Godot through godot-sandbox and libriscv._

- [contract-ggml-rd](https://github.com/V-Sekai-fire/contract-ggml-rd) - ggml's backend on Godot's RenderingDevice for godot-sandbox guests: Lean-emitted kernels, a CPU fallback, L2 and graph oracles. (C++)
- [contract-guest-common](https://github.com/V-Sekai-fire/contract-guest-common) - The shared headers the dress-on guests include: blake3 and the mesh wire format. (C++)
- [contract-guest-runtime](https://github.com/V-Sekai-fire/contract-guest-runtime) - The godot-sandbox guest runtime the dress-on ELFs share: sandbox API, rd_compute, fiber and pump, godot_lite, slang-rt. (C++)
- [entities-godot-bird-plane](https://github.com/V-Sekai-fire/entities-godot-bird-plane) - A Godot demo of a bird-plane in flight whose thrust, turning and follow camera run as C++ programs in the godot-sandbox addon. (GDScript)
- [entities-godot-enet-sandbox](https://github.com/V-Sekai-fire/entities-godot-enet-sandbox) - A Python bridge that speaks JSON-RPC 2.0 over ENet to sandboxed programs in a running Godot instance. (Python)
- [entities-godot-gdscript-compiler-demo](https://github.com/V-Sekai-fire/entities-godot-gdscript-compiler-demo) - An engine project that runs a sandboxed script and compiles its source to a RISC-V program with the sandbox addon's in-guest compiler. (GDScript)
- [entities-godot-sandbox-gdscript-compiler](https://github.com/V-Sekai-fire/entities-godot-sandbox-gdscript-compiler) - A compiler from GDScript to RISC-V ELF programs that run as godot-sandbox guests. (C++)
- [entities-godot-sandbox-robust-weight-transfer](https://github.com/V-Sekai-fire/entities-godot-sandbox-robust-weight-transfer) - An engine project that runs robust skin weight transfer, by weight inpainting, inside a sandboxed RISC-V guest. (C++)
- [entities-libriscv](https://github.com/V-Sekai-fire/entities-libriscv) (C++)
- [hypercore-chat-guest](https://github.com/V-Sekai-fire/hypercore-chat-guest) - P2P DHT chat on hypercore as a godot-sandbox RISC-V guest, Lean 4.
- [interactor-bake](https://github.com/V-Sekai-fire/interactor-bake) - Alpha culling and texture atlases for avatar meshes as a godot-sandbox guest, the CPU part of RFD 2284's bake stage. (C++)
- [interactor-cage](https://github.com/V-Sekai-fire/interactor-cage) - The cage stage as a godot-sandbox guest: the (1,3) biharmonic bind and the in-motion cage fit on L-BFGS-B. (C++)
- [interactor-curvenet](https://github.com/V-Sekai-fire/interactor-curvenet) - The curvenet stage as a godot-sandbox guest: CASSIE strokes to a curve network and a mesh, with its sketch graph. (C++)
- [interactor-drape](https://github.com/V-Sekai-fire/interactor-drape) - The drape stage as a godot-sandbox guest: AVBD cloth from Lean kernels on the CPU and on RenderingDevice. (C++)
- [interactor-garment-fit](https://github.com/V-Sekai-fire/interactor-garment-fit) - The fit stage as a godot-sandbox guest: cloth-fit's PolyFEM garment solve with the Lean SDF sampler. (C++)
- [interactor-headfit](https://github.com/V-Sekai-fire/interactor-headfit) - The head fit as a godot-sandbox guest: the ANNY head fit and the unified-expression transfer. (C++)
- [interactor-lasso](https://github.com/V-Sekai-fire/interactor-lasso) - The lasso as a godot-sandbox guest: far-target picking by a pointing cone, with its Lean tests. (C++)
- [interactor-lean-guest](https://github.com/V-Sekai-fire/interactor-lean-guest) - Lean 4 programs as static riscv64 guest ELFs for godot-sandbox (libriscv). (CMake)
- [interactor-motion-guest](https://github.com/V-Sekai-fire/interactor-motion-guest) - Kimodo and MotionBricks motion on ggml-rd as a godot-sandbox guest, for the in-motion dress fit. (C++)
- [interactor-mujoco-cloth-sim](https://github.com/V-Sekai-fire/interactor-mujoco-cloth-sim) - Deterministic cloth on a RISC-V/MuJoCo guest: a garment-craft sim whose constraint solve is bit-identical on every host. (GDScript)
- [interactor-mujoco-riscv64](https://github.com/V-Sekai-fire/interactor-mujoco-riscv64) - riscv64 Linux build of MuJoCo, with libriscv host bindings (seeded from zone-server-h2o's own vendored mujoco + mj_physics.c wiring). (C)
- [interactor-mujoco-sandbox-demo](https://github.com/V-Sekai-fire/interactor-mujoco-sandbox-demo) - A physics library built as a RISC-V guest program that an engine project loads into a sandbox and steps from script. (GDScript)
- [interactor-multiplayer-fabric-elf-programs](https://github.com/V-Sekai-fire/interactor-multiplayer-fabric-elf-programs) - Sandboxed RISC-V guest programs for the multiplayer fabric: grid simulation kernels and an HTN planner with holographic memory. (C++)
- [interactor-remesh](https://github.com/V-Sekai-fire/interactor-remesh) - meshoptimizer's voxel remesher and simplifier as a godot-sandbox guest, the remesh stage of RFD 2284. (C++)
- [interactor-rfdetr-seg-guest](https://github.com/V-Sekai-fire/interactor-rfdetr-seg-guest) - RF-DETR instance segmentation on ggml-rd as a godot-sandbox guest. (Elixir)
- [interactor-slughorn](https://github.com/V-Sekai-fire/interactor-slughorn) - slughorn for slug.elf: SVG to curve and band data and baked meshes, with ThorVG and Clipper2. (C++)
- [interactor-taskweft-crowd](https://github.com/V-Sekai-fire/interactor-taskweft-crowd) - A deterministic transit-station crowd on a RISC-V/MuJoCo guest: thousands of taskweft HTN agents steer through a shared station, bit-identical on every host. (GDScript)
- [interactor-usd-guest](https://github.com/V-Sekai-fire/interactor-usd-guest) - OpenUSD from bytes as a godot-sandbox guest: usd.elf and its Gate 0G probe. (C++)
- [repository-riscv64-sysroot](https://github.com/V-Sekai-fire/repository-riscv64-sysroot) - A committed riscv64-linux-gnu sysroot, so clang on any host can build and link RISC-V Linux binaries without a cross-toolchain or a container. (C++)
- [service-weft-warp-burrito](https://github.com/V-Sekai-fire/service-weft-warp-burrito) - An Elixir host that runs a sandboxed RISC-V guest through a NIF, one supervised process per guest machine, released as a single executable. (C++)

## Taskweft and planning

_Hierarchical task network planning: the Taskweft planner, its domains, and the agents that use it._

- [datasource-easy-diffusion-traces](https://github.com/V-Sekai-fire/datasource-easy-diffusion-traces) - taskweft JSON-LD session traces for easy-diffusion-mcp (plans, spans, curated image sweeps).
- [entities-multiplayer-fabric-rpg](https://github.com/V-Sekai-fire/entities-multiplayer-fabric-rpg) - Monorepo: VR-MMOG-RPG game layer (HTN planning, taskweft).
- [interactor-aria-blocks](https://github.com/V-Sekai-fire/interactor-aria-blocks) - The blocks-world planning domain written for aria-hybrid-planner, with tests that plan the classic problems. (Elixir)
- [interactor-aria-bmesh](https://github.com/V-Sekai-fire/interactor-aria-bmesh) - An Elixir library that holds n-gon meshes as vertices, edges, face-corner loops and faces, and walks the topology between them. (Elixir)
- [interactor-aria-carbs](https://github.com/V-Sekai-fire/interactor-aria-carbs) - An Elixir library that drives the CARBS cost-aware Bayesian hyperparameter optimizer through embedded Python. (Elixir)
- [interactor-aria-core](https://github.com/V-Sekai-fire/interactor-aria-core) - Shared Elixir utilities for the aria applications: a Bayesian success-rate estimator, UUIDv7 generation and changeset validators. (Elixir)
- [interactor-aria-fate](https://github.com/V-Sekai-fire/interactor-aria-fate) - Character generation and planning for an aspect-based tabletop role-playing system, built on its CC BY reference documents. (Elixir)
- [interactor-aria-gltf](https://github.com/V-Sekai-fire/interactor-aria-gltf) - An Elixir umbrella that reads and processes glTF 2.0 assets, manages joint hierarchies, and solves inverse kinematics over them. (Elixir)
- [interactor-aria-lbfgspp](https://github.com/V-Sekai-fire/interactor-aria-lbfgspp) - An Elixir library that drives the LBFGS++ limited-memory quasi-Newton optimizer through a NIF. (Elixir)
- [interactor-aria-math](https://github.com/V-Sekai-fire/interactor-aria-math) - Vector, matrix, quaternion and interval maths on Nx tensors, with goal, temporal-constraint and workflow solvers built on them. (Elixir)
- [interactor-aria-planner](https://github.com/V-Sekai-fire/interactor-aria-planner) - A hierarchical task planner in Elixir with temporal scheduling, where a persona is defined by its capability set alone. (Elixir)
- [interactor-aria-qcp](https://github.com/V-Sekai-fire/interactor-aria-qcp) - An Elixir implementation of the quaternion characteristic polynomial method for the optimal rotation and translation between two point sets. (Elixir)
- [interactor-aria-simple-travel](https://github.com/V-Sekai-fire/interactor-aria-simple-travel) - A travel planning domain in Elixir, where people walk or take a taxi between places under time and cash limits. (Elixir)
- [interactor-aria-storage](https://github.com/V-Sekai-fire/interactor-aria-storage) - An Elixir library for content-defined chunk storage that reads and writes the casync and desync chunk-store format. (Elixir)
- [interactor-aria-temporal-blocks](https://github.com/V-Sekai-fire/interactor-aria-temporal-blocks) - A temporal blocks-world planning domain in Elixir, with durative actions, for testing the hybrid planner. (Elixir)
- [interactor-aria-town](https://github.com/V-Sekai-fire/interactor-aria-town) - An Elixir application that keeps a town's non-player characters, its game clock and its persistence under one supervision tree. (Elixir)
- [interactor-ranktration](https://github.com/V-Sekai-fire/interactor-ranktration) - Rank/compare algorithms, models, or approaches with weighted multi-criteria analysis. (Elixir)
- [interactor-rebac](https://github.com/V-Sekai-fire/interactor-rebac) - ReBAC graph traversal for Elixir, backed by taskweft-nif. (Elixir)
- [interactor-taskweft](https://github.com/V-Sekai-fire/interactor-taskweft) - The planner plane: an HTN planner that decides what a body should do, not how it moves. (Elixir)
- [interactor-taskweft-function-block-diagram](https://github.com/V-Sekai-fire/interactor-taskweft-function-block-diagram) - Lean 4 compiler from IEC 61131-3 PLCopen FBD (XML) to RISC-V ELF for godot-sandbox. (Lean)
- [interactor-taskweft-function-block-diagram-teacher](https://github.com/V-Sekai-fire/interactor-taskweft-function-block-diagram-teacher) - A teacher model that speaks IEC 61131-3 Function Block Diagrams: dataset, pretraining, reinforcement training. (Python)
- [interactor-taskweft-godot-sandbox](https://github.com/V-Sekai-fire/interactor-taskweft-godot-sandbox) - Load an OpenPLC-compiled RECTGTN .riscv into a Godot process via lib_godot_connector. (Elixir)
- [interactor-taskweft-mmog-agent](https://github.com/V-Sekai-fire/interactor-taskweft-mmog-agent) - ArtifactsMMO Multiplayer Fabric agent — HTN planning (Taskweft) + ex_ratatui TUI. (Elixir)
- [interactor-taskweft-nmm-personas](https://github.com/V-Sekai-fire/interactor-taskweft-nmm-personas) - IEC 60848 GRAFCET personas playing Neural MMO 2 over 2-contract/bus, with MaskScore traces. (Elixir)
- [transport-artifacts-mmo-mcp](https://github.com/V-Sekai-fire/transport-artifacts-mmo-mcp) - MCP server that plays ArtifactsMMO and records paired planner/API traces for taskweft. (Elixir)
- [transport-mcp-client](https://github.com/V-Sekai-fire/transport-mcp-client) - MCP client, peer behaviour, and solver wiring for Taskweft. (Elixir)

## Avatars, motion and inverse kinematics

_Humanoid bodies, VRM avatars, retargeting, IK solvers, tracking hardware and motion generation._

- [contract-anny](https://github.com/V-Sekai-fire/contract-anny) - The ANNY parametric human body model, carried from naver/anny. (Jupyter Notebook)
- [contract-anny-keypoint-anchors](https://github.com/V-Sekai-fire/contract-anny-keypoint-anchors) - Where the COCO-WholeBody 133 keypoints sit on ANNY's base mesh, as vertex weights, checked against the data. (Python)
- [contract-orbit-views](https://github.com/V-Sekai-fire/contract-orbit-views) - The orbit-view standard: one subject seen from cameras spread evenly around it, as a still sheet or a clip. (Python)
- [datasource-anim-female-doll-retargeting](https://github.com/V-Sekai-fire/datasource-anim-female-doll-retargeting) - A game-engine project that retargets dance and walk animations onto a set of humanoid avatars, the female doll among them. (GDShader)
- [datasource-anim-female-face](https://github.com/V-Sekai-fire/datasource-anim-female-face) - A blendshape face model and its baked exports, staged for turning facial blendshape animation into skinned bone animation. (GDShader)
- [datasource-anim-ik-samples](https://github.com/V-Sekai-fire/datasource-anim-ik-samples) - A Godot project of inverse-kinematics test cases: rigs, avatars and scenes for checking IK solvers. (GDShader)
- [datasource-sk-faavrs-breadbread](https://github.com/V-Sekai-fire/datasource-sk-faavrs-breadbread)
- [datasource-sk-fire-black-cat-girl](https://github.com/V-Sekai-fire/datasource-sk-fire-black-cat-girl) - Source files for the black cat fire avatar: the current VRM release, its editable base mesh, and earlier versions and outfits.
- [datasource-sk-Latifa-V2](https://github.com/V-Sekai-fire/datasource-sk-Latifa-V2) - An engine project that holds the Latifa V2 avatar as VRM, with the V-Sekai avatar tooling as addons. (GDShader)
- [datasource-sk-skeleton-merge-01](https://github.com/V-Sekai-fire/datasource-sk-skeleton-merge-01) - An engine project of avatars, clothing and animation clips for trying the skeleton merge tool on. (GDScript)
- [datasource-sk-test-chan-01](https://github.com/V-Sekai-fire/datasource-sk-test-chan-01) - A game-engine project that prepares the public-domain Test-Chan avatar for upload to a social VR platform. (ShaderLab)
- [datasource-skel-liqu](https://github.com/V-Sekai-fire/datasource-skel-liqu) (GDScript)
- [entities-anny-creator](https://github.com/V-Sekai-fire/entities-anny-creator) - A character creator with sliders over a parametric human. (GDScript)
- [entities-godot-toon-shaders](https://github.com/V-Sekai-fire/entities-godot-toon-shaders) - Godot ports + a shared parameter map for avatar toon shaders (MToon 0.x / MToon10, with planned SCSS and lilToon ports) to ease cross-shader parameter porting. (GDScript)
- [entities-tundra-and-vive-tracker-chest-mount](https://github.com/V-Sekai-fire/entities-tundra-and-vive-tracker-chest-mount) - Printable models for a chest mount that holds a body-tracking puck on a camera chest harness, from two community designs.
- [frame-controller-sim](https://github.com/V-Sekai-fire/frame-controller-sim) - A VR runtime driver that adds companion pen controllers beside the two a person holds, moved through a shared-memory contract. (C++)
- [frame-eye-osc](https://github.com/V-Sekai-fire/frame-eye-osc) - Transmitting Steam Frame Eye Tracking Data via OSC. (Slang)
- [interactor-blender-bone-to-mesh](https://github.com/V-Sekai-fire/interactor-blender-bone-to-mesh) - A 3D editor add-on that turns the bones of the selected armature into one mesh. (Python)
- [interactor-fire-smol-slimes](https://github.com/V-Sekai-fire/interactor-fire-smol-slimes) - A plan for a twenty-tracker wireless inertial motion-capture suit, for animating game characters. (Python)
- [interactor-g1-sim-to-real](https://github.com/V-Sekai-fire/interactor-g1-sim-to-real) - The G1 humanoid sim-to-real environment: MuJoCo rig, joint-range envelope, PPO task with GGUF policy export. (Python)
- [interactor-gait-classification](https://github.com/V-Sekai-fire/interactor-gait-classification) - WEAR HAR + gait/biomechanics: single-limb inertial pipeline. (Python)
- [interactor-kimodo-text-to-motion](https://github.com/V-Sekai-fire/interactor-kimodo-text-to-motion) - Model image for kimodo_text_to_motion. (Python)
- [interactor-pose-consensus](https://github.com/V-Sekai-fire/interactor-pose-consensus) - Four independent pose estimators via pythonx; a keypoint set is accepted only when they agree. (Python)
- [interactor-shader-motion-mirror](https://github.com/V-Sekai-fire/interactor-shader-motion-mirror) - ShaderMotion is a motion-to-video codec for Unity humanoid avatar, whose core system is completely written in shader language HLSL. (C#)
- [interactor-skintokens-auto-rig](https://github.com/V-Sekai-fire/interactor-skintokens-auto-rig) - Model image for skintokens_auto_rig. (Python)
- [interactor-test-ewbik](https://github.com/V-Sekai-fire/interactor-test-ewbik) - Test scenes for the EWBIK inverse kinematics solver as a Godot 4 project: simple bone chains, an arm, and full avatars. (GDScript)
- [interactor-test-godot-vrm-motion-checker](https://github.com/V-Sekai-fire/interactor-test-godot-vrm-motion-checker) - A Godot project that plays a dance clip on VRM avatars to check their motion, node constraints and spring bones. (GDScript)
- [interactor-test-many-bone-ik](https://github.com/V-Sekai-fire/interactor-test-many-bone-ik) - A game-engine test project that poses rigged characters with a many-bone inverse-kinematics solver and its joint constraints. (GDScript)
- [interactor-test-range-of-motion](https://github.com/V-Sekai-fire/interactor-test-range-of-motion)
- [interactor-tool-walk-the-dog](https://github.com/V-Sekai-fire/interactor-tool-walk-the-dog) - A vector-quantized periodic autoencoder that aligns motion across different morphologies. (Python)
- [transport-meshing-pen](https://github.com/V-Sekai-fire/transport-meshing-pen) - The meshing pen: an XR project where a person draws a character and outfit with their hands, and wears it. (GDScript)

## Godot modules, addons and test projects

_Engine modules, GDExtensions, editor addons and the small projects that check them._

- [entities-aria-godot](https://github.com/V-Sekai-fire/entities-aria-godot) - An Elixir library that parses Godot's text scene (`.tscn`) and text resource (`.tres`) files. (Elixir)
- [entities-cassie-flow-project](https://github.com/V-Sekai-fire/entities-cassie-flow-project) - Headless Godot checks for modules/cassie in entities-godot. (GDScript)
- [entities-godot-3dgs](https://github.com/V-Sekai-fire/entities-godot-3dgs) - Godot 3DGS gaussian splatting experiments. (GDScript)
- [entities-godot-bidirected-graph-min-deviation-flow](https://github.com/V-Sekai-fire/entities-godot-bidirected-graph-min-deviation-flow) - A Godot GDExtension that runs libsatsuma's minimum-deviation-flow solver on a bidirected graph. (C++)
- [entities-godot-catlin-and-the-lucky-cat](https://github.com/V-Sekai-fire/entities-godot-catlin-and-the-lucky-cat) - A Magical Girls Game Jam 7 game where spells are cast by drawing gestures with the mouse. (GDScript)
- [entities-godot-cineform](https://github.com/V-Sekai-fire/entities-godot-cineform) - CineForm for Godot Movie Maker. (C++)
- [entities-godot-farm-chickens](https://github.com/V-Sekai-fire/entities-godot-farm-chickens) - A minimal sample project for Godot 4's network replication system. (GDScript)
- [entities-godot-ipfs](https://github.com/V-Sekai-fire/entities-godot-ipfs) - A small game-engine project that runs a bundled IPFS node as a child process and fetches content by its link. (GDScript)
- [entities-godot-mascot-mousse](https://github.com/V-Sekai-fire/entities-godot-mascot-mousse) - An engine foundation's character mascot as a 3D scene file with its physically based textures.
- [entities-godot-mujoco](https://github.com/V-Sekai-fire/entities-godot-mujoco) - MuJoCo physics for Godot as a PhysicsServer3DExtension that delegates stepping to the godot-sandbox RISC-V guest. (C++)
- [entities-godot-mujoco-demo](https://github.com/V-Sekai-fire/entities-godot-mujoco-demo) - A RigidBody3D dropping onto a floor, simulated by the native MuJoCo PhysicsServer3DExtension from entities-godot-mujoco. (GDScript)
- [entities-godot-onnx](https://github.com/V-Sekai-fire/entities-godot-onnx) - A Rust GDExtension that loads ONNX models in Godot and runs inference on tensors from GDScript. (Rust)
- [entities-godot-paint-mixer](https://github.com/V-Sekai-fire/entities-godot-paint-mixer) - A Godot project that mixes two paint colours the way pigments mix, through spectral reflectance, and shows the palette between them. (GDScript)
- [entities-godot-primitive-tools](https://github.com/V-Sekai-fire/entities-godot-primitive-tools)
- [entities-godot-springbone-test](https://github.com/V-Sekai-fire/entities-godot-springbone-test) - An engine test scene that loops a walking rig through the spring-bone simulator, with a checkbox that resets the simulation on each loop. (GDScript)
- [entities-godot-visual-anomaly-detection](https://github.com/V-Sekai-fire/entities-godot-visual-anomaly-detection) - A one-class visual anomaly detector, trained on images of normal avatar poses, for spotting rendering bugs. (Python)
- [entities-godot-wmf-game-project](https://github.com/V-Sekai-fire/entities-godot-wmf-game-project) - A minimal engine project that loops one short video clip, for testing a native media-framework video playback backend.
- [entities-idtx-flow-project](https://github.com/V-Sekai-fire/entities-idtx-flow-project) - Headless Godot test project for the idtx-flow GDExtension. (GDScript)
- [entities-khr-interactivity-samples](https://github.com/V-Sekai-fire/entities-khr-interactivity-samples) - Sample behavior graphs in the JSON form of the KHR_interactivity glTF extension, for testing graph runtimes and compilers.
- [entities-multiplayer-fabric-abyssal](https://github.com/V-Sekai-fire/entities-multiplayer-fabric-abyssal) - Abyssal VR zone client — operator camera, headless observer, fabric client. (GDScript)
- [entities-multiplayer-fabric-cycle-tests](https://github.com/V-Sekai-fire/entities-multiplayer-fabric-cycle-tests) - Maglev cycle smoke tests — minimal Godot scenes that verify each cycle's pass criteria end-to-end against live infrastructure. (GDScript)
- [entities-multiplayer-fabric-humanoid-project](https://github.com/V-Sekai-fire/entities-multiplayer-fabric-humanoid-project) - A Godot test project that encodes a humanoid pose as muscle values and drives a skeleton back from them, with sample avatars and clips. (GDScript)
- [entities-multiplayer-fabric-interaction-system](https://github.com/V-Sekai-fire/entities-multiplayer-fabric-interaction-system) - Delegates input events, such as mouse or VR controller clicks, as 3D raycasts into a scene, with canvas_plane for UI. (GDScript)
- [entities-multiplayer-fabric-interaction-system-project](https://github.com/V-Sekai-fire/entities-multiplayer-fabric-interaction-system-project) - Godot test project for multiplayer-fabric-interaction-system. (GDScript)
- [entities-opentelemetry-godot-project](https://github.com/V-Sekai-fire/entities-opentelemetry-godot-project) - Integration test: Godot open_telemetry module → standard OTLP collector. (C++)
- [entities-order-independent-transparency](https://github.com/V-Sekai-fire/entities-order-independent-transparency) - A test stack that draws the engine's froxel order-independent transparency and checks it against sorted blending. (GDScript)
- [entities-sponza-godot-audio](https://github.com/V-Sekai-fire/entities-sponza-godot-audio) - A nice-looking 3D demo and benchmark for Godot 4, based on the Sponza from Crytek. (GDScript)
- [entities-zone-baker](https://github.com/V-Sekai-fire/entities-zone-baker) - Minimal Godot project for headless VSK asset validation and export. (GDScript)
- [interactor-addon-correct-bone-direction](https://github.com/V-Sekai-fire/interactor-addon-correct-bone-direction) - A Godot 4 editor plugin that corrects the bone directions of imported skeletons and the bind poses of their meshes. (GDScript)
- [interactor-addon-force-bone-forward](https://github.com/V-Sekai-fire/interactor-addon-force-bone-forward) - A Godot editor addon that re-rests an imported skeleton so each bone points toward its children. (GDScript)
- [interactor-flow](https://github.com/V-Sekai-fire/interactor-flow) - The Immersive Digital Twin Experience Flow (IDTX Flow) plugin for Godot, from idtx-flow. (C++)
- [interactor-flow-project](https://github.com/V-Sekai-fire/interactor-flow-project) - A Godot project that exercises the IDTXFlow scene-import addon against the canonical ANNY animation fixture. (GDScript)
- [interactor-mp-seeking-test](https://github.com/V-Sekai-fire/interactor-mp-seeking-test) - A Godot test project that plays a short open film and seeks it with a slider. (GDScript)
- [interactor-multiplayer-fabric-meta](https://github.com/V-Sekai-fire/interactor-multiplayer-fabric-meta) - Meta XR Simulator OpenXR runtime setup for multiplayer-fabric macOS smoke test. (Elixir)
- [interactor-test-javascript](https://github.com/V-Sekai-fire/interactor-test-javascript) - A one-scene Godot project that runs an ECMAScript module as a node's script. (JavaScript)
- [interactor-test-material-x](https://github.com/V-Sekai-fire/interactor-test-material-x) - An engine test project with an editor import plugin that turns MaterialX documents into materials. (GDScript)
- [interactor-test-scripting-01](https://github.com/V-Sekai-fire/interactor-test-scripting-01) - Trigger to switch the texture a to texture b.
- [interactor-tool-godot-cage-deformer](https://github.com/V-Sekai-fire/interactor-tool-godot-cage-deformer) - A Godot extension that deforms a mesh with a triangle cage using biharmonic coordinates. (C++)
- [interactor-tool-godot-curvenet](https://github.com/V-Sekai-fire/interactor-tool-godot-curvenet) - Pixar-style CurveNet profile-curve deformer for Godot, with on-the-fly tri-to-quad fusion via LEMON max-weight matching. (Makefile)
- [interactor-tool-godot-curvenet-archive](https://github.com/V-Sekai-fire/interactor-tool-godot-curvenet-archive) - Retired algorithm specs and benches from TOOL_godot_curvenet. (C++)

## Garments and 3D content generation

_weftfit garment retargeting, mesh processing, and image- or text-to-3D model images._

- [biharmonic-3d-coordinates-siggraph-2024](https://github.com/V-Sekai-fire/biharmonic-3d-coordinates-siggraph-2024) - Reference code for biharmonic 3D coordinates (SIGGRAPH 2024). (C++)
- [contract-billboard-labels](https://github.com/V-Sekai-fire/contract-billboard-labels) - RFD 0074: 3D caption labels over weftspun-3d-studio's billboard gallery cards. (HTML)
- [interactor-blender-meshoptimizer](https://github.com/V-Sekai-fire/interactor-blender-meshoptimizer) - An add-on for an open-source 3D creation suite that simplifies the selected meshes to a target error with meshoptimizer. (Python)
- [interactor-blender-multi-user](https://github.com/V-Sekai-fire/interactor-blender-multi-user) - The Blender multi-user collaborative editing addon, carried from slumber/multi-user. (Python)
- [interactor-cli](https://github.com/V-Sekai-fire/interactor-cli) - weftfit driving adapter: Elixir CLI + Fine NIF, packaged as a self-contained Burrito binary. (Elixir)
- [interactor-dress-designer-maskscore](https://github.com/V-Sekai-fire/interactor-dress-designer-maskscore) - Scripts that sample garments from a second-hand fashion dataset and drive a pattern-drafting garment simulator to rebuild them as USD. (Python)
- [interactor-libeigen-eigen](https://github.com/V-Sekai-fire/interactor-libeigen-eigen) - Mirror of libeigen/eigen@21e4582d (gitlab source), pinned for trellis2-upstream. (C++)
- [interactor-material-graph-maskscore](https://github.com/V-Sekai-fire/interactor-material-graph-maskscore) - MaskScore dataset automation. (Python)
- [interactor-material-sampler-maskscore](https://github.com/V-Sekai-fire/interactor-material-sampler-maskscore) - MaskScore dataset automation. (Python)
- [interactor-mesh-transformer](https://github.com/V-Sekai-fire/interactor-mesh-transformer) - Mesh generation with attention, in PyTorch. (Python)
- [interactor-obj](https://github.com/V-Sekai-fire/interactor-obj) - weftfit adapter: Wavefront OBJ mesh source+sink. (C++)
- [interactor-p3sam-mesh-segmentation](https://github.com/V-Sekai-fire/interactor-p3sam-mesh-segmentation) - Model image for p3sam_mesh_segmentation. (Python)
- [interactor-panelspun](https://github.com/V-Sekai-fire/interactor-panelspun) - Docking panel UI on SDL3 windows and ThorVG canvases, Apache-2.0 OR MIT. (C++)
- [interactor-pixal3d-image-to-textured-mesh](https://github.com/V-Sekai-fire/interactor-pixal3d-image-to-textured-mesh) - Model image for pixal3d_image_to_textured_mesh (image to 3D, PBR). (Python)
- [interactor-retarget](https://github.com/V-Sekai-fire/interactor-retarget) - weftfit core: intersection-free garment retargeting + mesh port contracts. (C++)
- [interactor-space-starvector-8b-im2svg](https://github.com/V-Sekai-fire/interactor-space-starvector-8b-im2svg) - A model-serving container that turns a raster image into SVG markup with an image-to-SVG language model. (Python)
- [interactor-stage](https://github.com/V-Sekai-fire/interactor-stage) - weftfit adapter: OpenUSD scene-description mesh source+sink (via stage_runtime). (C++)
- [interactor-stage-runtime](https://github.com/V-Sekai-fire/interactor-stage-runtime) - A prebuilt USD scene-description runtime per platform triplet, shipped as the `stage_runtime` Mix package. (Python)
- [interactor-texture-painter-maskscore](https://github.com/V-Sekai-fire/interactor-texture-painter-maskscore) - MaskScore dataset automation. (Python)
- [interactor-tool-quadwild](https://github.com/V-Sekai-fire/interactor-tool-quadwild) - A script that retopologizes a GLB mesh into quads through prebuilt QuadWild-BiMDF binaries. (Python)
- [interactor-trellis2-ex](https://github.com/V-Sekai-fire/interactor-trellis2-ex) - Elixir ports of an image-to-3D model's vision encoder and sparse-structure flow transformer, checked against reference activations. (Elixir)
- [interactor-trellis2-image-mesh-painting](https://github.com/V-Sekai-fire/interactor-trellis2-image-mesh-painting) - Model image for trellis2_image_mesh_painting. (Python)
- [interactor-trellis2-image-to-textured-mesh](https://github.com/V-Sekai-fire/interactor-trellis2-image-to-textured-mesh) - Model image for trellis2_image_to_textured_mesh (image to 3D, PBR). (Python)
- [interactor-ufbx-to-openusd](https://github.com/V-Sekai-fire/interactor-ufbx-to-openusd) - FBX in, OpenUSD out, through ufbx. (Python)
- [interactor-viewer](https://github.com/V-Sekai-fire/interactor-viewer) - weftfit adapter (planned): mesh sink for QA visualization. (C)
- [interactor-voxhammer-image-mesh-editing](https://github.com/V-Sekai-fire/interactor-voxhammer-image-mesh-editing) - Model image for voxhammer_image_mesh_editing. (Python)
- [interactor-voxhammer-text-mesh-editing](https://github.com/V-Sekai-fire/interactor-voxhammer-text-mesh-editing) - Model image for voxhammer_text_mesh_editing. (Elixir)
- [interactor-vtracer-pixel](https://github.com/V-Sekai-fire/interactor-vtracer-pixel) - visioncortex VTracer is an open source software to convert raster images (like jpg & png) into vector graphics (svg). (Rust)
- [repository-usd-core-wheels](https://github.com/V-Sekai-fire/repository-usd-core-wheels) - OpenUSD Python wheels built for arm64 macOS (and other platforms lacking pypi coverage).
- [service-cog-sam-part-3d](https://github.com/V-Sekai-fire/service-cog-sam-part-3d) - A `cog` predictor that builds the SAMPart3D part-segmentation stack and renders a mesh's views for it. (Python)
- [service-cog-vsk-mesh-optimizer](https://github.com/V-Sekai-fire/service-cog-vsk-mesh-optimizer) - A container predictor that simplifies a binary glTF model with meshoptimizer's packer and returns the smaller file. (Python)
- [weftspun-character-taxonomy](https://github.com/V-Sekai-fire/weftspun-character-taxonomy) - RFD 0065 character taxonomy: headless-CMS JSON route, static randomizer page, MCP server. (Elixir)
- [weftspun-usd-viewer](https://github.com/V-Sekai-fire/weftspun-usd-viewer) - usd_viewer_app: static server for the RFD 0073 billboard gallery's usd-viewer WASM build, its own Fly deploy target. (JavaScript)

## Machine learning and inference

_ggml ports, model images, Elixir ML bindings and training experiments._

- [datasource-llama-dataset-01](https://github.com/V-Sekai-fire/datasource-llama-dataset-01) - Grammar-constrained generation with a local language model: GBNF grammars that make it emit Godot scene text or JSON arrays. (Python)
- [datasource-meshgpt-dataset-02](https://github.com/V-Sekai-fire/datasource-meshgpt-dataset-02) - A notebook that trains a text-conditioned mesh autoencoder and transformer on a small labelled mesh set, then generates meshes from text. (Jupyter Notebook)
- [entities-elixir-holographic-reduced-representation](https://github.com/V-Sekai-fire/entities-elixir-holographic-reduced-representation) - Holographic Reduced Representations with phase encoding, over Nx. (Elixir)
- [entities-vsk-docker-python-notebook](https://github.com/V-Sekai-fire/entities-vsk-docker-python-notebook) - A GPU notebook container, and a predictor that fine-tunes the RF-DETR detector on an uploaded dataset and returns the trained weights. (Jupyter Notebook)
- [interactor-character-concept-acclaim](https://github.com/V-Sekai-fire/interactor-character-concept-acclaim) - Generated full-body character concept illustrations with their prompts and captions, and a declarative model config for scoring them. (Python)
- [interactor-cyclegan-style-transfer](https://github.com/V-Sekai-fire/interactor-cyclegan-style-transfer) - Model image for cyclegan_style_transfer: ukiyo-e and Monet restyling of ANNY renders, BSD upstream, non-diffusion by design. (Python)
- [interactor-editscore-lora-qwen3vl-4b](https://github.com/V-Sekai-fire/interactor-editscore-lora-qwen3vl-4b) - EditScore reward-model role on Qwen3-VL-4B: MLX for Mac mini; LoRA training path for 3090. (Python)
- [interactor-elixir-forge](https://github.com/V-Sekai-fire/interactor-elixir-forge) - Elixir tools for machine-learning inference and mesh work: an image-generation pipeline app and single-file scripts. (Elixir)
- [interactor-elixir-turboquant-llm](https://github.com/V-Sekai-fire/interactor-elixir-turboquant-llm) - Elixir bindings for a vendored ggml language-model runtime with a quantised KV cache, as native functions. (C++)
- [interactor-executorch-tiling](https://github.com/V-Sekai-fire/interactor-executorch-tiling) - A demo that exports one dynamic-shape model to an on-device inference runtime and runs it on the CPU over image tiles of varying size. (Python)
- [interactor-fire-architext-v2](https://github.com/V-Sekai-fire/interactor-fire-architext-v2) (Elixir)
- [interactor-game-tag-starvote-ballots](https://github.com/V-Sekai-fire/interactor-game-tag-starvote-ballots) - Picks a set of standout games from a market-research table by a score-voting election, with a sales metric as each ballot's score. (Python)
- [interactor-hailo-ugen300](https://github.com/V-Sekai-fire/interactor-hailo-ugen300) - UGen300 (Hailo-10H) apparatus: HailoRT shim, DFC probes, rung ladders. (Python)
- [interactor-minicpm-vision](https://github.com/V-Sekai-fire/interactor-minicpm-vision) - An Elixir service that runs a vision-language model through an embedded Python runtime to describe images and video. (Elixir)
- [interactor-ml-fire-juan-mosaic](https://github.com/V-Sekai-fire/interactor-ml-fire-juan-mosaic) - A command-line sample that restyles a PNG with a mosaic style-transfer network in ONNX format, on the GPU or the CPU. (C++)
- [interactor-multimodal-semantic-ids](https://github.com/V-Sekai-fire/interactor-multimodal-semantic-ids) - Multimodal FOSS encoders + concat-vector ResidualFSQ semantic IDs (text/image/mesh/audio/body-phenotype); successor to vsk-session-item-recommendation-01. (Python)
- [interactor-multiplayer-fabric-llm](https://github.com/V-Sekai-fire/interactor-multiplayer-fabric-llm) - An Elixir NIF that loads a GGUF language model and runs chat completion in process, streamed or whole. (Elixir)
- [interactor-nx-ggml](https://github.com/V-Sekai-fire/interactor-nx-ggml) - A JIT-compiled Nx backend that lowers `Nx.Defn` expression graphs into ggml compute graphs on the CPU or Vulkan. (Elixir)
- [interactor-python-notebooks](https://github.com/V-Sekai-fire/interactor-python-notebooks) - Scratch notebooks: a SQLite example, a schema and planner sketch for a social VR platform, and a table of character polygon counts. (Jupyter Notebook)
- [interactor-residual-fsq-recommender](https://github.com/V-Sekai-fire/interactor-residual-fsq-recommender) - Holographic (HRR phase-vector) session memory over concat-vector ResidualFSQ semantic IDs; zero-shot next-item recall in Elixir, certified via… (Elixir)
- [interactor-rf-detr-ggml](https://github.com/V-Sekai-fire/interactor-rf-detr-ggml) - A C++ and ggml port of the RF-DETR real-time detection transformer, for object detection, instance segmentation and keypoints. (Python)
- [interactor-see-through-ggml](https://github.com/V-Sekai-fire/interactor-see-through-ggml) - Single-image layer decomposition for anime characters, over ggml, answering on the weft command bus. (C)
- [interactor-see-through-python](https://github.com/V-Sekai-fire/interactor-see-through-python) - The reference half of the see-through A/B: the PyTorch pipeline on iceoryx2's Python binding, sharing nothing with the C++ half but the wire between them. (Python)
- [interactor-shader-gpt](https://github.com/V-Sekai-fire/interactor-shader-gpt) - Run popular small language models in Unity with pixel shaders. (C#)
- [interactor-shadergpt](https://github.com/V-Sekai-fire/interactor-shadergpt) - Mirror of lox9973's ShaderGPT. (C#)
- [interactor-tool-logoscale](https://github.com/V-Sekai-fire/interactor-tool-logoscale) - Image upscaling work with ESRGAN.
- [interactor-tool-rotten-tomatoes-01](https://github.com/V-Sekai-fire/interactor-tool-rotten-tomatoes-01) - A declarative training experiment that predicts whether a critic's review recommends a film, from the review text and film metadata. (Python)
- [interactor-tosa-converter-for-tflite](https://github.com/V-Sekai-fire/interactor-tosa-converter-for-tflite) (Python)
- [service-cog-template](https://github.com/V-Sekai-fire/service-cog-template) - A blank model-serving template with empty prediction and training entry points, packaged for the `cog` container tool. (Python)
- [service-cog-yolo-nas-pose](https://github.com/V-Sekai-fire/service-cog-yolo-nas-pose) - A model container that serves a single-pass person detection and pose estimation network. (Python)
- [service-language-model](https://github.com/V-Sekai-fire/service-language-model) (C++)
- [service-see-through](https://github.com/V-Sekai-fire/service-see-through) - A service: the see-through transport layer and interactor pair packed into a release, and the dev -> beta -> rc -> release ladder that gates a promotion… (Python)

## MCP servers and agent tools

_Model Context Protocol servers and tools that let agents drive engines, editors and solvers._

- [interactor-touch-companion](https://github.com/V-Sekai-fire/interactor-touch-companion) - A game's captured window and touch key buttons in one window, so an agent that can only click can play keyboard games. (C++)
- [interactor-xr-pilot](https://github.com/V-Sekai-fire/interactor-xr-pilot) - Lets an AI agent see and drive OpenXR apps. (C++)
- [transport-blender-mcp](https://github.com/V-Sekai-fire/transport-blender-mcp) - A Blender addon and Model Context Protocol server that let an agent build and edit 3D scenes over a local socket. (Python)
- [transport-easy-diffusion-mcp](https://github.com/V-Sekai-fire/transport-easy-diffusion-mcp) - MCP Server for Easy Diffusion. (Elixir)
- [transport-godot-mcp](https://github.com/V-Sekai-fire/transport-godot-mcp) - In-editor MCP server addon for Godot. (GDScript)
- [transport-mcp-autogluon](https://github.com/V-Sekai-fire/transport-mcp-autogluon) - An Elixir Model Context Protocol server that exposes an automated machine learning library as tools for training, prediction and evaluation. (Elixir)
- [transport-minizinc-mcp](https://github.com/V-Sekai-fire/transport-minizinc-mcp) - A Model Context Protocol server that validates and solves constraint models written in the MiniZinc modelling language. (Elixir)
- [transport-pcg-mcp](https://github.com/V-Sekai-fire/transport-pcg-mcp) - A Model Context Protocol server in Elixir that grows tile levels by wave function collapse and solves constraint models. (Elixir)
- [transport-rf-detr-mcp](https://github.com/V-Sekai-fire/transport-rf-detr-mcp) - MCP server wrapping RF-DETR for pose keypoints, instance segmentation, and detection QA of generated character art. (Python)
- [transport-sympy-mcp](https://github.com/V-Sekai-fire/transport-sympy-mcp) - An Elixir-based MCP (Model Context Protocol) server that provides symbolic mathematics capabilities using SymPy. (Elixir)

## Video, audio and broadcast

_CineForm recording, AV1/FLAC muxing and the desk's broadcast setup._

- [entities-core-streaming-steam-deck](https://github.com/V-Sekai-fire/entities-core-streaming-steam-deck) - Setup notes for streaming a handheld gaming PC's screen to the desktop through a capture card, for work and study sessions.
- [entities-parsec](https://github.com/V-Sekai-fire/entities-parsec) - A Windows 11 tray app that moves any window into the desktop wallpaper layer, behind the icons, so a full-screen remote-desktop session plays as the wallpaper. (C#)
- [interactor-av1mkv](https://github.com/V-Sekai-fire/interactor-av1mkv) - CineForm recordings to AV1 and FLAC in a WebM or an MKV. (C++)
- [interactor-cineform](https://github.com/V-Sekai-fire/interactor-cineform) - CineForm encoder as a weft-bus interactor: an encode command in, a CineForm Matroska out, a progress sample per frame over iceoryx2. (C++)
- [interactor-deskpin](https://github.com/V-Sekai-fire/interactor-deskpin) - Send any window to the Windows desktop wallpaper layer, behind the icons. (Elixir)
- [service-cineform](https://github.com/V-Sekai-fire/service-cineform) - The CineForm encode service: stands up the iceoryx2 bus and interactor-cineform on one host, in a runtime directory the service owns. (Python)
- [transport-cineform-tui](https://github.com/V-Sekai-fire/transport-cineform-tui) - The command line as a transport layer for interactor-cineform: an ffmpeg-style status line driven by iceoryx2 progress samples. (C++)
- [transport-obs-broadcast](https://github.com/V-Sekai-fire/transport-obs-broadcast) - The desk's OBS broadcast: its scene collection and the obs-websocket scripts that lay out, switch and repair it. (Python)

## Infrastructure, secrets and delivery

_Secrets, storage, builds, launchers and observability._

- [datasource-duckdb](https://github.com/V-Sekai-fire/datasource-duckdb) - Lean 4 + DuckDB FFI for loading Parquet/CSV files — sim-first dataset I/O. (Shell)
- [datasource-launcher-chunks](https://github.com/V-Sekai-fire/datasource-launcher-chunks) - Content-addressed chunk store for central-launcher payload updates.
- [datasource-versitygw-local](https://github.com/V-Sekai-fire/datasource-versitygw-local) - An Elixir library that runs a local object-storage gateway over a plain directory and hands back the endpoint config for a storage client. (Elixir)
- [entities-fuschia-tin-giraffe](https://github.com/V-Sekai-fire/entities-fuschia-tin-giraffe) - OSXCross: a macOS cross toolchain for Linux, FreeBSD, OpenBSD and Android. (C++)
- [entities-vsk-database-roundtable](https://github.com/V-Sekai-fire/entities-vsk-database-roundtable) - Side-by-side benchmark rounds that run one cloud-serving workload against several databases in CI.
- [interactor-ecto-bench-tpcc](https://github.com/V-Sekai-fire/interactor-ecto-bench-tpcc) - Generic TPC-C-style benchmark harness for any Ecto adapter. (Elixir)
- [interactor-flow-hello-world](https://github.com/V-Sekai-fire/interactor-flow-hello-world) - A hello-world webhook event source and a sensor that starts a container workflow when the webhook receives a POST.
- [interactor-parqview](https://github.com/V-Sekai-fire/interactor-parqview) - Local web viewer for Parquet directories, with embedded-image support. (Elixir)
- [interactor-popcorn-test](https://github.com/V-Sekai-fire/interactor-popcorn-test) - A minimal Elixir application compiled to WebAssembly with popcorn, to run on AtomVM in a browser. (Elixir)
- [interactor-sqlar-cas](https://github.com/V-Sekai-fire/interactor-sqlar-cas) - Content-addressable chunk store using casync wire format inside SQLite. (Python)
- [interactor-test-appium-windows-hello-world](https://github.com/V-Sekai-fire/interactor-test-appium-windows-hello-world) - A WebDriver script that clicks through a sum in the desktop calculator app and reads the result back from its accessibility tree. (JavaScript)
- [interactor-tool-game-start](https://github.com/V-Sekai-fire/interactor-tool-game-start) - A design note for a game starter with no graphical interface that downloads the graphical downloader over the casync protocol.
- [service-ayon-setup](https://github.com/V-Sekai-fire/service-ayon-setup) - A task schedule, kept as SQLite databases, for standing up a production-tracking server and connecting artist workstations to it.
- [service-bao-sqlite-fdb](https://github.com/V-Sekai-fire/service-bao-sqlite-fdb) - OpenBao secrets engine that runs precanned SQL against fabric-store SQLite databases and returns rows through Bao's KV interface. (Go)
- [service-crossbuild-fedora](https://github.com/V-Sekai-fire/service-crossbuild-fedora) - Fedora amd64 container that cross-builds mac/windows/linux; osxcross packaged as dev-latest release asset. (Shell)
- [service-dokku-cockroachdb](https://github.com/V-Sekai-fire/service-dokku-cockroachdb) - A cockroachdb plugin for dokku. (Shell)
- [service-game-observability](https://github.com/V-Sekai-fire/service-game-observability) - Observability stack: VictoriaMetrics + VictoriaLogs + Tempo + OTEL Collector on Fly.io.
- [service-godot-build](https://github.com/V-Sekai-fire/service-godot-build) - Runs a Godot repository's Windows build matrix locally, reading it from .github/workflows. (Elixir)
- [service-hex-ops](https://github.com/V-Sekai-fire/service-hex-ops) - Manual GitHub Actions ops for Hex package publish/retire/unretire across the taskweft org.
- [service-openbao](https://github.com/V-Sekai-fire/service-openbao) - OpenBao on Fly.io with the restored FoundationDB storage backend. (Shell)
- [service-sqlar-cas](https://github.com/V-Sekai-fire/service-sqlar-cas) - Elixir service serving sqlar-cas (age v1.1.0 crypto in a SQLite/S3 wire, ReBAC via Bao). (Elixir)
- [transport-central-launcher](https://github.com/V-Sekai-fire/transport-central-launcher) - Install, launch and update the workspace runtime as one binary per platform. (Elixir)
- [transport-oauth-mcp-bridge](https://github.com/V-Sekai-fire/transport-oauth-mcp-bridge) - A generic OAuth 2.1-to-MCP authorization bridge (GitHub login), extracted from taskweft/deploy. (Elixir)
- [transport-shepherd](https://github.com/V-Sekai-fire/transport-shepherd) - Elixir Burrito TUI that reduces weftspun's Bao agent enrol / rotate / migrate / revoke ceremony to one command per operation. (Elixir)
- [transport-usbip-frame](https://github.com/V-Sekai-fire/transport-usbip-frame) - Userspace USB/IP server over libusb; traffic logged as zstd Parquet. (Python)

## Worlds, scenes, stories and art

_Maps, scenes, interactive fiction, galleries and concept work._

- [contract-tutorial-shapes-rhino3d-01](https://github.com/V-Sekai-fire/contract-tutorial-shapes-rhino3d-01) - Makes shapes with Rhino3D and grasshopper.
- [datasource-concept-fire-girl](https://github.com/V-Sekai-fire/datasource-concept-fire-girl) - Concept images of an avatar character in an orange dress, generated by a text-to-image diffusion model and kept with their prompts.
- [datasource-gallery-fire-selfies-01](https://github.com/V-Sekai-fire/datasource-gallery-fire-selfies-01) - Fire's Photo Gallery (part of split series). (CSS)
- [datasource-gallery-fire-selfies-02](https://github.com/V-Sekai-fire/datasource-gallery-fire-selfies-02) - Fire's Photo Gallery (part of split series). (CSS)
- [datasource-gallery-fire-selfies-03](https://github.com/V-Sekai-fire/datasource-gallery-fire-selfies-03) - Fire's Photo Gallery (part of split series). (CSS)
- [datasource-gallery-fire-selfies-04](https://github.com/V-Sekai-fire/datasource-gallery-fire-selfies-04) - Fire's Photo Gallery (part of split series). (CSS)
- [datasource-gallery-fire-selfies-05](https://github.com/V-Sekai-fire/datasource-gallery-fire-selfies-05) - Fire's Photo Gallery (part of split series). (CSS)
- [entities-bullet-game-jam](https://github.com/V-Sekai-fire/entities-bullet-game-jam) - Branching-story scripts in `.ink` format and a storyboard, written for a game jam. (Ink)
- [entities-env-cafe](https://github.com/V-Sekai-fire/entities-env-cafe) (GDScript)
- [entities-fire-work](https://github.com/V-Sekai-fire/entities-fire-work) - A static web gallery of K. S. Ernest (iFire) Lee's work. (CSS)
- [entities-ink-bullet-train](https://github.com/V-Sekai-fire/entities-ink-bullet-train) - A dice-driven interactive story about a sleeper-train journey, written as an ink script, with a storyboard of its opening. (Ink)
- [entities-sakuragaoka-station](https://github.com/V-Sekai-fire/entities-sakuragaoka-station) - Sakuragaoka Station, the procedural sakura station town, ported to Godot as an addon. (GDScript)
- [entities-scene-morning-in-a-cafe](https://github.com/V-Sekai-fire/entities-scene-morning-in-a-cafe) - A cafe scene for the social VR world, as an engine project with the avatar and map add-ons it loads. (GDShader)
- [entities-scene-room-1107](https://github.com/V-Sekai-fire/entities-scene-room-1107) - A living-room map scene in an engine project, with the addons that define it as a V-Sekai map and upload it. (GDShader)
- [entities-scene-Video-and-Gltf](https://github.com/V-Sekai-fire/entities-scene-Video-and-Gltf) - A social VR world project, started from the platform's default world scene, meant for video and glTF content. (C#)
- [entities-starforged](https://github.com/V-Sekai-fire/entities-starforged) - Game module for entities-godot: RFD 1175 Starforged decision-point VN + video capture head.
- [entities-vsk-character-overview](https://github.com/V-Sekai-fire/entities-vsk-character-overview) - An engine project that lays out a character overview sheet around a `.vrm` avatar. (GDShader)
- [entities-vsk-FONT-experiments](https://github.com/V-Sekai-fire/entities-vsk-FONT-experiments) - A few openly licensed font families with their engine import settings, kept for typeface experiments.
- [entities-vsk-hut](https://github.com/V-Sekai-fire/entities-vsk-hut) (GDScript)
- [entities-vsk-idea-prompts](https://github.com/V-Sekai-fire/entities-vsk-idea-prompts) - A text prompt for a character concept image, kept with the description a language model wrote from it.
- [entities-vsk-sleepy-fox-cafe](https://github.com/V-Sekai-fire/entities-vsk-sleepy-fox-cafe) - A cafe environment for social VR, kept as one `.blend` scene file.
- [entities-vsk-spark](https://github.com/V-Sekai-fire/entities-vsk-spark)
- [entities-vsk-visual-novel-01](https://github.com/V-Sekai-fire/entities-vsk-visual-novel-01) - A short branching noir story written as an interactive-fiction script, with the prompts and drafts that led to it. (Ink)
- [entities-world-magical-college-town](https://github.com/V-Sekai-fire/entities-world-magical-college-town)
- [interactor-ml-image-generation](https://github.com/V-Sekai-fire/interactor-ml-image-generation) - Generated concept-art character sheets, one folder per character idea, with a few hand-made concept files beside them.
- [interactor-tool-inspirator](https://github.com/V-Sekai-fire/interactor-tool-inspirator)
- [interactor-udon-flat](https://github.com/V-Sekai-fire/interactor-udon-flat) - UdonFlat does the opposite of UdonSharp. (C#)

## Datasets and test corpora

_Training sets, evaluation sets and importer fixtures._

- [datasource-anny-render-corpus](https://github.com/V-Sekai-fire/datasource-anny-render-corpus) - The ANNY render corpus pipeline: ETNF schema, identity sampling, the audits that gate a render run, and a Mitsuba render pass pinned by pixi. (Python)
- [datasource-anny-soma-corpus](https://github.com/V-Sekai-fire/datasource-anny-soma-corpus) - ANNY-SOMA keypoint corpus. (Python)
- [datasource-coco-ood-eval](https://github.com/V-Sekai-fire/datasource-coco-ood-eval) - COCO-OOD stylized val2017 evaluation sets, filtered to the 523 licence-clean images, as ETNF parquet. (Python)
- [datasource-dataset-architext-v1](https://github.com/V-Sekai-fire/datasource-dataset-architext-v1) (Roff)
- [datasource-dataset-unslop-good](https://github.com/V-Sekai-fire/datasource-dataset-unslop-good)
- [datasource-mat-material-x-sample](https://github.com/V-Sekai-fire/datasource-mat-material-x-sample) - An engine project that carries the standard `.mtlx` material libraries and sample assets for trying `.mtlx` materials in a scene. (GLSL)
- [datasource-mesh-human-base-mesh-1-1](https://github.com/V-Sekai-fire/datasource-mesh-human-base-mesh-1-1) - Human Base Meshes v1.1 by Blender Studio and community contributions.
- [datasource-rf-detr-detection-data](https://github.com/V-Sekai-fire/datasource-rf-detr-detection-data) - Train/test split for RF-DETR object-detection finetuning (Roboflow clothing dataset, CC BY 4.0). (Python)
- [datasource-rf-detr-keypoint-data](https://github.com/V-Sekai-fire/datasource-rf-detr-keypoint-data) - Train/test split for RF-DETR keypoint-detection finetuning (COCO val2017, CC BY 4.0). (Python)
- [datasource-rf-detr-segmentation-data](https://github.com/V-Sekai-fire/datasource-rf-detr-segmentation-data) - Train/test split for RF-DETR instance-segmentation finetuning (Roboflow clothing dataset, CC BY 4.0). (Python)
- [interactor-test-fbx](https://github.com/V-Sekai-fire/interactor-test-fbx) - Third-party `.fbx` models and animations, each with a JSON record of its title, author, source and licence, for testing scene importers.
- [interactor-test-fbx-arm-pulser](https://github.com/V-Sekai-fire/interactor-test-fbx-arm-pulser) - An animated arm model in FBX with reference OBJ geometry at sampled frames, for import tests.
- [interactor-test-fbx-github](https://github.com/V-Sekai-fire/interactor-test-fbx-github) - A model-import test fixture: a telescope model from a public rendering sample set, stored as a reference OBJ with its materials.
- [interactor-test-fbx-kenney](https://github.com/V-Sekai-fire/interactor-test-fbx-kenney) - Animated characters and model kits in FBX, each with reference OBJ geometry and a record of its source and licence, for import tests.
- [interactor-test-fbx-mocap-market](https://github.com/V-Sekai-fire/interactor-test-fbx-mocap-market) - Motion-capture clips in FBX, each with reference OBJ frames and a record of its source and licence, for import tests.
- [interactor-test-fbx-opengameart](https://github.com/V-Sekai-fire/interactor-test-fbx-opengameart) - Public-domain test models in `.fbx` form from a free game-art archive, each with `.obj` snapshots and a record of its source.
- [interactor-test-fbx-polyhaven](https://github.com/V-Sekai-fire/interactor-test-fbx-polyhaven) - Public-domain test models in FBX and OBJ form, each with a record of its title, author, source and licence, for importer tests.
- [interactor-test-fbx-quaternius](https://github.com/V-Sekai-fire/interactor-test-fbx-quaternius) - Low-poly character and prop packs in FBX, each with reference OBJ geometry and a record of its source and licence, for import tests.
- [interactor-test-fbx-rug](https://github.com/V-Sekai-fire/interactor-test-fbx-rug) - A test fixture of one rug model with dense strand geometry, exported to binary FBX twice, for checking an FBX importer.
- [interactor-test-fbx-sketchfab-01](https://github.com/V-Sekai-fire/interactor-test-fbx-sketchfab-01) - Third-party `.fbx` models, one directory per author, each with a JSON record of its author, source and licence, for testing scene importers.
- [interactor-test-fbx-sketchfab-03](https://github.com/V-Sekai-fire/interactor-test-fbx-sketchfab-03) - Community 3D models grouped by author, each with a record of its source and licence, as fixtures for an FBX importer test.
- [interactor-test-fbx-sketchfab-04](https://github.com/V-Sekai-fire/interactor-test-fbx-sketchfab-04) - A test corpus of third-party FBX models with reference meshes, for checking an FBX importer against known output.
- [interactor-test-fbx-thebasemesh](https://github.com/V-Sekai-fire/interactor-test-fbx-thebasemesh) - A test corpus of public-domain FBX models with reference meshes, for checking an FBX importer against known output.

## Forks we maintain

_Upstream projects that V-Sekai-fire mirrors, pins or patches. The link goes to the fork; the parent is in brackets._

<details>
<summary>219 forks</summary>

- [3dgs-ply2gltf](https://github.com/V-Sekai-fire/3dgs-ply2gltf) [[NorbertNopper-Huawei/3dgs_ply2gltf](https://github.com/NorbertNopper-Huawei/3dgs_ply2gltf)] - 3DGS PLY to glTF converter.
- [app-ayon-backend](https://github.com/V-Sekai-fire/app-ayon-backend) [[digitalocean/sample-dockerfile](https://github.com/digitalocean/sample-dockerfile)] - The Docker-based deployment for the Ayon production-tracking server.
- [Baballs](https://github.com/V-Sekai-fire/Baballs) [[Project-Babble/Baballs](https://github.com/Project-Babble/Baballs)] - Enhanced Blink And Look Learning System.
- [babble-docs](https://github.com/V-Sekai-fire/babble-docs) [[Project-Babble/BabbleDocs](https://github.com/Project-Babble/BabbleDocs)] - Documentation for Project Babble.
- [babble-hardware](https://github.com/V-Sekai-fire/babble-hardware) [[Project-Babble/BabbleHardware](https://github.com/Project-Babble/BabbleHardware)] - Hardware files for Project Babble.
- [BFI_VRCFT_Module](https://github.com/V-Sekai-fire/BFI_VRCFT_Module) [[HashEdits/BFI_VRCFT_Module](https://github.com/HashEdits/BFI_VRCFT_Module)] - A VRCFT module that let's you control VRCFT avatars using BFI expression actions controlled by your brain 🧠.
- [blueprint-self-hosted](https://github.com/V-Sekai-fire/blueprint-self-hosted) [[blueprintue/blueprintue-self-hosted-edition](https://github.com/blueprintue/blueprintue-self-hosted-edition)]
- [breeze](https://github.com/V-Sekai-fire/breeze) [[Gazler/breeze](https://github.com/Gazler/breeze)] - An experimental TUI library based on LiveView without using 3rd party NIFs.
- [build-containers](https://github.com/V-Sekai-fire/build-containers) [[godotengine/build-containers](https://github.com/godotengine/build-containers)] - Godot engine build containers.
- [bumblebee](https://github.com/V-Sekai-fire/bumblebee) [[elixir-nx/bumblebee](https://github.com/elixir-nx/bumblebee)] - Vendored fork of Bumblebee (Elixir/Nx).
- [CCTV](https://github.com/V-Sekai-fire/CCTV) [[C2SP/CCTV](https://github.com/C2SP/CCTV)] - Community Cryptography Test Vectors.
- [cineform-sdk](https://github.com/V-Sekai-fire/cineform-sdk) [[gopro/cineform-sdk](https://github.com/gopro/cineform-sdk)] - Vendored fork of the CineForm video codec SDK (C).
- [cloth-fit](https://github.com/V-Sekai-fire/cloth-fit) [[Huangzizhou/cloth-fit](https://github.com/Huangzizhou/cloth-fit)]
- [CoACD](https://github.com/V-Sekai-fire/CoACD) [[SarahWeiii/CoACD](https://github.com/SarahWeiii/CoACD)] - Approximate Convex Decomposition for 3D Meshes with Collision-Aware Concavity and Tree Search [SIGGRAPH2022].
- [cog-grounding-dino](https://github.com/V-Sekai-fire/cog-grounding-dino) [[replicate/cog-grounding-dino](https://github.com/replicate/cog-grounding-dino)] - Cog wrapper for Grounding DINO.
- [cog-instruct-code-generation](https://github.com/V-Sekai-fire/cog-instruct-code-generation) [[lucataco/cog-instruct-glaive](https://github.com/lucataco/cog-instruct-glaive)] - Attempt at cog wrapper for sahil2801/replit-code-instruct-glaive.
- [cog-mpt-7b-storywriter-65k](https://github.com/V-Sekai-fire/cog-mpt-7b-storywriter-65k) [[replicate/cog-mpt-7b-storywriter-65k](https://github.com/replicate/cog-mpt-7b-storywriter-65k)] - A cog implementation of MosaicML's MPT-7B-StoryWriter-65k+ Large Language Model.
- [cog-paligemma-3b-pt-224](https://github.com/V-Sekai-fire/cog-paligemma-3b-pt-224) [[lucataco/cog-paligemma-3b-pt-224](https://github.com/lucataco/cog-paligemma-3b-pt-224)] - Cog wrapper for google/paligemma-3b-pt-224.
- [cog-vsk-flux](https://github.com/V-Sekai-fire/cog-vsk-flux) [[replicate/cog-flux](https://github.com/replicate/cog-flux)] - Cog inference for flux models.
- [cog-vsk-trellis](https://github.com/V-Sekai-fire/cog-vsk-trellis) [[firtoz/TRELLIS](https://github.com/firtoz/TRELLIS)] - Fork of the repo for paper "Structured 3D Latents for Scalable and Versatile 3D Generation".
- [ComfyUI-TRELLIS2](https://github.com/V-Sekai-fire/ComfyUI-TRELLIS2) [[PozzettiAndrea/ComfyUI-TRELLIS2](https://github.com/PozzettiAndrea/ComfyUI-TRELLIS2)] - ComfyUI wrapper for Trellis 2.
- [ComfyUI-Trellis2-visualbruno](https://github.com/V-Sekai-fire/ComfyUI-Trellis2-visualbruno) [[visualbruno/ComfyUI-Trellis2](https://github.com/visualbruno/ComfyUI-Trellis2)] - ComfyUI Wrapper for Microsoft Trellis.2 - Native and Compact Structured Latents for 3D Generation.
- [ConTesse](https://github.com/V-Sekai-fire/ConTesse) [[squidrice21/ConTesse](https://github.com/squidrice21/ConTesse)] - Source code for the paper "ConTesse: Accurate Occluding Contours for Subdivision Surfaces".
- [CSGTerrain](https://github.com/V-Sekai-fire/CSGTerrain) [[SpockBauru/CSG_Terrain](https://github.com/SpockBauru/CSG_Terrain)] - Godot terrain system made with CSG nodes for fast prototyping.
- [cubvh](https://github.com/V-Sekai-fire/cubvh) [[JeffreyXiang/cubvh](https://github.com/JeffreyXiang/cubvh)] - Mesh tools.
- [CuMesh](https://github.com/V-Sekai-fire/CuMesh) [[JeffreyXiang/CuMesh](https://github.com/JeffreyXiang/CuMesh)] - Cuda mesh utils.
- [dag_amendment](https://github.com/V-Sekai-fire/dag_amendment) [[eliemichel/DagAmendment](https://github.com/eliemichel/DagAmendment)] - DAG Amendment for inverse control of parametric shapes, the official Blender implementation.
- [datasource-foundationdb](https://github.com/V-Sekai-fire/datasource-foundationdb) [[V-Sekai-archive/datasource-foundationdb](https://github.com/V-Sekai-archive/datasource-foundationdb)] - Vendored fork of FoundationDB (C++).
- [datasource-store](https://github.com/V-Sekai-fire/datasource-store) [[V-Sekai-archive/datasource-store](https://github.com/V-Sekai-archive/datasource-store)] - SQLite runs in a native process with a custom VFS with no local file.
- [desync](https://github.com/V-Sekai-fire/desync) [[folbricht/desync](https://github.com/folbricht/desync)] - Alternative casync implementation.
- [dinov2](https://github.com/V-Sekai-fire/dinov2) [[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)] - PyTorch code and models for the DINOv2 self-supervised learning method.
- [dokku-objectstore-seaweedfs](https://github.com/V-Sekai-fire/dokku-objectstore-seaweedfs) [[kenob/dokku-objectstore](https://github.com/kenob/dokku-objectstore)] - S3-compatible object storage backed by minio.
- [drawable-textures-demo](https://github.com/V-Sekai-fire/drawable-textures-demo) [[BastiaanOlij/drawable-textures-demo](https://github.com/BastiaanOlij/drawable-textures-demo)] - Demo/test project to try out Colins drawable textures, mini ORM 3D texture painter.
- [eflatbuffers](https://github.com/V-Sekai-fire/eflatbuffers) [[wooga/eflatbuffers](https://github.com/wooga/eflatbuffers)] - Elixir/Erlang flatbuffers implementation.
- [egit](https://github.com/V-Sekai-fire/egit) [[saleyn/egit](https://github.com/saleyn/egit)] - Erlang native interface to git.
- [entities-libgodot](https://github.com/V-Sekai-fire/entities-libgodot) [[migeran/godot](https://github.com/migeran/godot)] - Godot Engine – Multi-platform 2D and 3D game engine.
- [entities-libgodot-cpp](https://github.com/V-Sekai-fire/entities-libgodot-cpp) [[migeran/godot-cpp](https://github.com/migeran/godot-cpp)] - C++ bindings for the Godot script API.
- [exhort](https://github.com/V-Sekai-fire/exhort) [[elixir-or-tools/exhort](https://github.com/elixir-or-tools/exhort)] - Experimental Elixir interface to Google's OR Tools.
- [fabric-ardy](https://github.com/V-Sekai-fire/fabric-ardy) [[nv-tlabs/ardy](https://github.com/nv-tlabs/ardy)] - Fork of the ARDY reference implementation (Python/PyTorch).
- [fabric-locomotion-generator](https://github.com/V-Sekai-fire/fabric-locomotion-generator) [[MasterYip/KimodoLocoMoGen](https://github.com/MasterYip/KimodoLocoMoGen)] - Fork of a Kimodo-based fine-grained locomotion generator (Python/PyTorch).
- [fabric-motion-diffusion](https://github.com/V-Sekai-fire/fabric-motion-diffusion) [[GuyTevet/motion-diffusion-model](https://github.com/GuyTevet/motion-diffusion-model)] - Fork of the Motion Diffusion Model reference (Python/PyTorch).
- [fabric-wholebody-control](https://github.com/V-Sekai-fire/fabric-wholebody-control) [[NVlabs/GR00T-WholeBodyControl](https://github.com/NVlabs/GR00T-WholeBodyControl)] - Fork of a decoupled whole-body-control humanoid controller stack (Python/PyTorch).
- [fire.poly-green-coords](https://github.com/V-Sekai-fire/fire.poly-green-coords) [[eliemichel/PolyGreenCoords](https://github.com/eliemichel/PolyGreenCoords)] - Public page of "Polynomial 2D Green Coordinates for Polygonal Cages"(Siggraph 2023).
- [flac](https://github.com/V-Sekai-fire/flac) [[xiph/flac](https://github.com/xiph/flac)] - Free Lossless Audio Codec.
- [FlexGEMM](https://github.com/V-Sekai-fire/FlexGEMM) [[JeffreyXiang/FlexGEMM](https://github.com/JeffreyXiang/FlexGEMM)] - A Cross-Platform Backend for High-Performance Sparse Convolutions.
- [FTXUI](https://github.com/V-Sekai-fire/FTXUI) [[ArthurSonzogni/FTXUI](https://github.com/ArthurSonzogni/FTXUI)] - Vendored fork of FTXUI (C++).
- [gaia](https://github.com/V-Sekai-fire/gaia) [[AnkaChan/Gaia](https://github.com/AnkaChan/Gaia)] - Gaia Physics Engine.
- [ganimator](https://github.com/V-Sekai-fire/ganimator) [[PeizhuoLi/ganimator](https://github.com/PeizhuoLi/ganimator)] - A motion generation model learned from a single example [SIGGRAPH 2022].
- [gd-curl](https://github.com/V-Sekai-fire/gd-curl) [[Faless/gd-curl](https://github.com/Faless/gd-curl)] - A Godot HTTPClient-compatible implementation using libcurl.
- [gdextension-to-module](https://github.com/V-Sekai-fire/gdextension-to-module) [[appsinacup/documentation_gdextension_to_module](https://github.com/appsinacup/documentation_gdextension_to_module)] - Port your GDExtension addon to modules with minimal changes.
- [ggml](https://github.com/V-Sekai-fire/ggml) [[PABannier/ggml](https://github.com/PABannier/ggml)] - Vendored fork of ggml (C/C++).
- [glTF](https://github.com/V-Sekai-fire/glTF) [[KhronosGroup/glTF](https://github.com/KhronosGroup/glTF)] - glTF – Runtime 3D Asset Delivery.
- [glTF-InteractivityGraph-AuthoringTool](https://github.com/V-Sekai-fire/glTF-InteractivityGraph-AuthoringTool) [[KhronosGroup/glTF-InteractivityGraph-AuthoringTool](https://github.com/KhronosGroup/glTF-InteractivityGraph-AuthoringTool)] - A React based DCC for viewing and authoring KHR_interactivity models.
- [gltf-toolkit](https://github.com/V-Sekai-fire/gltf-toolkit) [[microsoft/glTF-Toolkit](https://github.com/microsoft/glTF-Toolkit)] - A collection of tools for modifying and optimizing glTF assets.
- [godot-benchmarks](https://github.com/V-Sekai-fire/godot-benchmarks) [[godotengine/godot-benchmarks](https://github.com/godotengine/godot-benchmarks)] - Collection of benchmarks to test performance of different areas of Godot.
- [godot-build-scripts](https://github.com/V-Sekai-fire/godot-build-scripts) [[godotengine/godot-build-scripts](https://github.com/godotengine/godot-build-scripts)] - Build scripts used for official Godot Engine builds with https://github.com/godotengine/build-containers.
- [godot-cpp](https://github.com/V-Sekai-fire/godot-cpp) [[godotengine/godot-cpp](https://github.com/godotengine/godot-cpp)] - Vendored fork of godot-cpp (C++).
- [godot-debug-draw-3d](https://github.com/V-Sekai-fire/godot-debug-draw-3d) [[DmitriySalnikov/godot_debug_draw_3d](https://github.com/DmitriySalnikov/godot_debug_draw_3d)] - Draw 3D debug graphics and 2D overlays with this add-on.
- [godot-demo-projects](https://github.com/V-Sekai-fire/godot-demo-projects) [[godotengine/godot-demo-projects](https://github.com/godotengine/godot-demo-projects)] - Demonstration and Template Projects.
- [godot-duckdb-module](https://github.com/V-Sekai-fire/godot-duckdb-module) [[mrjsj/godot-duckdb](https://github.com/mrjsj/godot-duckdb)] - GDNative wrapper for DuckDB.
- [godot-geometry-3](https://github.com/V-Sekai-fire/godot-geometry-3) [[godot-extended-libraries/geometry3](https://github.com/godot-extended-libraries/geometry3)] - C++ math / geometry / mesh processing library.
- [godot-goap](https://github.com/V-Sekai-fire/godot-goap) [[viniciusgerevini/godot-goap](https://github.com/viniciusgerevini/godot-goap)] - Goal Oriented Action Planning example in Godot.
- [godot-imposter](https://github.com/V-Sekai-fire/godot-imposter) [[zhangjt93/godot-imposter](https://github.com/zhangjt93/godot-imposter)] - imposter plugin for godot 4.x.
- [godot-jsondiffpatch](https://github.com/V-Sekai-fire/godot-jsondiffpatch) [[benjamine/jsondiffpatch](https://github.com/benjamine/jsondiffpatch)] - Diff & patch JavaScript objects.
- [godot-libopenmpt](https://github.com/V-Sekai-fire/godot-libopenmpt) [[RevoluPowered/godot-libopenmpt](https://github.com/RevoluPowered/godot-libopenmpt)] - Returning tracker music to the top.
- [godot-minimal-theme](https://github.com/V-Sekai-fire/godot-minimal-theme) [[passivestar/godot-minimal-theme](https://github.com/passivestar/godot-minimal-theme)] - Godot minimal editor theme.
- [godot-motion-matching-demo](https://github.com/V-Sekai-fire/godot-motion-matching-demo) [[GuilhermeGSousa/godot-motion-matching-demo](https://github.com/GuilhermeGSousa/godot-motion-matching-demo)] - A third-person character controller built on the Godot Motion Matching extension.
- [godot-multiplayer-fps-tutorial](https://github.com/V-Sekai-fire/godot-multiplayer-fps-tutorial) [[devloglogan/MultiplayerFPSTutorial](https://github.com/devloglogan/MultiplayerFPSTutorial)] - A Simple Godot 4 Online Multiplayer FPS Prototype.
- [godot-okhsl-picker](https://github.com/V-Sekai-fire/godot-okhsl-picker) [[Fenreliania/OKHSL-Picker](https://github.com/Fenreliania/OKHSL-Picker)] - A simple standalone wrapper for the Godot engine's colour picker using the OKHSL colour space.
- [godot-orchestrator](https://github.com/V-Sekai-fire/godot-orchestrator) [[CraterCrash/godot-orchestrator](https://github.com/CraterCrash/godot-orchestrator)] - Orchestrator - A Visual Scripting Godot Plugin.
- [godot-pano-renderer](https://github.com/V-Sekai-fire/godot-pano-renderer) [[revpriest/godotPanoRenderer](https://github.com/revpriest/godotPanoRenderer)] - A 360-degree stereo-3d panographic image renderer for Godot.
- [godot-python-extension](https://github.com/V-Sekai-fire/godot-python-extension) [[maiself/godot-python-extension](https://github.com/maiself/godot-python-extension)] - Python language bindings for the Godot game engine.
- [godot-robust-skin-weights-transfer](https://github.com/V-Sekai-fire/godot-robust-skin-weights-transfer) [[V-Sekai/godot-robust-skin-weights-transfer](https://github.com/V-Sekai/godot-robust-skin-weights-transfer)] - Sample code for the Siggraph Asia 2023 Technical Communications paper - Robust Skin Weights Transfer via Weight Inpainting.
- [godot-sandbox](https://github.com/V-Sekai-fire/godot-sandbox) [[libriscv/godot-sandbox](https://github.com/libriscv/godot-sandbox)] - Godot Sandbox: run untrusted code safely in a RISC-V sandbox inside Godot.
- [godot-sandbox-programs](https://github.com/V-Sekai-fire/godot-sandbox-programs) [[libriscv/godot-sandbox-programs](https://github.com/libriscv/godot-sandbox-programs)] - This repository can be used as a starting point for automatically building and maintaining Sandbox programs with CMake.
- [godot-ShaderToHuman](https://github.com/V-Sekai-fire/godot-ShaderToHuman) [[celyk/godot-ShaderToHuman](https://github.com/celyk/godot-ShaderToHuman)] - A port of the ShaderToHuman library to the Godot Shading Language (GDSL).
- [godot-simple-explosion-vfx](https://github.com/V-Sekai-fire/godot-simple-explosion-vfx) [[drcd1/GodotSimpleExplosionVFX](https://github.com/drcd1/GodotSimpleExplosionVFX)] - Simple Explosion VFX in the Godot game engine.
- [godot-slicer](https://github.com/V-Sekai-fire/godot-slicer) [[cj-dimaggio/godot-slicer](https://github.com/cj-dimaggio/godot-slicer)] - A port of Ezy-Slicer for the Godot game engine updated to Godot Engine 4.3.
- [godot-slicer-example-project](https://github.com/V-Sekai-fire/godot-slicer-example-project) [[cj-dimaggio/godot-slicer-example-project](https://github.com/cj-dimaggio/godot-slicer-example-project)] - A simple Godot project demonstrating Godot-Slicer updated to Godot Engine 4.3.
- [godot-steam-audio](https://github.com/V-Sekai-fire/godot-steam-audio) [[stechyo/godot-steam-audio](https://github.com/stechyo/godot-steam-audio)] - Immersive spatial audio extension for Godot, using Valve's SteamAudio.
- [godot-summer-island](https://github.com/V-Sekai-fire/godot-summer-island) [[sunkper/Project-Summer-Island](https://github.com/sunkper/Project-Summer-Island)] - A 3D scene made with Godot, inspired by Boku no Natsuyasumi 2.
- [godot-vrm](https://github.com/V-Sekai-fire/godot-vrm) [[V-Sekai/godot-vrm](https://github.com/V-Sekai/godot-vrm)] - Importer/Exporter for VRM avatars and MToon shader.
- [godot-vrm-tailor](https://github.com/V-Sekai-fire/godot-vrm-tailor) [[V-Sekai/godot-vrm](https://github.com/V-Sekai/godot-vrm)] - Work in Progress.
- [godot_openvr](https://github.com/V-Sekai-fire/godot_openvr) [[GodotVR/godot_openvr](https://github.com/GodotVR/godot_openvr)] - GDExtension-based OpenVR (SteamVR) module.
- [godot_spatial_gardener](https://github.com/V-Sekai-fire/godot_spatial_gardener) [[dreadpon/godot_spatial_gardener](https://github.com/dreadpon/godot_spatial_gardener)] - A Godot plugin for painting plants and props on arbitrary 3D surfaces implemented in GDScript.
- [graphrag](https://github.com/V-Sekai-fire/graphrag) [[microsoft/graphrag](https://github.com/microsoft/graphrag)] - A modular graph-based Retrieval-Augmented Generation (RAG) system.
- [grounded_sam_replicate](https://github.com/V-Sekai-fire/grounded_sam_replicate) [[schananas/grounded_sam_replicate](https://github.com/schananas/grounded_sam_replicate)] - Implementation of Grounding DINO & Segment Anything, and it allows masking based on prompt, which is useful for programmed inpainting.
- [GRPO-Zero](https://github.com/V-Sekai-fire/GRPO-Zero) [[policy-gradient/GRPO-Zero](https://github.com/policy-gradient/GRPO-Zero)] - GRPO training with minimal dependencies.
- [GTPyhop](https://github.com/V-Sekai-fire/GTPyhop) [[dananau/GTPyhop](https://github.com/dananau/GTPyhop)] - A task-planning system based on Pyhop, but generalized to plan for both goals and tasks.
- [HiDream-I1-nf4](https://github.com/V-Sekai-fire/HiDream-I1-nf4) [[hykilpikonna/HiDream-I1-nf4](https://github.com/hykilpikonna/HiDream-I1-nf4)] - 4Bit Quantized Model for HiDream I1.
- [hierarchical-reasoning-model](https://github.com/V-Sekai-fire/hierarchical-reasoning-model) [[sapientinc/HRM](https://github.com/sapientinc/HRM)] - Hierarchical Reasoning Model Official Release.
- [holo-part](https://github.com/V-Sekai-fire/holo-part) [[VAST-AI-Research/HoloPart](https://github.com/VAST-AI-Research/HoloPart)] - HoloPart: Generative 3D Part Amodal Segmentation.
- [humanizer](https://github.com/V-Sekai-fire/humanizer) [[NitroxNova/humanizer](https://github.com/NitroxNova/humanizer)] - convert MPFB2 to Godot4.
- [hymotion-animation-gen-mixamo-retargeting](https://github.com/V-Sekai-fire/hymotion-animation-gen-mixamo-retargeting) [[RevoluPowered/hymotion-animation-gen-mixamo-retargeting](https://github.com/RevoluPowered/hymotion-animation-gen-mixamo-retargeting)] - A CPU Docker image for the HY-Motion API with Mixamo retargeting.
- [iceoryx2](https://github.com/V-Sekai-fire/iceoryx2) [[eclipse-iceoryx/iceoryx2](https://github.com/eclipse-iceoryx/iceoryx2)] - Vendored fork of iceoryx2 (Rust, with a C ABI).
- [idtx-flow](https://github.com/V-Sekai-fire/idtx-flow) [[Immersive-Data-Center-Management/idtx-flow](https://github.com/Immersive-Data-Center-Management/idtx-flow)] - Fork of idtx-flow (C++/GDExtension).
- [instructor_ex](https://github.com/V-Sekai-fire/instructor_ex) [[thmsmlr/instructor_ex](https://github.com/thmsmlr/instructor_ex)] - Structured outputs for LLMs in Elixir.
- [interactor-anny](https://github.com/V-Sekai-fire/interactor-anny) [[naver/anny](https://github.com/naver/anny)] - Vendored fork of the ANNY parametric body model (Python/PyTorch).
- [interactor-editscore](https://github.com/V-Sekai-fire/interactor-editscore) [[VectorSpaceLab/EditScore](https://github.com/VectorSpaceLab/EditScore)] - Vendored fork of the EditScore reward-model reference (Python/PyTorch).
- [interactor-language-ggml](https://github.com/V-Sekai-fire/interactor-language-ggml) [[PrismML-Eng/llama.cpp](https://github.com/PrismML-Eng/llama.cpp)] - LLM inference in C/C++.
- [interactor-omnigen2](https://github.com/V-Sekai-fire/interactor-omnigen2) [[VectorSpaceLab/OmniGen2](https://github.com/VectorSpaceLab/OmniGen2)] - Vendored fork of OmniGen2 (Python/PyTorch), a multimodal image editor.
- [interactor-pixal3d-image-mesh-painting](https://github.com/V-Sekai-fire/interactor-pixal3d-image-mesh-painting) [[V-Sekai-fire/interactor-pixal3d-image-to-textured-mesh](https://github.com/V-Sekai-fire/interactor-pixal3d-image-to-textured-mesh)] - Model image for pixal3d_image_to_textured_mesh (image to 3D, PBR).
- [interactor-seethrough-layerdiff](https://github.com/V-Sekai-fire/interactor-seethrough-layerdiff) [[shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through)] - Vendored fork of the See-Through paper's LayerDiff component (Python/PyTorch).
- [interactor-seethrough-marigold-depth](https://github.com/V-Sekai-fire/interactor-seethrough-marigold-depth) [[shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through)] - Vendored fork of the See-Through paper's Marigold-depth component (Python/PyTorch).
- [interactor-seethrough-partseg](https://github.com/V-Sekai-fire/interactor-seethrough-partseg) [[shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through)] - Vendored fork of the See-Through paper's part-segmentation component (Python/PyTorch).
- [interactor-seethrough-vae](https://github.com/V-Sekai-fire/interactor-seethrough-vae) [[shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through)] - Vendored fork of the See-Through paper's VAE component (Python/PyTorch).
- [interactor-soma-x](https://github.com/V-Sekai-fire/interactor-soma-x) [[NVlabs/SOMA-X](https://github.com/NVlabs/SOMA-X)] - Vendored fork of SOMA-X (Python/PyTorch), the parametric body model that stands in for SMPL.
- [interactor-vllm-2x3090](https://github.com/V-Sekai-fire/interactor-vllm-2x3090) [[DominikBucko/qwen38-flash-next-2x3090](https://github.com/DominikBucko/qwen38-flash-next-2x3090)] - Qwen3.8-Flash-Next serving on two RTX 3090 cards.
- [IOPaint_VSK](https://github.com/V-Sekai-fire/IOPaint_VSK) [[AlanIWBFT/IOPaint_EasySetup](https://github.com/AlanIWBFT/IOPaint_EasySetup)] - IOPaint, with easier setup & run.
- [ipc-toolkit](https://github.com/V-Sekai-fire/ipc-toolkit) [[ipc-sim/ipc-toolkit](https://github.com/ipc-sim/ipc-toolkit)] - A set of reusable functions to integrate IPC into an existing simulation.
- [iree.gd](https://github.com/V-Sekai-fire/iree.gd) [[iree-gd/iree.gd](https://github.com/iree-gd/iree.gd)] - Running Pre-trained Machine Learning Model in Godot.
- [itch.io-Scrapy-Project](https://github.com/V-Sekai-fire/itch.io-Scrapy-Project) [[patkle/itch.io-Scrapy-Project](https://github.com/patkle/itch.io-Scrapy-Project)] - A Scrapy project that crawls itch.io.
- [JFA_driven_motion_blur_addon](https://github.com/V-Sekai-fire/JFA_driven_motion_blur_addon) [[sphynx-owner/JFA_driven_motion_blur_addon](https://github.com/sphynx-owner/JFA_driven_motion_blur_addon)] - an addon containing a jump flood algorithm driven motion blur compositor effect for Godot 4.3 beta.
- [json](https://github.com/V-Sekai-fire/json) [[nlohmann/json](https://github.com/nlohmann/json)] - JSON for Modern C++.
- [lean-truth-research-zk](https://github.com/V-Sekai-fire/lean-truth-research-zk) [[lambdaclass/truth_research_zk](https://github.com/lambdaclass/truth_research_zk)] - Verified Optimizing Compiler for Cryptographic Primitives.
- [libigl](https://github.com/V-Sekai-fire/libigl) [[libigl/libigl](https://github.com/libigl/libigl)] - Simple MPL-2.0-licensed C++ geometry processing library.
- [libsatsuma](https://github.com/V-Sekai-fire/libsatsuma) [[cgg-bern/libSatsuma](https://github.com/cgg-bern/libSatsuma)] - Exact and approximate solvers for minimum-cost-flow problems in bi-directed graphs.
- [libwebm](https://github.com/V-Sekai-fire/libwebm) [[webmproject/libwebm](https://github.com/webmproject/libwebm)] - Vendored fork of libwebm (C++).
- [limbo-ai](https://github.com/V-Sekai-fire/limbo-ai) [[limbonaut/limboai](https://github.com/limbonaut/limboai)] - LimboAI - Behavior Trees and State Machines for Godot 4.
- [lingbot-map](https://github.com/V-Sekai-fire/lingbot-map) [[Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map)] - Vendored fork of lingbot-map (Python/PyTorch), a feed-forward scene-reconstruction model.
- [liquid-feedback](https://github.com/V-Sekai-fire/liquid-feedback) [[codefordenver/liquidfeedback](https://github.com/codefordenver/liquidfeedback)] - LiquidFeedback tool for internal decision making.
- [llada-o-upstream](https://github.com/V-Sekai-fire/llada-o-upstream) [[ML-GSAI/LLaDA-o](https://github.com/ML-GSAI/LLaDA-o)] - Official implementation of **LLaDA-o**, an effective and length-adaptive omni diffusion model for unified multimodal generation and understanding.
- [loot-assets](https://github.com/V-Sekai-fire/loot-assets) [[M3-org/loot-assets](https://github.com/M3-org/loot-assets)] - Remixable assets for 3D avatars and game dev inspired by loot (for adventurers).
- [MaterialX](https://github.com/V-Sekai-fire/MaterialX) [[AcademySoftwareFoundation/MaterialX](https://github.com/AcademySoftwareFoundation/MaterialX)] - Vendored fork of MaterialX (C++).
- [maya-ace](https://github.com/V-Sekai-fire/maya-ace) [[NVIDIA/Maya-ACE](https://github.com/NVIDIA/Maya-ACE)] - Maya-ACE: A Reference Client Implementation for NVIDIA ACE Audio2Face Service.
- [mediamtx](https://github.com/V-Sekai-fire/mediamtx) [[bluenviron/mediamtx](https://github.com/bluenviron/mediamtx)] - Ready-to-use SRT / WebRTC / RTSP / RTMP / LL-HLS media server and media proxy that allows to read, publish, proxy, record and playback video and audio streams.
- [meshgpt-pytorch](https://github.com/V-Sekai-fire/meshgpt-pytorch) [[lucidrains/meshgpt-pytorch](https://github.com/lucidrains/meshgpt-pytorch)] - Implementation of MeshGPT, mesh generation with attention, in PyTorch.
- [miniflac](https://github.com/V-Sekai-fire/miniflac) [[Aritile/miniflac](https://github.com/Aritile/miniflac)] - Single-file FLAC decoder with a push-style API.
- [mitsuba3](https://github.com/V-Sekai-fire/mitsuba3) [[mitsuba-renderer/mitsuba3](https://github.com/mitsuba-renderer/mitsuba3)] - Mitsuba 3: A Retargetable Forward and Inverse Renderer.
- [ML_alchemy_worker](https://github.com/V-Sekai-fire/ML_alchemy_worker) [[xpportal/alchemy-worker](https://github.com/xpportal/alchemy-worker)] - Alchemy Worker is a Cloudflare Worker that performs string parsing and generates queries to inject personality and a desired prompt into GPT-3.
- [MoGe](https://github.com/V-Sekai-fire/MoGe) [[microsoft/MoGe](https://github.com/microsoft/MoGe)] - Vendored fork of MoGe (Python/PyTorch), a monocular geometry estimator.
- [MoRig](https://github.com/V-Sekai-fire/MoRig) [[zhan-xu/MoRig](https://github.com/zhan-xu/MoRig)] - Code for SIGGRAPH ASIA 2022 paper "Morig: Motion-Aware Rigging of Character Meshes from Point Clouds".
- [mount-drift](https://github.com/V-Sekai-fire/mount-drift) [[sinew-mocap/mount-drift](https://github.com/sinew-mocap/mount-drift)] - Sinew TIC calibrator (mount/drift) + the vkc Vulkan compute host (hexagon cluster).
- [multiplayer-fabric-webtransport](https://github.com/V-Sekai-fire/multiplayer-fabric-webtransport) [[bugnano/wtransport-elixir](https://github.com/bugnano/wtransport-elixir)] - Elixir bindings for the WTransport WebTransport library.
- [multiplayer-world](https://github.com/V-Sekai-fire/multiplayer-world) [[Ughuuu/Multiplayer-World](https://github.com/Ughuuu/Multiplayer-World)] - Multiplayer World where you can walk, chat, talk and play mini games.
- [NAF](https://github.com/V-Sekai-fire/NAF) [[valeoai/NAF](https://github.com/valeoai/NAF)] - Official Implementation of NAF: Zero-Shot Feature Upsampling via Neighborhood Attention Filtering.
- [nif](https://github.com/V-Sekai-fire/nif) [[taskweft/nif](https://github.com/taskweft/nif)]
- [ninfer-all](https://github.com/V-Sekai-fire/ninfer-all) [[iamwavecut/ninfer-all](https://github.com/iamwavecut/ninfer-all)] - NInfer for the RTX 3090, 4090 and 5090, consolidated from the forks that carry it.
- [nv-codec-headers](https://github.com/V-Sekai-fire/nv-codec-headers) [[FFmpeg/nv-codec-headers](https://github.com/FFmpeg/nv-codec-headers)] - automatic mirror of https://code.ffmpeg.org/FFmpeg/nv-codec-headers.
- [nvdiffrast](https://github.com/V-Sekai-fire/nvdiffrast) [[NVlabs/nvdiffrast](https://github.com/NVlabs/nvdiffrast)] - Nvdiffrast - Modular Primitives for High-Performance Differentiable Rendering.
- [nvdiffrec](https://github.com/V-Sekai-fire/nvdiffrec) [[JeffreyXiang/nvdiffrec](https://github.com/JeffreyXiang/nvdiffrec)] - Official code for the CVPR 2022 (oral) paper "Extracting Triangular 3D Models, Materials, and Lighting From Images".
- [nx_shuttle](https://github.com/V-Sekai-fire/nx_shuttle) [[mortont/axon_onnx](https://github.com/mortont/axon_onnx)] - Compiles an `Nx.Defn` function to an ONNX graph.
- [Objaverse-downloader](https://github.com/V-Sekai-fire/Objaverse-downloader) [[MarcusLoppe/Objaverse-downloader](https://github.com/MarcusLoppe/Objaverse-downloader)] - Instead of downloading the entire 8.9 TB dataset, download only files you need!
- [oculus-networked-physics-sample](https://github.com/V-Sekai-fire/oculus-networked-physics-sample) [[fbsamples/oculus-networked-physics-sample](https://github.com/fbsamples/oculus-networked-physics-sample)] - This is a networked physics sample for Rift built in Unity.
- [OmniPart](https://github.com/V-Sekai-fire/OmniPart) [[HKU-MMLab/OmniPart](https://github.com/HKU-MMLab/OmniPart)]
- [onnxruntime-mlx](https://github.com/V-Sekai-fire/onnxruntime-mlx) [[justinchuby/onnxruntime-mlx](https://github.com/justinchuby/onnxruntime-mlx)] - MLX provider for onnxruntime.
- [openbao](https://github.com/V-Sekai-fire/openbao) [[openbao/openbao](https://github.com/openbao/openbao)] - OpenBao fork with restored FoundationDB storage backend (MPL-2.0, from Vault v1.14.8).
- [OpenUSD](https://github.com/V-Sekai-fire/OpenUSD) [[PixarAnimationStudios/OpenUSD](https://github.com/PixarAnimationStudios/OpenUSD)] - Universal Scene Description.
- [openvdb](https://github.com/V-Sekai-fire/openvdb) [[Huangzizhou/openvdb](https://github.com/Huangzizhou/openvdb)]
- [Optimized-Tris-to-Quads-Converter](https://github.com/V-Sekai-fire/Optimized-Tris-to-Quads-Converter) [[Rulesobeyer/Optimized-Tris-to-Quads-Converter](https://github.com/Rulesobeyer/Optimized-Tris-to-Quads-Converter)] - Tris to quads for Blender 4.0+ by mathematical optimization.
- [paints-undo](https://github.com/V-Sekai-fire/paints-undo) [[lllyasviel/Paints-UNDO](https://github.com/lllyasviel/Paints-UNDO)] - Understand Human Behavior to Align True Needs.
- [PartCrafter](https://github.com/V-Sekai-fire/PartCrafter) [[JackDainzh/PartCrafter-Windows](https://github.com/JackDainzh/PartCrafter-Windows)] - PartCrafter: Structured 3D Mesh Generation via Compositional Latent Diffusion Transformers for Windows.
- [pict](https://github.com/V-Sekai-fire/pict) [[microsoft/pict](https://github.com/microsoft/pict)] - Pairwise Independent Combinatorial Tool.
- [Pixal3D](https://github.com/V-Sekai-fire/Pixal3D) [[TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D)] - Vendored fork of Pixal3D (Python/PyTorch), a pixel-aligned image-to-3D generator.
- [pixal3d-ggml](https://github.com/V-Sekai-fire/pixal3d-ggml) [[rms80/trellis2cpp](https://github.com/rms80/trellis2cpp)] - C++/ggml port of TRELLIS.2 stage-1 geometry.
- [plausible](https://github.com/V-Sekai-fire/plausible) [[leanprover-community/plausible](https://github.com/leanprover-community/plausible)] - A property testing framework for Lean 4 that integrates into the tactic framework.
- [plausible-witness-dag](https://github.com/V-Sekai-fire/plausible-witness-dag) [[fire/plausible-witness-dag](https://github.com/fire/plausible-witness-dag)] - Plausible witness DAG.
- [polygonjs](https://github.com/V-Sekai-fire/polygonjs) [[polygonjs/polygonjs](https://github.com/polygonjs/polygonjs)] - node-based WebGL design tool.
- [popcorn](https://github.com/V-Sekai-fire/popcorn) [[software-mansion/popcorn](https://github.com/software-mansion/popcorn)] - Running Elixir in the browser.
- [project-babble](https://github.com/V-Sekai-fire/project-babble) [[Project-Babble/ProjectBabble](https://github.com/Project-Babble/ProjectBabble)] - Open-source mouth tracking method for VR.
- [pyrowave](https://github.com/V-Sekai-fire/pyrowave) [[Themaister/pyrowave](https://github.com/Themaister/pyrowave)] - PyroWave, an intra-only video codec built for fast GPU encode and decode.
- [rapidcheck](https://github.com/V-Sekai-fire/rapidcheck) [[emil-e/rapidcheck](https://github.com/emil-e/rapidcheck)] - QuickCheck clone for C++ with the goal of being simple to use with as little boilerplate as possible.
- [ReboSlime](https://github.com/V-Sekai-fire/ReboSlime) [[Daniel81i/ReboSlime](https://github.com/Daniel81i/ReboSlime)] - Use ReboCap with SlimeVR Server over OSC.
- [rf-detr](https://github.com/V-Sekai-fire/rf-detr) [[roboflow/rf-detr](https://github.com/roboflow/rf-detr)] - RF-DETR, Roboflow's real-time object detection model architecture, designed for fine-tuning.
- [rtmps-hls-server](https://github.com/V-Sekai-fire/rtmps-hls-server) [[JamiePhonic/rtmps-hls-server](https://github.com/JamiePhonic/rtmps-hls-server)] - A docker file to create a streaming server that supports RTMP, HLS and DASH content based on nginx and nginx-rtmp-module.
- [runtime_godot_block_coding](https://github.com/V-Sekai-fire/runtime_godot_block_coding) [[DanielSnd/runtime_godot_block_coding](https://github.com/DanielSnd/runtime_godot_block_coding)] - runtime_blocks_code.
- [sam_2_remove_video_background](https://github.com/V-Sekai-fire/sam_2_remove_video_background) [[argildotai/sam2removevideobackground](https://github.com/argildotai/sam2removevideobackground)] - This project uses the Segment Anything 2 (SAM2) model to remove backgrounds from videos.
- [SAMPart3D](https://github.com/V-Sekai-fire/SAMPart3D) [[Pointcept/SAMPart3D](https://github.com/Pointcept/SAMPart3D)] - SAMPart3D: Segment Any Part in 3D Objects.
- [sd-libwebm](https://github.com/V-Sekai-fire/sd-libwebm) [[webmproject/libwebm](https://github.com/webmproject/libwebm)] - Mirror only.
- [sd-libwebp](https://github.com/V-Sekai-fire/sd-libwebp) [[webmproject/libwebp](https://github.com/webmproject/libwebp)] - Mirror only.
- [service-burrito](https://github.com/V-Sekai-fire/service-burrito) [[burrito-elixir/burrito](https://github.com/burrito-elixir/burrito)] - Wrap your application in a BEAM Burrito!
- [SK_fire_magical_girl](https://github.com/V-Sekai-fire/SK_fire_magical_girl) [[fire-archive/SK_avatar_wellness](https://github.com/fire-archive/SK_avatar_wellness)]
- [skin-tokens-ggml](https://github.com/V-Sekai-fire/skin-tokens-ggml) [[localai-org/skin-tokens.cpp](https://github.com/localai-org/skin-tokens.cpp)] - C++/GGML conversion of VAST-AI SkinTokens; Auto rigs a mesh ready for animation.
- [solve](https://github.com/V-Sekai-fire/solve) [[sinew-mocap/solve](https://github.com/sinew-mocap/solve)] - Sinew body solve — FK + LBS skinning of the ANNY body (hexagon cluster).
- [solverl](https://github.com/V-Sekai-fire/solverl) [[bokner/solverl](https://github.com/bokner/solverl)] - Erlang/Elixir interface to MiniZinc.
- [soma-retargeter](https://github.com/V-Sekai-fire/soma-retargeter) [[NVIDIA/soma-retargeter](https://github.com/NVIDIA/soma-retargeter)] - SOMA BVH to humanoid robot motion retargeting library built with Newton and NVIDIA Warp.
- [sqlite-jdbc](https://github.com/V-Sekai-fire/sqlite-jdbc) [[xerial/sqlite-jdbc](https://github.com/xerial/sqlite-jdbc)] - SQLite JDBC Driver.
- [stable-diffusion-ggml](https://github.com/V-Sekai-fire/stable-diffusion-ggml) [[leejet/stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)] - Diffusion model(SD,Flux,Wan,Qwen Image,Z-Image,...) inference in pure C/C++.
- [stable-motion](https://github.com/V-Sekai-fire/stable-motion) [[Murrol/StableMotion](https://github.com/Murrol/StableMotion)]
- [star-vector](https://github.com/V-Sekai-fire/star-vector) [[nyirocsaba/star-vector](https://github.com/nyirocsaba/star-vector)] - StarVector is a foundation model for SVG generation that transforms vectorization into a code generation task.
- [Storages](https://github.com/V-Sekai-fire/Storages) [[LDYang694/Storages](https://github.com/LDYang694/Storages)]
- [T_cc0_cat_A](https://github.com/V-Sekai-fire/T_cc0_cat_A) [[jeanahelver/CC0-CAT](https://github.com/jeanahelver/CC0-CAT)] - We have cats in the public domain.
- [test_specular_aliasing](https://github.com/V-Sekai-fire/test_specular_aliasing) [[Calinou/test_specular_aliasing](https://github.com/Calinou/test_specular_aliasing)] - Godot 4.0 test project for specular aliasing.
- [three-nanite](https://github.com/V-Sekai-fire/three-nanite) [[AIFanatic/three-nanite](https://github.com/AIFanatic/three-nanite)] - An attempt at reproducing unreal nanite in threejs.
- [tla-transmutation](https://github.com/V-Sekai-fire/tla-transmutation) [[bugarela/tla-transmutation](https://github.com/bugarela/tla-transmutation)] - Elixir code and test generation from TLA+ specifications.
- [TOOL_agent_reinforcement_trainer](https://github.com/V-Sekai-fire/TOOL_agent_reinforcement_trainer) [[OpenPipe/ART](https://github.com/OpenPipe/ART)] - OpenPipe ART (Agent Reinforcement Trainer): train LLM agents.
- [TOOL_blender_xatlas](https://github.com/V-Sekai-fire/TOOL_blender_xatlas) [[s-ilent/blender-xatlas](https://github.com/s-ilent/blender-xatlas)] - Xatlas Packer Addon for Blender.
- [tool_character_concepts](https://github.com/V-Sekai-fire/tool_character_concepts) [[fogside/rpm_characters_replicate](https://github.com/fogside/rpm_characters_replicate)]
- [tool_clip_interrogator](https://github.com/V-Sekai-fire/tool_clip_interrogator) [[pharmapsychotic/clip-interrogator](https://github.com/pharmapsychotic/clip-interrogator)] - Image to prompt with BLIP and CLIP.
- [TOOL_cloth_dynamics](https://github.com/V-Sekai-fire/TOOL_cloth_dynamics) [[V-Sekai/TOOL_cloth_dynamics](https://github.com/V-Sekai/TOOL_cloth_dynamics)]
- [TOOL_heroix](https://github.com/V-Sekai-fire/TOOL_heroix) [[arielj/heroix](https://github.com/arielj/heroix)] - Heroic Games Launcher, written in Elixir and Phoenix LiveView.
- [tool_music_source_separation](https://github.com/V-Sekai-fire/tool_music_source_separation) [[chenxwh/demucs](https://github.com/chenxwh/demucs)] - Code for the paper Hybrid Spectrogram and Waveform Source Separation.
- [tool_remove_background](https://github.com/V-Sekai-fire/tool_remove_background) [[danielgatis/rembg](https://github.com/danielgatis/rembg)] - Rembg is a tool to remove images background.
- [tool_scale_arbitrary_super_resolution](https://github.com/V-Sekai-fire/tool_scale_arbitrary_super_resolution) [[SYSU-SAIL/ArbSR](https://github.com/SYSU-SAIL/ArbSR)]
- [tool_stylized_talking_face](https://github.com/V-Sekai-fire/tool_stylized_talking_face) [[chenxwh/SadTalker](https://github.com/chenxwh/SadTalker)]
- [tool_tortoise_text_to_speech](https://github.com/V-Sekai-fire/tool_tortoise_text_to_speech) [[afiaka87/tortoise-tts](https://github.com/afiaka87/tortoise-tts)] - A multi-voice TTS system trained with an emphasis on quality.
- [transport-elixir-libgodot-connector](https://github.com/V-Sekai-fire/transport-elixir-libgodot-connector) [[Ughuuu/libgodot-elixir](https://github.com/Ughuuu/libgodot-elixir)] - Runs LibGodot inside Elixir.
- [transport-usd-viewer](https://github.com/V-Sekai-fire/transport-usd-viewer) [[coryrylan/usd-viewer](https://github.com/coryrylan/usd-viewer)] - Vendored fork of usd-viewer (JavaScript/TypeScript).
- [transport-xr-grid](https://github.com/V-Sekai-fire/transport-xr-grid) [[V-Sekai/transport-xr-grid](https://github.com/V-Sekai/transport-xr-grid)] - Fork of V-Sekai/xr-grid (GDScript).
- [trellis](https://github.com/V-Sekai-fire/trellis) [[pinokiofactory/TRELLIS](https://github.com/pinokiofactory/TRELLIS)] - A pinokio script for https://github.com/microsoft/TRELLIS.
- [TRELLIS-2](https://github.com/V-Sekai-fire/TRELLIS-2) [[microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)] - Vendored fork of TRELLIS.2 (Python/PyTorch), the structured-latent 3D generator.
- [trust-lean](https://github.com/V-Sekai-fire/trust-lean) [[lambdaclass/trust-lean](https://github.com/lambdaclass/trust-lean)] - Verified codegen framework for cryptographic primitives — Lean 4, 0 sorry.
- [udon2godot](https://github.com/V-Sekai-fire/udon2godot) [[fireflyk64/udon2godot](https://github.com/fireflyk64/udon2godot)] - Udon 2 godot translator.
- [udp](https://github.com/V-Sekai-fire/udp) [[mas-bandwidth/udp](https://github.com/mas-bandwidth/udp)] - Writing highly scalable backends in UDP.
- [unidot_importer](https://github.com/V-Sekai-fire/unidot_importer) [[V-Sekai/unidot_importer](https://github.com/V-Sekai/unidot_importer)] - Import .unitypackage and other assets designed for Unity Engine as a GDScript addon for vanilla Godot 4.x.
- [unity-import-shadermotion-export-bvh](https://github.com/V-Sekai-fire/unity-import-shadermotion-export-bvh) [[guillefix/shadermotion-bvh-utils](https://github.com/guillefix/shadermotion-bvh-utils)] - shadermotion and BVH exporting.
- [usd-godot](https://github.com/V-Sekai-fire/usd-godot) [[meshula/usd-godot](https://github.com/meshula/usd-godot)] - A plugin that integrates Universal Scene Description (USD) into Godot.
- [utils3d](https://github.com/V-Sekai-fire/utils3d) [[EasternJournalist/utils3d](https://github.com/EasternJournalist/utils3d)] - A collection of useful functions for 3D vision & graphics research in Python.
- [utils3d-moge](https://github.com/V-Sekai-fire/utils3d-moge) [[EasternJournalist/utils3d-moge](https://github.com/EasternJournalist/utils3d-moge)] - 3D vision & graphics utilities for Python.
- [v-sekai-game](https://github.com/V-Sekai-fire/v-sekai-game) [[V-Sekai/v-sekai-game](https://github.com/V-Sekai/v-sekai-game)] - Open-source VR socials.
- [vk_video_samples](https://github.com/V-Sekai-fire/vk_video_samples) [[nvpro-samples/vk_video_samples](https://github.com/nvpro-samples/vk_video_samples)] - Vulkan video samples.
- [VoxHammer](https://github.com/V-Sekai-fire/VoxHammer) [[Nelipot-Lee/VoxHammer](https://github.com/Nelipot-Lee/VoxHammer)] - Vendored fork of VoxHammer (Python/PyTorch), a training-free 3D editor.
- [VRMConverterForVRChat](https://github.com/V-Sekai-fire/VRMConverterForVRChat) [[esperecyan/VRMConverterForVRChat](https://github.com/esperecyan/VRMConverterForVRChat)]
- [VSK_desktop_app](https://github.com/V-Sekai-fire/VSK_desktop_app) [[elixir-desktop/desktop-example-app](https://github.com/elixir-desktop/desktop-example-app)] - Elixir Automation App using the Desktop library with LiveView to create a desktop app.
- [VSK_godot_web_file_manager](https://github.com/V-Sekai-fire/VSK_godot_web_file_manager) [[SIsilicon/Godot-Web-File-Manager](https://github.com/SIsilicon/Godot-Web-File-Manager)] - A user script for the web that allows you to view and edit files in the Godot Web Editor.
- [walk-the-dog](https://github.com/V-Sekai-fire/walk-the-dog) [[PeizhuoLi/walk-the-dog](https://github.com/PeizhuoLi/walk-the-dog)] - A vector-quantized periodic autoencoder (VQ-PAE) for motion alignment across different morphologies with no supervision [SIGGRAPH 2024].
- [wax](https://github.com/V-Sekai-fire/wax) [[SamuelMarks/wax](https://github.com/SamuelMarks/wax)] - A tiny programming language that transpiles to C, C++, Java, TypeScript, Python, C#, Swift, Lua and WebAssembly 🚀.
- [world-godot](https://github.com/V-Sekai-fire/world-godot) [[V-Sekai/world-godot](https://github.com/V-Sekai/world-godot)] - V-Sekai Godot Engine build.
- [xdp](https://github.com/V-Sekai-fire/xdp) [[mas-bandwidth/xdp](https://github.com/mas-bandwidth/xdp)] - XDP example programs.

</details>

## Related

- [Awesome V-Sekai](https://github.com/V-Sekai/awesome-v-sekai) - The V-Sekai list this one follows.
- [V-Sekai](https://github.com/V-Sekai) - The main V-Sekai organization.
- [Taskweft](https://github.com/taskweft/taskweft) - The HTN planner.
- [Awesome Godot](https://github.com/godotengine/awesome-godot) - Godot Engine frameworks, libraries and resources.

## Contributing

Read [CONTRIBUTING](CONTRIBUTING). Pull requests and issues are welcome.
