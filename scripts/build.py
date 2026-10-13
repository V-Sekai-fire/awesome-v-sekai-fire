#!/usr/bin/env python3
"""Build README.md from the data scripts/fetch.py writes.

Usage: python3 scripts/fetch.py && python3 scripts/build.py [README.md]
       python3 scripts/build.py --check   # print section membership, write nothing

Sections are subject groups chosen by name rules in SECTIONS (first match wins).
A new repo that matches no rule stops the build: add it to a section.
OVERRIDES replace descriptions that are missing, misleading, or carry unbenchmarked
speed/size/"SOTA" claims (see CONTRIBUTING).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get("AWESOME_DATA") or os.path.join(HERE, "..", ".cache")
repos = json.load(open(os.path.join(DATA, "repos.json")))
readme = json.load(open(os.path.join(DATA, "readme-desc.json")))
forks = {r["name"]: r for r in json.load(open(os.path.join(DATA, "forks.json")))}

pub = [r for r in repos if r["visibility"] == "PUBLIC" and not r["isArchived"]]  # fetch.py is public-only; double check
orig = {r["name"]: r for r in pub if not r["isFork"]}
frk = {r["name"]: r for r in pub if r["isFork"]}

JUNK = re.compile(r"^(license:|\*|\[|_|\*\*|SPDX|\W|V-Sekai is an open source|alt=|-\s|https?://|Customized by|None$)")

def first_sentence(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # strip md links
    s = re.sub(r"\s+", " ", s).strip()
    m = re.match(r"(.+?(?<!\b[A-Z])[.!?])(\s|$)", s)
    s = m.group(1) if m else s
    if len(s) > 160:
        s = s[:157].rsplit(" ", 1)[0] + "…"
    return s

OVERRIDES = {
    "biharmonic-3d-coordinates-siggraph-2024": "Reference code for biharmonic 3D coordinates (SIGGRAPH 2024).",
    "contract-anny": "The ANNY parametric human body model, carried from naver/anny.",
    "interactor-blender-multi-user": "The Blender multi-user collaborative editing addon, carried from slumber/multi-user.",
    "entities-fire-work": "A static web gallery of K. S. Ernest (iFire) Lee's work.",
    "entities-godot-catlin-and-the-lucky-cat": "A Magical Girls Game Jam 7 game where spells are cast by drawing gestures with the mouse.",
    "entities-godot-farm-chickens": "A minimal sample project for Godot 4's network replication system.",
    "entities-multiplayer-fabric-interaction-system": "Delegates input events, such as mouse or VR controller clicks, as 3D raycasts into a scene, with canvas_plane for UI.",
    "entities-fuschia-tin-giraffe": "OSXCross: a macOS cross toolchain for Linux, FreeBSD, OpenBSD and Android.",
    "interactor-flow": "The Immersive Digital Twin Experience Flow (IDTX Flow) plugin for Godot, from idtx-flow.",
    "interactor-tool-logoscale": "Image upscaling work with ESRGAN.",
    "interactor-tool-walk-the-dog": "A vector-quantized periodic autoencoder that aligns motion across different morphologies.",
    "interactor-mesh-transformer": "Mesh generation with attention, in PyTorch.",
    "interactor-vertex": "Experimental backend that serves custom game content.",
    "service-language-model": "",
    "meshgpt-pytorch": "Implementation of MeshGPT, mesh generation with attention, in PyTorch.",
    "rf-detr": "RF-DETR, Roboflow's real-time object detection model architecture, designed for fine-tuning.",
    "pyrowave": "PyroWave, an intra-only video codec built for fast GPU encode and decode.",
    "interactor-vllm-2x3090": "Qwen3.8-Flash-Next serving on two RTX 3090 cards.",
    "hymotion-animation-gen-mixamo-retargeting": "A CPU Docker image for the HY-Motion API with Mixamo retargeting.",
    "TOOL_heroix": "Heroic Games Launcher, written in Elixir and Phoenix LiveView.",
    "dag_amendment": "DAG Amendment for inverse control of parametric shapes, the official Blender implementation.",
    "itch.io-Scrapy-Project": "A Scrapy project that crawls itch.io.",
    "usd-godot": "A plugin that integrates Universal Scene Description (USD) into Godot.",
    "ninfer-all": "NInfer for the RTX 3090, 4090 and 5090, consolidated from the forks that carry it.",
    "app-ayon-backend": "The Docker-based deployment for the Ayon production-tracking server.",
    "ReboSlime": "Use ReboCap with SlimeVR Server over OSC.",
    "godot-motion-matching-demo": "A third-person character controller built on the Godot Motion Matching extension.",
    "godot-sandbox": "Godot Sandbox: run untrusted code safely in a RISC-V sandbox inside Godot.",
}

def describe(name):
    if name in OVERRIDES:
        return OVERRIDES[name]
    r = orig.get(name) or frk.get(name)
    d = (r or {}).get("description") or ""
    if name in orig and d.startswith(("Migrated from mirror", "Fork of ")) and readme.get(name):
        d = readme[name]
    if not d:
        d = readme.get(name) or ""
    d = d.strip()
    if not d or JUNK.match(d):
        return ""
    d = first_sentence(d)
    d = d.replace("|", "\\|")
    if not d.endswith((".", "!", "?", "…")):
        d += "."
    return d

# Section rules: (title, blurb, predicate). First match wins.
def has(*words):
    return lambda n: any(w in n for w in words)

def names(*ns):
    s = set(ns)
    return lambda n: n in s

SECTIONS = [
    ("Engine and client",
     "The Godot engine branch the fabric runs on, and the build that assembles it.",
     names("entities-godot", "entities-images", "entities-assembly", "entities-curvenet-godot",
           "entities-multiplayer-fabric-rx", "entities-multiplayer-fabric-xr-dev", "transport-client")),
    ("Workspace, decisions and agreements",
     "How the workspace is laid out, decided and checked. Start here.",
     names("awesome-v-sekai-fire", "contract-manifest-taskweft", "manuals-weftspun", "weftspun-agreements", "dot-claude", "dot-vscode",
           ".github", ".vscode", "interactor-infrastructure-logbook", "contract-multiplayer-fabric-skills",
           "contract-multiplayer-fabric-archive", "interactor-study-data-vsk", "contract-bootstrap",
           "contract-taskweft-proposals", "fabric", "interactor-tropes-removal-model", "repository-witness-cpp")),
    ("Multiplayer fabric: planes, transports and zones",
     "The shared-world server stack: the iceoryx2 bus, the authority and fan-out planes, the QUIC/WebTransport edges, and zone hosting.",
     names("contract-bus", "contract-command", "contract-protocol", "contract-entity-packet", "contract-connection-fsm",
           "contract-http3-queue", "contract-interest-mgmt", "contract-wt", "contract-zone-backend",
           "interactor-weft", "interactor-authority", "interactor-crowd", "interactor-janet", "interactor-tool",
           "interactor-motion", "interactor-physics", "interactor-ward", "interactor-fabric-zone", "interactor-vertex",
           "interactor-voice", "interactor-spatial-oracle", "interactor-tla-game-networking-model",
           "interactor-elixir-enet", "interactor-elixir-entity-database", "interactor-quickstart",
           "entities-enet-godot", "entities-godot-patrol-client", "interactor-aria-patrol-client",
           "interactor-aria-patrol-solver", "repository-entity-store", "datasource-store", "datasource-queen",
           "service-zone", "service-behaviour", "service-docker-multiplayer-fabric",
           "service-multiplayer-fabric-hosting", "service-multiplayer-fabric-generate-secrets",
           "service-phoenix-uro-webrtc-signaling", "transport-gateway-c", "transport-gateway-python",
           "transport-ingest-c", "transport-ingest-python", "transport-fanout", "transport-asset",
           "transport-bus-cli")
     ),
    ("Game rules as Lean 4 hexagons",
     "Gameplay and engine rules stated and checked in Lean 4, often with Plausible property tests, then emitted to C or Slang.",
     lambda n: ((orig[n]["primaryLanguage"] or {}).get("name") == "Lean" and not n.startswith("interactor-taskweft"))
     or n in ("contract-lean-slang", "contract-lbfgsb", "contract-anny-kernels", "contract-trellis2-mesh-vae-slang",
              "contract-materialx-shaders-lean", "contract-hm08-partition", "contract-bone-kernels")),
    ("godot-sandbox guests (RISC-V)",
     "Programs that run as sandboxed RISC-V ELF guests inside Godot through godot-sandbox and libriscv.",
     lambda n: n in ("interactor-bake", "interactor-cage", "interactor-curvenet", "interactor-drape",
                     "interactor-garment-fit", "interactor-headfit", "interactor-lasso", "interactor-remesh",
                     "interactor-usd-guest", "interactor-motion-guest", "interactor-rfdetr-seg-guest",
                     "interactor-mujoco-riscv64", "interactor-mujoco-sandbox-demo", "interactor-mujoco-cloth-sim",
                     "interactor-slughorn", "interactor-multiplayer-fabric-elf-programs",
                     "contract-guest-common", "contract-guest-runtime", "contract-ggml-rd",
                     "entities-libriscv", "entities-godot-sandbox-gdscript-compiler",
                     "entities-godot-sandbox-robust-weight-transfer", "entities-godot-gdscript-compiler-demo",
                     "entities-godot-bird-plane", "entities-godot-enet-sandbox", "service-weft-warp-burrito",
                     "repository-riscv64-sysroot", "interactor-taskweft-crowd",
                     "interactor-lean-guest", "hypercore-chat-guest")),
    ("Taskweft and planning",
     "Hierarchical task network planning: the Taskweft planner, its domains, and the agents that use it.",
     lambda n: n.startswith("interactor-taskweft") or n.startswith("interactor-aria-")
     or n in ("transport-mcp-client", "interactor-rebac", "interactor-ranktration", "transport-artifacts-mmo-mcp",
              "datasource-easy-diffusion-traces", "entities-multiplayer-fabric-rpg")),
    ("Avatars, motion and inverse kinematics",
     "Humanoid bodies, VRM avatars, retargeting, IK solvers, tracking hardware and motion generation.",
     lambda n: n.startswith(("datasource-anim-", "datasource-sk-", "contract-anny"))
     or n in ("datasource-skel-liqu", "entities-humanoid-rom", "entities-anny-creator", "entities-godot-toon-shaders",
              "interactor-test-many-bone-ik", "interactor-test-ewbik", "interactor-test-godot-vrm-motion-checker",
              "interactor-test-range-of-motion", "interactor-shader-motion-mirror", "interactor-kimodo-text-to-motion",
              "interactor-skintokens-auto-rig", "interactor-g1-sim-to-real", "interactor-gait-classification",
              "interactor-pose-consensus", "interactor-fire-smol-slimes", "interactor-blender-bone-to-mesh",
              "frame-eye-osc", "frame-controller-sim", "entities-tundra-and-vive-tracker-chest-mount",
              "contract-orbit-views", "transport-meshing-pen", "contract-sinew-align",
              "contract-swing-twist-kusudama", "interactor-tool-walk-the-dog")),
    ("Godot modules, addons and test projects",
     "Engine modules, GDExtensions, editor addons and the small projects that check them.",
     lambda n: n.startswith(("entities-godot-", "interactor-addon-", "interactor-tool-godot-", "interactor-flow"))
     and n != "interactor-flow-hello-world"
     or n.startswith("entities-multiplayer-fabric-")
     or n in ("entities-cassie-flow-project", "entities-idtx-flow-project", "entities-opentelemetry-godot-project",
              "entities-order-independent-transparency", "entities-zone-baker", "entities-khr-interactivity-samples",
              "entities-aria-godot", "entities-sponza-godot-audio", "transport-elixir-libgodot-connector",
              "interactor-test-javascript", "interactor-test-material-x", "interactor-mp-seeking-test",
              "interactor-test-scripting-01", "interactor-multiplayer-fabric-meta")),
    ("Garments and 3D content generation",
     "weftfit garment retargeting, mesh processing, and image- or text-to-3D model images.",
     lambda n: n in ("interactor-retarget", "interactor-obj", "interactor-stage", "interactor-stage-runtime",
                     "interactor-viewer", "interactor-cli", "interactor-ufbx-to-openusd", "repository-usd-core-wheels",
                     "interactor-trellis2-ex", "interactor-trellis2-image-mesh-painting",
                     "interactor-trellis2-image-to-textured-mesh", "interactor-pixal3d-image-to-textured-mesh",
                     "interactor-voxhammer-image-mesh-editing", "interactor-voxhammer-text-mesh-editing",
                     "interactor-p3sam-mesh-segmentation", "interactor-mesh-transformer",
                     "interactor-dress-designer-maskscore", "interactor-material-graph-maskscore",
                     "interactor-material-sampler-maskscore", "interactor-texture-painter-maskscore",
                     "interactor-blender-meshoptimizer", "interactor-tool-quadwild", "interactor-libeigen-eigen",
                     "biharmonic-3d-coordinates-siggraph-2024", "service-cog-sam-part-3d",
                     "service-cog-vsk-mesh-optimizer", "interactor-blender-multi-user", "weftspun-usd-viewer",
                     "contract-billboard-labels", "contract-vsekai-materialx", "weftspun-character-taxonomy",
                     "interactor-vtracer-pixel", "interactor-space-starvector-8b-im2svg", "interactor-panelspun")),
    ("Machine learning and inference",
     "ggml ports, model images, Elixir ML bindings and training experiments.",
     lambda n: (n.startswith(("interactor-see-through", "interactor-rf-detr", "interactor-ml-", "service-cog-"))
                and n != "interactor-ml-image-generation")
     or n in ("interactor-nx-ggml", "interactor-elixir-turboquant-llm", "interactor-multiplayer-fabric-llm",
              "interactor-minicpm-vision", "interactor-editscore-lora-qwen3vl-4b", "interactor-cyclegan-style-transfer",
              "interactor-executorch-tiling", "interactor-tosa-converter-for-tflite", "interactor-hailo-ugen300",
              "interactor-multimodal-semantic-ids", "interactor-residual-fsq-recommender",
              "entities-elixir-holographic-reduced-representation", "interactor-elixir-forge",
              "interactor-shader-gpt", "interactor-shadergpt", "interactor-character-concept-acclaim",
              "interactor-tool-rotten-tomatoes-01", "interactor-tool-logoscale", "service-see-through",
              "service-language-model", "entities-vsk-docker-python-notebook", "interactor-python-notebooks",
              "interactor-fire-architext-v2", "interactor-game-tag-starvote-ballots", "datasource-llama-dataset-01",
              "datasource-meshgpt-dataset-02")),
    ("MCP servers and agent tools",
     "Model Context Protocol servers and tools that let agents drive engines, editors and solvers.",
     lambda n: n.endswith("-mcp") or n.startswith("transport-mcp-") or n in ("interactor-xr-pilot", "transport-sympy-mcp", "interactor-touch-companion")),
    ("Video, audio and broadcast",
     "CineForm recording, AV1/FLAC muxing and the desk's broadcast setup.",
     lambda n: n in ("interactor-cineform", "interactor-av1mkv", "service-cineform", "transport-cineform-tui",
                     "transport-obs-broadcast", "entities-core-streaming-steam-deck", "entities-parsec",
                     "interactor-deskpin")),
    ("Infrastructure, secrets and delivery",
     "Secrets, storage, builds, launchers and observability.",
     lambda n: n.startswith("service-") or n in (
         "transport-central-launcher", "transport-shepherd", "datasource-launcher-chunks", "interactor-sqlar-cas",
         "interactor-aria-storage", "datasource-duckdb", "datasource-versitygw-local", "interactor-parqview",
         "transport-usbip-frame", "interactor-ecto-bench-tpcc", "entities-vsk-database-roundtable",
         "interactor-flow-hello-world", "interactor-popcorn-test", "interactor-tool-game-start",
         "transport-oauth-mcp-bridge", "entities-fuschia-tin-giraffe", "interactor-test-appium-windows-hello-world")),
    ("Worlds, scenes, stories and art",
     "Maps, scenes, interactive fiction, galleries and concept work.",
     lambda n: n.startswith(("entities-scene-", "entities-vsk-", "entities-world-")) or n in (
         "entities-bullet-game-jam", "entities-ink-bullet-train", "entities-sakuragaoka-station", "entities-starforged",
         "entities-env-cafe", "entities-fire-work", "interactor-ml-image-generation", "contract-tutorial-shapes-rhino3d-01",
         "interactor-tool-inspirator", "interactor-udon-flat", "datasource-concept-fire-girl")
     or n.startswith("datasource-gallery-")),
    ("Datasets and test corpora",
     "Training sets, evaluation sets and importer fixtures.",
     lambda n: n.startswith(("datasource-", "interactor-test-fbx"))),
]

assigned = {}
for n in sorted(orig, key=str.lower):
    for i, (_, _, pred) in enumerate(SECTIONS):
        try:
            ok = pred(n)
        except Exception:
            ok = False
        if ok:
            assigned.setdefault(i, []).append(n)
            break
    else:
        assigned.setdefault(-1, []).append(n)

if "--check" in sys.argv:
    for i, ns in sorted(assigned.items()):
        title = SECTIONS[i][0] if i >= 0 else "UNASSIGNED"
        print(f"\n## {title} ({len(ns)})\n  " + ", ".join(ns))
    sys.exit(0)

assert -1 not in assigned, assigned.get(-1)

def lang(name):
    r = orig.get(name) or frk.get(name)
    l = (r.get("primaryLanguage") or {}).get("name")
    return f" ({l})" if l else ""

def anchor(t):
    a = t.lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")

def item(name):
    d = describe(name)
    return f"- [{name}](https://github.com/V-Sekai-fire/{name}){' - ' + d if d else ''}{lang(name)}"

out = []
out.append("# Awesome V-Sekai-fire [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
out.append("A curated list of the public projects in the [V-Sekai-fire](https://github.com/V-Sekai-fire) organization: "
           "the multiplayer fabric, Godot sandbox guests, Lean 4 contracts, Taskweft planning, avatar and garment tools, "
           "and the experiments around them. It is the companion to [Awesome V-Sekai](https://github.com/V-Sekai/awesome-v-sekai).\n")
out.append("## How the names work\n")
out.append("Most repositories carry a prefix that places them on one side of the workspace hexagon "
           "(see [contract-manifest-taskweft](https://github.com/V-Sekai-fire/contract-manifest-taskweft)):\n")
for p, d in [("contract-", "a specification or interface: Lean proofs, wire formats, shared headers."),
             ("datasource-", "data the system reads: datasets, avatars, fixtures."),
             ("entities-", "engines, game projects and domain cores."),
             ("interactor-", "a unit of work: a plane, a guest, a library or a model image."),
             ("repository-", "storage interfaces and prebuilt artifacts."),
             ("service-", "something that runs: a deployment, a container, a build service."),
             ("transport-", "an edge that carries requests in or out: gateways, CLIs, MCP servers.")]:
    out.append(f"- `{p}` - {d}")
out.append("\nThis list sorts by subject, not by prefix. Private repositories are not listed.\n")
out.append("## Contents\n")
for i, (t, _, _) in enumerate(SECTIONS):
    out.append(f"- [{t}](#{anchor(t)})")
out.append("- [Forks we maintain](#forks-we-maintain)")
out.append("- [Related](#related)")
out.append("- [Contributing](#contributing)\n")
for i, (t, blurb, _) in enumerate(SECTIONS):
    out.append(f"## {t}\n")
    out.append(f"_{blurb}_\n")
    for n in assigned.get(i, []):
        out.append(item(n))
    out.append("")

out.append("## Forks we maintain\n")
out.append("_Upstream projects that V-Sekai-fire mirrors, pins or patches. The link goes to the fork; the parent is in brackets._\n")
out.append("<details>\n<summary>" + f"{len(frk)} forks" + "</summary>\n")
for n in sorted(frk, key=str.lower):
    p = (forks.get(n) or {}).get("parent") or {}
    parent = f"{p['owner']['login']}/{p['name']}" if p else ""
    d = describe(n)
    s = f"- [{n}](https://github.com/V-Sekai-fire/{n})"
    if parent:
        s += f" [[{parent}](https://github.com/{parent})]"
    if d:
        s += f" - {d}"
    out.append(s)
out.append("\n</details>\n")

out.append("## Related\n")
out.append("- [Awesome V-Sekai](https://github.com/V-Sekai/awesome-v-sekai) - The V-Sekai list this one follows.")
out.append("- [V-Sekai](https://github.com/V-Sekai) - The main V-Sekai organization.")
out.append("- [Taskweft](https://github.com/taskweft/taskweft) - The HTN planner.")
out.append("- [Awesome Godot](https://github.com/godotengine/awesome-godot) - Godot Engine frameworks, libraries and resources.\n")
out.append("## Contributing\n")
out.append("Read [CONTRIBUTING](CONTRIBUTING). Pull requests and issues are welcome.\n")
open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "README.md"), "w").write("\n".join(out))
print("orig", len(orig), "forks", len(frk), {SECTIONS[i][0]: len(v) for i, v in assigned.items() if i >= 0})
