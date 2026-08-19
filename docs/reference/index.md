# Command reference

The reference describes the exact syntax, supported scope, behavior, result fields, and common failures for every UmbraScript 1.0 command.

## Command groups

- [Content commands](content/index.md) inspect and manage the content tree.
- [Property commands](properties/index.md) read and change content property values.
- [Media commands](media/index.md) inspect and organize the media tree.

## Syntax notation

Reference pages use placeholders inside angle brackets:

| Placeholder | Meaning |
| --- | --- |
| `<key>` | A GUID key written as a quoted string |
| `<path>` | An absolute path written as a quoted string |
| `<reference>` | One item identified by `"<key>"` or `at "<path>"` |
| `<selection>` | A reference, `in "<key-or-path>"`, or `below "<key-or-path>"` |
| `<destination>` | `root`, `"<key>"`, or `at "<path>"` |

Square brackets indicate an optional clause. Do not type the angle or square brackets when running a command.

Read [References and selections](../language/references-and-selections.md) and [Destinations](../language/destinations.md) for the complete forms.

## Results

Result property names are shown in their JSON form. See [Results and errors](../language/results-and-errors.md) for common batch fields and diagnostic codes.
