# Batch 10 — image manifest (moroccoforamericans)

**21 images.** Landscape, ≥1600px, no faces, no brand signage.
Folder `moroccoforamericans/articles/`. **Key = filename, NO extension.**
URL: `https://img.sgfleetmedia.com/cdn-cgi/image/format=auto,width=1200/moroccoforamericans/articles/<key>` (width=1200 REQUIRED).

Name your files **1..21 in this exact order** — `rename-batch.mjs` maps them by number.

| # | key | shows | source |
|---|---|---|---|
| 1 | `casablanca-airport-arrival-hero` | Arriving at Casablanca Airport: Your First Two Hours | [Unsplash](https://unsplash.com/s/photos/arriving-casablanca-airport-your) · [Pexels](https://www.pexels.com/search/arriving%20casablanca%20airport%20your/) |
| 2 | `casablanca-airport-arrival-1` | The interior of Casablanca Mohammed V airport arrivals, no clear faces | [Unsplash](https://unsplash.com/s/photos/interior-casablanca-mohammed-airport) · [Pexels](https://www.pexels.com/search/interior%20casablanca%20mohammed%20airport/) |
| 3 | `casablanca-airport-arrival-2` | An ONCF train at the Casablanca airport station platform, no faces | 🎨 **generate** (prompt below) |
| 4 | `atlas-mountains-guide-hero` | The Atlas Mountains: Day Trips and Longer Stays | [Unsplash](https://unsplash.com/s/photos/atlas-mountains-trips-longer) · [Pexels](https://www.pexels.com/search/atlas%20mountains%20trips%20longer/) |
| 5 | `atlas-mountains-guide-1` | A High Atlas valley with a Berber village and terraced fields, no clea | [Unsplash](https://unsplash.com/s/photos/high-atlas-valley-berber) · [Pexels](https://www.pexels.com/search/high%20atlas%20valley%20berber/) |
| 6 | `atlas-mountains-guide-2` | A trekking trail in the High Atlas with mountain views, no clear faces | [Unsplash](https://unsplash.com/s/photos/trekking-trail-high-atlas) · [Pexels](https://www.pexels.com/search/trekking%20trail%20high%20atlas/) |
| 7 | `essaouira-guide-hero` | Essaouira: The Coast Escape from Marrakech | [Unsplash](https://unsplash.com/s/photos/essaouira-coast-escape-marrakech) · [Pexels](https://www.pexels.com/search/essaouira%20coast%20escape%20marrakech/) |
| 8 | `essaouira-guide-1` | The ramparts and harbour of Essaouira with blue fishing boats, no clea | [Unsplash](https://unsplash.com/s/photos/ramparts-harbour-essaouira-blue) · [Pexels](https://www.pexels.com/search/ramparts%20harbour%20essaouira%20blue/) |
| 9 | `essaouira-guide-2` | A quiet blue-and-white medina street in Essaouira, no clear faces | [Unsplash](https://unsplash.com/s/photos/quiet-blue-white-medina) · [Pexels](https://www.pexels.com/search/quiet%20blue%20white%20medina/) |
| 10 | `best-riads-marrakech-hero` | Riads in Marrakech: How to Choose One (Not Which One) | 🎨 **generate** (prompt below) |
| 11 | `best-riads-marrakech-1` | A Marrakech riad courtyard with a fountain and tilework, no faces | [Unsplash](https://unsplash.com/s/photos/marrakech-riad-courtyard-fountain) · [Pexels](https://www.pexels.com/search/marrakech%20riad%20courtyard%20fountain/) |
| 12 | `best-riads-marrakech-2` | A riad rooftop terrace overlooking the Marrakech medina, no faces | [Unsplash](https://unsplash.com/s/photos/riad-rooftop-terrace-overlooking) · [Pexels](https://www.pexels.com/search/riad%20rooftop%20terrace%20overlooking/) |
| 13 | `morocco-etiquette-customs-hero` | Etiquette and Customs in Morocco | [Unsplash](https://unsplash.com/s/photos/etiquette-customs-morocco) · [Pexels](https://www.pexels.com/search/etiquette%20customs%20morocco/) |
| 14 | `morocco-etiquette-customs-1` | A Moroccan tea pouring ritual with glasses on a tray, no faces | [Unsplash](https://unsplash.com/s/photos/moroccan-pouring-ritual-glasses) · [Pexels](https://www.pexels.com/search/moroccan%20pouring%20ritual%20glasses/) |
| 15 | `morocco-etiquette-customs-2` | An ornate madrasa courtyard with tilework in Morocco, no faces | [Unsplash](https://unsplash.com/s/photos/ornate-madrasa-courtyard-tilework) · [Pexels](https://www.pexels.com/search/ornate%20madrasa%20courtyard%20tilework/) |
| 16 | `alcohol-in-morocco-hero` | Alcohol in Morocco: Where You Can and Can't Drink | [Unsplash](https://unsplash.com/s/photos/alcohol-morocco-where-drink) · [Pexels](https://www.pexels.com/search/alcohol%20morocco%20where%20drink/) |
| 17 | `alcohol-in-morocco-1` | A rooftop bar table overlooking a Moroccan city at sunset, no faces | [Unsplash](https://unsplash.com/s/photos/rooftop-table-overlooking-moroccan) · [Pexels](https://www.pexels.com/search/rooftop%20table%20overlooking%20moroccan/) |
| 18 | `alcohol-in-morocco-2` | Bottles of Moroccan wine on a restaurant table, no faces | [Unsplash](https://unsplash.com/s/photos/bottles-moroccan-wine-restaurant) · [Pexels](https://www.pexels.com/search/bottles%20moroccan%20wine%20restaurant/) |
| 19 | `morocco-travel-insurance-hero` | Travel Insurance for Morocco: What It Needs to Cover | 🎨 **generate** (prompt below) |
| 20 | `morocco-travel-insurance-1` | A traveler with a daypack looking over a Moroccan landscape, no clear  | [Unsplash](https://unsplash.com/s/photos/traveler-daypack-looking-over) · [Pexels](https://www.pexels.com/search/traveler%20daypack%20looking%20over/) |
| 21 | `morocco-travel-insurance-2` | A camel trek in the desert dunes at sunset, no clear faces | [Unsplash](https://unsplash.com/s/photos/camel-trek-desert-dunes) · [Pexels](https://www.pexels.com/search/camel%20trek%20desert%20dunes/) |

## 🎨 Generation prompts — all 21 slots

A prompt for every slot, so you never have to hunt. The ones marked **generate** in
the table are the ones stock handles badly — abstract headlines, props, screens,
documents, currency. For the rest, try stock first and fall back to these.

### 1. `casablanca-airport-arrival-hero`

```
A wide, atmospheric establishing photograph for a travel article about: Arriving at Casablanca Airport, set in Morocco. Show it as one concrete, evocative real-world scene with a clear sense of place and depth — a location, a moment or an activity a traveler would actually encounter — never as text, a poster, a collage or an infographic. Rich foreground-to-background composition. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 2. `casablanca-airport-arrival-1`

```
The interior of Casablanca Mohammed V airport arrivals. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 3. `casablanca-airport-arrival-2` — 🎨 hard to source, generate this

```
An ONCF train at the Casablanca airport station platform. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 4. `atlas-mountains-guide-hero`

```
A wide, atmospheric establishing photograph for a travel article about: The Atlas Mountains, set in Morocco. Show it as one concrete, evocative real-world scene with a clear sense of place and depth — a location, a moment or an activity a traveler would actually encounter — never as text, a poster, a collage or an infographic. Rich foreground-to-background composition. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 5. `atlas-mountains-guide-1`

```
A High Atlas valley with a Berber village and terraced fields. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 6. `atlas-mountains-guide-2`

```
A trekking trail in the High Atlas with mountain views. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 7. `essaouira-guide-hero`

```
A wide, atmospheric establishing photograph for a travel article about: Essaouira, set in Morocco. Show it as one concrete, evocative real-world scene with a clear sense of place and depth — a location, a moment or an activity a traveler would actually encounter — never as text, a poster, a collage or an infographic. Rich foreground-to-background composition. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 8. `essaouira-guide-1`

```
The ramparts and harbour of Essaouira with blue fishing boats. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 9. `essaouira-guide-2`

```
A quiet blue-and-white medina street in Essaouira. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 10. `best-riads-marrakech-hero` — 🎨 abstract headline, generate this

```
A wide, atmospheric establishing photograph for a travel article about: Riads in Marrakech, set in Morocco. Show it as one concrete, evocative real-world scene with a clear sense of place and depth — a location, a moment or an activity a traveler would actually encounter — never as text, a poster, a collage or an infographic. Rich foreground-to-background composition. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 11. `best-riads-marrakech-1`

```
A Marrakech riad courtyard with a fountain and tilework. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 12. `best-riads-marrakech-2`

```
A riad rooftop terrace overlooking the Marrakech medina. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 13. `morocco-etiquette-customs-hero`

```
A wide, atmospheric establishing photograph for a travel article about: Etiquette and Customs in Morocco, set in Morocco. Show it as one concrete, evocative real-world scene with a clear sense of place and depth — a location, a moment or an activity a traveler would actually encounter — never as text, a poster, a collage or an infographic. Rich foreground-to-background composition. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 14. `morocco-etiquette-customs-1`

```
A Moroccan tea pouring ritual with glasses on a tray. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 15. `morocco-etiquette-customs-2`

```
An ornate madrasa courtyard with tilework in Morocco. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 16. `alcohol-in-morocco-hero`

```
A wide, atmospheric establishing photograph for a travel article about: Alcohol in Morocco, set in Morocco. Show it as one concrete, evocative real-world scene with a clear sense of place and depth — a location, a moment or an activity a traveler would actually encounter — never as text, a poster, a collage or an infographic. Rich foreground-to-background composition. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 17. `alcohol-in-morocco-1`

```
A rooftop bar table overlooking a Moroccan city at sunset. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 18. `alcohol-in-morocco-2`

```
Bottles of Moroccan wine on a restaurant table. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 19. `morocco-travel-insurance-hero` — 🎨 hard to source, generate this

```
A wide, atmospheric establishing photograph for a travel article about: Travel Insurance for Morocco, set in Morocco. Show it as one concrete, evocative real-world scene with a clear sense of place and depth — a location, a moment or an activity a traveler would actually encounter — never as text, a poster, a collage or an infographic. Rich foreground-to-background composition. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 20. `morocco-travel-insurance-1`

```
A traveler with a daypack looking over a Moroccan landscape. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

### 21. `morocco-travel-insurance-2`

```
A camel trek in the desert dunes at sunset. A real, specific moment somewhere in Morocco — a genuine everyday setting with natural surroundings, depth and context around the subject, as if photographed by a travel journalist who happened upon the scene. Shot as unstaged documentary travel photography on a full-frame camera, 35mm lens, f/2.8, natural available light with soft directional shadows and warm Moroccan tones. Candid and lived-in rather than posed or polished: real textures — worn plaster, aged wood, sun-faded fabric, dust, patina — shallow depth of field with a naturally blurred background, subtle imperfections, no studio look, no HDR, no over-saturation, no CGI smoothness. Landscape 3:2 aspect ratio, high resolution. No recognizable faces (people only distant, turned away, or cropped), no readable text or numbers, no logos or brand signage, no watermarks.
```

