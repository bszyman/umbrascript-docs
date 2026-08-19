# Rename content

Changes the name of one content item and saves it.

## Syntax

```text
rename content <reference> to "<new-name>"
```

## Examples

Rename by path:

```text title="UmbraScript"
rename content at "/news/old-title/" to "New title"
```

Rename by key:

```text title="UmbraScript"
rename content "b01b9237-ca8d-499a-aa97-de894cab5e3b" to "Pensacola guide"
```

## Behavior

The command saves the new name but does not publish the item. A rename can change the draft route, so retain the item key when a later command must target the same item.

## Result

The result contains `key`, `oldName`, `newName`, `success`, and `message`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the save operation.

## Common failures

- The reference does not resolve to exactly one content item.
- The new name is not accepted by Umbraco.
- The current user is unavailable for the save operation.

## See also

- [Publish content](publish.md)
- [References and selections](../../language/references-and-selections.md)
