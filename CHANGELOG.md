# Changelog

All notable changes to this project will be documented in this file.

This project follows semantic versioning.

---

# Changelog

## [1.0.0] – 2025-12-19

### Added

- Full Markdown → HTML conversion
- Headings (`#` → `########`) with optional styling classes
- Paragraph handling
- Bold, italic, and inline code
- Fenced code blocks with syntax highlighting
- Ordered and unordered lists
- Images and links
- Tables with basic styling
- Blockquotes with nested Markdown support
- Recursive fenced div blocks (`:::`)
- CLI (`md2html`)
- Python API (`parse_markdown`)

### Fixed

- Correct parsing order for images vs links
- Nested container rendering issues
- Paragraph wrapping edge cases

### Design

- Single stable public API
- Internals hidden by convention
- Regex + state-machine based parser
- Extensible architecture for future renderers

---

Future versions will transition toward an AST-based parser for advanced features.

## [0.2.0] - 2025-12-15

### Added

- Initial Markdown → HTML parser
- CLI support (`md2html`)
- Python API (`parse_markdown`)
- Support for headings, lists, code blocks, images
- Fenced div blocks (`:::`)
- Optional full HTML document generation
- Optional syntax highlighting via CDN

### Notes

- Initial public release
