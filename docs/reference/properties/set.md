# Set a property

Sets one property value and saves every selected content item.

!!! warning
    Preview the same property and selection with `show property` before running this command. A scoped selection can update many items.

## Syntax

```text
set property "<property-alias>" of content <selection> to "<new-value>"
```

## Examples

Set one value:

```text title="UmbraScript"
set property "latitude" of content at "/destinations/chicago/" to "41.8781"
```

Set the same value on direct children:

```text title="UmbraScript"
set property "region" of content in "/destinations/" to "Midwest"
```

## Behavior

The new value is supplied as a string. UmbraScript saves each item but does not publish it. The command does not select a culture or segment.

## Result

The result contains `summary`, `attempted`, `succeeded`, `failed`, and a `content` array. Each item includes `propertyExists`, `oldValue`, `newValue`, `success`, and `outcome`.

If a content type does not contain the alias, that item is returned as a failure with `propertyExists` set to `false`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for each content save.

## Common failures

- The content reference cannot be resolved.
- The property editor does not accept the supplied string format.
- Umbraco rejects the save operation.

## See also

- [Update property values safely](../../how-to/update-properties.md)
- [Clear a property](clear.md)
- [Publish content](../content/publish.md)
