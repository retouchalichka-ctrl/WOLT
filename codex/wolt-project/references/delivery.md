# Generation, Upscale & Delivery

## Generation

Confirm the approval gate first. Freeze the exact prompt version and attachment order in `06-generation-log.md`. Typically the approved storyboard is `@Image1` and the Wolt kraft bag is `@Image2`; include only files actually attached and give each a narrow job.

Log every generation, output file, earliest failure frame, decision, and controlled next revision. Select one approved master before upscale.

## Upscale

Upscale the selected master separately to UHD `3840×2160`, preserving 16:9, duration, frame rate/cadence, audio sync, composition, and color intent. Record tool/model/version and all material settings. Do not describe the result as native Seedance 4K.

Inspect at 100%:

- Wolt logo/food-icon print stability and edge halos;
- kraft-paper texture;
- faces, eyes, teeth, hands, contacts, and food detail;
- flicker, ghosting, banding, ringing, false detail, and interpolation artifacts;
- accidental pseudo-text on generic packaging;
- audio sync and duration.

## Delivery

Use the client's container, codec, bitrate, colorspace, frame-rate, and audio spec. If absent, request it before the final encode rather than inventing a standard. Record output checksum, filename, location/date, and client receipt.
