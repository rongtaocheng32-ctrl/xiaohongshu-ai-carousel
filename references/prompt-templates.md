# Image prompt templates

## Cover

```text
Use case: scientific-educational
Asset type: Xiaohongshu knowledge carousel cover, exact 3:4 portrait.
Topic: <topic>
Reader promise: <one takeaway>
Locked style: warm off-white editorial background; cobalt, coral, yellow, pink and teal diffused accents; rounded Cinema 4D forms and readable typography covered in dense, even, very-short microfiber plush; soft studio light; generous whitespace.
Composition: smaller setup line above a dominant centered keyword; one supporting visual metaphor in the middle; four small fixed corner labels.
Exact text only: <verbatim list>
Constraints: mobile-readable, clean letter edges, no extra words, no watermark, no logo, no long fur, no generic robot head.
```

## Interior page

```text
Use case: scientific-educational
Asset type: Xiaohongshu carousel page <n> of <total>, exact 3:4 portrait.
Educational job: <single page takeaway>
Style references: approved cover plus latest approved interior page.
Preserve: palette, off-white background, short-fur C4D material, light direction, corner positions, headline hierarchy and character construction.
Top text: <verbatim>
Middle visual story: <one visual metaphor with necessary objects only>
Bottom text: <verbatim>
Corner text: "2026" "GuangYing" "AI" "<keyword>"
Constraints: explanatory text only at top/bottom; center image-led; exact Chinese; no extra text; no watermark; no long fur.
```

## Targeted correction

```text
Edit target: <page path>
Change only: <one focused correction>
Preserve exactly: composition, objects, palette, 3:4 canvas, approved typography hierarchy, corner labels and all other wording.
Exact final text: <verbatim list>
Avoid: added words, spelling changes, distorted Chinese, material drift, layout drift.
```

## Prompting rules

- List every required string verbatim.
- Keep image text short; move explanation into the post body when appropriate.
- Make one targeted correction per edit.
- Use a separate generation call for every distinct page.
- Do not ask the model to reproduce a copyrighted reference. Describe transferable attributes instead.
