# Rename media

Changes the name of one media item and saves it.

## Syntax

```text
rename media <reference> to "<new-name>"
```

## Examples

Rename by path:

```text title="UmbraScript"
rename media at "/Images/old-logo.png" to "Primary logo"
```

Rename by key:

```text title="UmbraScript"
rename media "b01b9237-ca8d-499a-aa97-de894cab5e3b" to "Primary logo"
```

## Behavior

Renaming an item changes the name segment used by UmbraScript media paths. Retain the item key when a later command must target the renamed item.

## Result

The result contains `key`, `oldName`, `newName`, `success`, and `message`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the save operation.

## Common failures

- The reference does not resolve to exactly one media item.
- The path is ambiguous.
- Umbraco rejects the name or save operation.

## See also

- [Media paths](../../language/references-and-selections.md#media-paths)
- [Move media](move.md)
