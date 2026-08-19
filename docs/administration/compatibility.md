# Compatibility and limitations

## Requirements

UmbraScript 1.0 is designed for Umbraco CMS 17 and later.

## Language scope

UmbraScript 1.0 supports:

- One statement per execution
- Case-insensitive keywords
- Quoted string values
- Content, property, and media commands
- Single-item references by key or path
- Child and descendant selections for supported commands
- JSON results

It does not currently define variables, comments, control flow, or multi-statement scripts.

## Property limitations

- Property commands currently operate on content, not media.
- New property values are supplied as strings.
- Set and clear commands do not select a culture or segment.
- Property changes save content but do not publish it.

Test changes on representative content, especially when a Document Type varies by culture or uses a complex property editor.

## Tree and path behavior

- Content paths are Umbraco routes resolved using the default culture.
- Media paths follow media item names and must be unambiguous at each level.
- Keys are more stable than paths when an item may be renamed or moved.
- The media root is a destination, not an item that can be selected with `/`.

## Batch behavior

Only commands that accept a [selection](../language/references-and-selections.md) can target children or descendants. Rename, move, copy, restore, and create commands target or create one item at a time.

Batch operations are not documented as transactional. Always inspect per-item outcomes.
