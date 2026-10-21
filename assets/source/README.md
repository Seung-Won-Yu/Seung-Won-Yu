# Artwork sources

These files are unchanged copies of artwork and public previews from the owner's projects. The profile compositions and sprite clipping are authored as SVG in `scripts/build_profile.py`.

- `ash-motion.webp`, `ash-portrait.webp`, `forest.webp`: [Rune Drift Survivors artwork](https://github.com/Seung-Won-Yu/rune-drift-survivors/tree/main/public/art/survivor). The motion sheet is a set of authored poses, not a generated video. The profile uses its first eight walking poses, with measured bounds from `src/survivor/actor-art.js`, at a common scale and foot baseline.
- `combat.jpg`: Rune Drift Survivors, `docs/design/survivor-restart/images/public-motion-combat-1280.jpg`.
- `autolabel.png`: [autolabel](https://github.com/Seung-Won-Yu/autolabel), `docs/og.png`.
- `pcb-sample.png`: the unchanged embedded sample in autolabel's `docs/deep-pcb-00041030.svg`.
- `workroom.png`: [Workroom Portal public preview](https://github.com/Seung-Won-Yu/workroom-portal-public), `docs/images/workroom-portal-preview.png`.
- `pocketdesk.png`: [PocketDesk OS](https://github.com/Seung-Won-Yu/pocket-desk-os), `public/brand/pocketdesk-social.png`.

Build with `python3 scripts/build_profile.py`. All generated SVGs are self-contained: embedded source images, local SVG references and inline CSS; no scripts, external resources or font services. The character's 3.2-second cycle plays eight poses for 1.28 seconds, then rests. `prefers-reduced-motion: reduce` shows only the first pose.

`assets/features/` pairs each complete project preview with its documented outcome. Desktop artwork is 1200×388 with the preview and result side by side; mobile artwork is 640×688 with the result below the preview. README `<picture>` elements select the viewport and color-scheme variant. Supporting descriptions, measurement conditions and links remain native Markdown. Publish generated assets first, then pin README image URLs to that immutable commit to avoid stale branch-image caches.
