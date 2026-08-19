# Trash media

Moves one media item to the Umbraco recycle bin.

!!! warning
    Confirm the item with `show media` before moving it to the recycle bin.

## Syntax

```text
trash media <reference>
```

## Example

```text title="UmbraScript"
trash media at "/Images/unused-banner.jpg"
```

## Result

The result contains `key`, `name`, `success`, and `result`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the recycle-bin operation.

## Common failures

- The reference does not resolve to exactly one media item.
- The media path is ambiguous.
- Umbraco rejects the recycle-bin operation.

Keep the returned key if you may need to restore the item.

## See also

- [Restore media](restore.md)
- [Permissions and safe use](../../administration/permissions-and-safety.md)
