# Trash content

Moves one content item to the Umbraco recycle bin.

!!! warning
    Confirm the item with `show content` before moving it to the recycle bin.

## Syntax

```text
trash content <reference>
```

## Example

```text title="UmbraScript"
trash content at "/news/old-story/"
```

## Result

The result contains `key`, `name`, `success`, and `result`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the recycle-bin operation.

## Common failures

- The reference cannot be resolved.
- The command does not resolve to exactly one item.
- Umbraco rejects the recycle-bin operation for the current user or content state.

Keep the returned key if you may need to restore the item.

## See also

- [Restore content](restore.md)
- [Permissions and safe use](../../administration/permissions-and-safety.md)
