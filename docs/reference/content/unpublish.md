# Unpublish content

Unpublishes one content item, the direct children of an item, or every descendant of an item.

!!! warning
    Unpublishing can remove pages from the public website immediately. Preview a scoped selection with `show content` first.

## Syntax

```text
unpublish content <selection>
```

## Examples

Unpublish one item by path:

```text title="UmbraScript"
unpublish content at "/destinations/pensacola-florida/"
```

Unpublish direct children:

```text title="UmbraScript"
unpublish content in "/destinations/"
```

Unpublish every descendant:

```text title="UmbraScript"
unpublish content below "/destinations/"
```

For a descendant selection, UmbraScript processes the resolved items in reverse order so deeper items are handled before earlier ancestors in the result set.

## Result

The result contains `requestedStatus`, `attempted`, `succeeded`, `failed`, and a `content` array. Each item contains `key`, `name`, `success`, and `outcome`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the unpublish operations.

## Common failures

- The reference cannot be resolved.
- An item is already in an incompatible state.
- Umbraco rejects the operation for the current user or content state.

## See also

- [Publish content](publish.md)
- [References and selections](../../language/references-and-selections.md)
