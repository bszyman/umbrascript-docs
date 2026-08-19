# Move content

Moves one content item under another content item or to the content root.

!!! warning
    Moving content changes its place in the tree and can change its route. Use the key when later operations must target the moved item reliably.

## Syntax

```text
move content <reference> to <destination>
```

## Examples

Move an item under Archive:

```text title="UmbraScript"
move content at "/news/old-story/" to at "/archive/"
```

Move an item to the content root:

```text title="UmbraScript"
move content "b01b9237-ca8d-499a-aa97-de894cab5e3b" to root
```

## Result

The result contains `summary`, `attempted`, `succeeded`, `failed`, and a one-item `content` array. The item records the source, destination, `success`, and Umbraco `result`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the move operation.

## Common failures

- The source or destination cannot be resolved.
- The source resolves to more than one item.
- The destination is not valid for the source Document Type.
- Umbraco rejects the move for the current user or tree state.

## See also

- [Destinations](../../language/destinations.md)
- [Copy content](copy.md)
