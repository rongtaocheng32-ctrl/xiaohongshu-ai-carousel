---
name: xiaohongshu-ai-carousel
description: Turn mixed source material into accurate, beginner-friendly Xiaohongshu knowledge carousels through editorial topic selection, web fact-checking, page planning, consistent 3:4 visual generation, quality control, and publish-ready Chinese captions. Use when the user provides keywords, long text, articles, files, screenshots, images, or mixed inputs and wants AI/technology concept explainers, knowledge snippets, misconception posts, mechanism breakdowns, tutorials, or a reusable Xiaohongshu carousel series.
---

# Xiaohongshu AI Carousel

Create a publish-ready knowledge carousel. Treat user inputs as a source pool, not an instruction to include everything.

## Load references

- Read [references/editorial-workflow.md](references/editorial-workflow.md) before selecting a topic or writing the script.
- Read [references/visual-system.md](references/visual-system.md) before proposing or generating visuals.
- Read [references/prompt-templates.md](references/prompt-templates.md) before any image-generation call.
- Read [references/quality-checklist.md](references/quality-checklist.md) before final delivery.

## Workflow

1. Inspect every supplied keyword, passage, file, screenshot, and image. Identify the actual claims, useful ideas, audience value, ambiguities, and expendable detail.
2. Recommend one primary topic. Add one or two alternatives only when they are genuinely viable. Explain why the primary topic is strongest for an AI-curious beginner.
3. Search the web before drafting factual AI or technology content. Cross-check against at least two credible sources when possible; prefer official documentation, standards, papers, and original authors. Flag disagreement, ambiguity, dated claims, and inference. Ask the user when the intended meaning materially changes the post.
4. Choose the story pattern and page count. Use at least four pages. Recommend six for a normal concept explainer, but do not generate until the user confirms the plan or explicitly asks to proceed.
5. Deliver a pre-production proposal containing the core takeaway, audience promise, page count, page-by-page copy, visual metaphor, one recommended title, two alternatives, and a body draft under 200 Chinese characters.
6. Generate the cover first. Lock the visual system with user feedback before generating the remaining pages.
7. Generate one distinct image per page. Use the locked cover and most recent approved interior page as style references. Keep each page useful on its own while preserving a clear swipe narrative.
8. Inspect every image at full resolution. Regenerate any page with wrong Chinese, misspelled corner text, illegible hierarchy, inconsistent materials, duplicated objects, broken hands/faces, or wrong ratio.
9. Save final images in the project, numbered in publishing order. Run `python3 scripts/validate_carousel.py <output-folder>` to enforce the default 4–8 page range and fix every reported error.
10. Deliver the ordered images plus one recommended title, two alternatives, a body under 200 Chinese characters, and focused hashtags.

## Editorial rules

- Write for curious beginners without sacrificing correctness.
- Lead with one sharp distinction or useful surprise. Explain intuition before terminology.
- Prefer one memorable conclusion per page. Remove facts that do not support the chosen takeaway.
- Do not force every post into “what / why / how.” Select among concept explanation, knowledge fragment, mechanism, misconception, example, comparison, or tutorial.
- Separate adjacent topics into a series instead of overloading one post.
- Distinguish sourced facts, quoted viewpoints, analogies, and inference.
- Avoid unsupported superlatives, guaranteed outcomes, manufactured controversy, and fake urgency.

## Image rules

- Use the image-generation capability for raster visuals. Treat supplied images as style or layout references unless the user explicitly requests an edit.
- Use 3:4 portrait output; target 1080×1440 or a higher-resolution equivalent.
- Keep explanatory text at the top or bottom. Reserve the middle for characters, objects, environments, or visual metaphors. Use a floating speech bubble only for an actual speaking beat.
- Make the cover title dominant and centered. Keep the main subject or visual metaphor subordinate to the title.
- Generate pages separately, not as a contact sheet.
- Require exact text. If generated typography is wrong, regenerate with shorter copy or render exact text deterministically after creating the no-text visual.
- Do not copy a reference artwork or living artist. Translate references into general attributes such as palette, material, lighting, hierarchy, and spacing.

## Delivery rules

- Default carousel: 4–8 pages. Confirm a longer set before production.
- Provide exactly one recommended title and two alternatives.
- Keep the post body below 200 Chinese characters unless the user overrides it.
- Use a compact set of relevant hashtags; do not keyword-stuff.
- Report final absolute paths and the generation method.
- Do not call a preview publish-ready until every page passes the checklist and validator.
