# Restore content

Restores one content item from the Umbraco recycle bin.

## Syntax

```text
restore content <reference>
```

## Example

Use a key because a recycled item's former route may no longer resolve:

```text title="UmbraScript"
restore content "b01b9237-ca8d-499a-aa97-de894cab5e3b"
```

## Result

The result contains `key`, `name`, `success`, and `result`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the restore operation.

## Common failures

- The key cannot be found.
- The reference does not resolve to exactly one item.
- Umbraco cannot determine or use a restore destination.
- The current user cannot perform the restore operation.

## See also

- [Trash content](trash.md)
- [Show content](show.md)
