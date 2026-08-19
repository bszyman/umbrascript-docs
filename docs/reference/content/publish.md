# Publish content

Publishes one content item, the direct children of an item, or every descendant of an item.

!!! warning
    A scoped selection can publish many items immediately. Preview it with `show content` before running this command.

## Syntax

```text
publish content <selection>
```

## Examples

Publish one item by path:

```text title="UmbraScript"
publish content at "/destinations/pensacola-florida/"
```

Publish direct children:

```text title="UmbraScript"
publish content in "/destinations/"
```

Publish every descendant:

```text title="UmbraScript"
publish content below "/destinations/"
```

The `in` and `below` forms do not publish the anchor item.

## Result

The result contains `requestedStatus`, `attempted`, `succeeded`, `failed`, and a `content` array. Each item contains `key`, `name`, `success`, and `outcome`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the publish operations.

## Common failures

- The reference cannot be resolved.
- An item is invalid for publishing.
- Umbraco rejects the operation for the current user or content state.

Check every item outcome. A failed item does not roll back items that were already published.

## See also

- [Publish content in batches](../../how-to/batch-publish.md)
- [Unpublish content](unpublish.md)
