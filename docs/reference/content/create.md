# Create content

Creates one content item with the specified name and Document Type alias under a parent or at the content root.

## Syntax

```text
create content named "<name>" of type "<document-type-alias>" at root
create content named "<name>" of type "<document-type-alias>" at "<parent-key>"
create content named "<name>" of type "<document-type-alias>" at "<parent-path>"
```

## Examples

Create an item below News:

```text title="UmbraScript"
create content named "Release notes" of type "article" at "/news/"
```

Create an item at the content root:

```text title="UmbraScript"
create content named "Site notice" of type "notice" at root
```

## Behavior

The new item has no initial property values. For a Document Type that varies by culture, UmbraScript uses the website's default culture for the initial name. The command creates but does not publish the item.

## Result

The result contains `summary`, `key`, `name`, `docType`, `success`, and `result`. `key` is `null` when creation fails.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the create operation.

## Common failures

- The name is empty or whitespace.
- The Document Type alias does not exist.
- The parent key or path cannot be resolved.
- Umbraco rejects the parent, Document Type, culture, or current user's operation.

## See also

- [Destinations](../../language/destinations.md)
- [Set a property](../properties/set.md)
- [Publish content](publish.md)
