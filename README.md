# Niceps

A 3D-anchored personal injury / anatomy **evidence log**. Stateless and browser-only — you own the file. Built by an injured climber, for people drowning in conflicting advice.

Click an entry in your patient card → the affected structures light up on a 3D body.

**Live:** https://niceps.pl

## Run locally

The page fetches the 3D model and patient-card JSON, which browsers block over `file://`.
Serve it over HTTP instead — from the project folder:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000/ (needs an internet connection — Three.js loads from a CDN).

## 3D model attribution

The anatomical model is **[Z-Anatomy](https://www.z-anatomy.com/)**, licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), itself derived from
**[BodyParts3D](https://lifesciencedb.jp/bp3d/)** (© The Database Center for Life Science,
licensed CC BY-SA 2.1 Japan).

The model file shipped here (`decimated_body.glb`) is a decimated derivative and is likewise
made available under CC BY-SA 4.0.

## License

- **Code:** [Apache License 2.0](LICENSE) © 2026 Filip Drapejkowski.
- **3D assets** (`*.glb` and any model exports): CC BY-SA 4.0, attribution above.
