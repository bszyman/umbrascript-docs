# Move media

Moves one media item under another media item or to the media root.

!!! warning
    Moving an item changes its media path. Use its key when later operations must target it reliably.

## Syntax

```text
move media <reference> to <destination>
```

## Examples

Move an item into Archive:

```text title="UmbraScript"
move media at "/Images/legacy-logo.png" to at "/Images/Archive/"
```

Move an item to the media root:

```text title="UmbraScript"
move media "b01b9237-ca8d-499a-aa97-de894cab5e3b" to root
```

## Result

The result contains `summary`, `attempted`, `succeeded`, `failed`, and a one-item `content` array. The item records the source, destination, `success`, and Umbraco `result`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the move operation.

## Common failures

- The source or destination cannot be resolved.
- A source or destination path is ambiguous.
- The destination is not valid for the media item.
- Umbraco rejects the move for the current user or tree state.

## See also

- [Destinations](../../language/destinations.md)
- [Copy media](copy.md)
