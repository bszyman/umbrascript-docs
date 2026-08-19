# Copy content

Copies one content item under another content item or to the content root. The copied item can be given a new name.

## Syntax

```text
copy content <reference> to <destination> [with name "<new-name>"]
```

## Examples

Copy and rename an item:

```text title="UmbraScript"
copy content at "/news/story/" to at "/archive/" with name "Story archive"
```

Copy an item to the root without renaming it:

```text title="UmbraScript"
copy content "b01b9237-ca8d-499a-aa97-de894cab5e3b" to root
```

## Behavior

The copy does not include descendants and is not related to the original through an Umbraco relation. When `with name` is present, UmbraScript copies first and then attempts a separate rename save.

## Result

The result contains batch summary counts and a one-item `content` array. The item distinguishes `copySucceeded` from the optional `renameSucceeded` and includes the source, destination, copied key, and final name.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the copy and optional rename operations.

## Common failures

- The source or destination cannot be resolved.
- The source resolves to more than one item.
- The requested name is empty.
- The copy succeeds but the requested rename fails; inspect both result fields.

## See also

- [Destinations](../../language/destinations.md)
- [Move content](move.md)
