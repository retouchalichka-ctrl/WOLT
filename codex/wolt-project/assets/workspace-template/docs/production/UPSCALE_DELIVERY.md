# UHD 4K Upscale & Delivery

4K delivery является отдельной post-production стадией после выбора master. Это не claim о native Seedance resolution.

## Target

- Frame: `3840×2160`, 16:9.
- Duration: ровно approved 15s master, если client spec не говорит иначе.
- Preserve: frame rate, cadence, audio duration/sync, composition, color intent и clean post-copy space.
- Codec/container/bitrate/audio/colorspace: брать из client delivery specification; если её нет, запросить до финального encode.

## Log

Записать source master, checksum, upscaler/tool, model/version, scale factor, denoise/deblur/sharpen/interpolation settings, output checksum и operator/date.

## Visual QA at 100%

- Wolt logo и food-icon print не wobble/morph, края без halos/ringing.
- Kraft paper сохраняет natural texture, без wax/plastic smoothing.
- Faces, eyes, teeth, hands и food contacts не «дорисованы» неверно.
- Food texture appetizing, без oversharpening, crawling crumbs или false detail.
- Нет flicker, ghosting, frame interpolation artifacts, banding, clipped highlights или crushed shadows.
- Generic packaging остаётся textless/unbranded; upscale не создаёт псевдотекст.
- Audio clean, sync and loudness unchanged unless отдельный mix approved.
