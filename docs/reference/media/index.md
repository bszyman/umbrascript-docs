# Media commands

Media commands inspect and organize items in the Umbraco media tree.

| Command | Scope | Changes data |
| --- | --- | --- |
| [`show media`](show.md) | Item, children, or descendants | No |
| [`create media folder`](create-folder.md) | One destination | Yes |
| [`rename media`](rename.md) | One item | Yes |
| [`move media`](move.md) | One item | Yes |
| [`copy media`](copy.md) | One item | Yes |
| [`trash media`](trash.md) | One item | Yes |
| [`restore media`](restore.md) | One item | Yes |

Media paths follow item names from the media root. Each path segment must have one case-insensitive match among its siblings. Use a key when names are ambiguous.

UmbraScript 1.0 creates media folders but does not upload new media files.
