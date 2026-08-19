# Clear a property

Removes one stored property value and saves every selected content item.

!!! warning
    Preview the same property and selection with `show property`. Clearing a scoped selection can remove values from many items.

## Syntax

```text
clear property "<property-alias>" of content <selection>
```

## Examples

Clear one value:

```text title="UmbraScript"
clear property "legacyCode" of content at "/destinations/chicago/"
```

Clear values from every descendant:

```text title="UmbraScript"
clear property "legacyCode" of content below "/destinations/"
```

## Behavior

UmbraScript removes the value and saves each item but does not publish it. The command does not select a culture or segment.

## Result

The result contains `summary`, `attempted`, `succeeded`, `failed`, and a `content` array. Each item includes `propertyExists`, `oldValue`, a null `newValue`, `success`, and `outcome`.

If a content type does not contain the alias, that item is returned as a failure with `propertyExists` set to `false`.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for each content save.

## Common failures

- The content reference cannot be resolved.
- The selected content does not contain the property.
- Umbraco rejects the save operation.

## See also

- [Show a property](show-property.md)
- [Set a property](set.md)
- [Permissions and safe use](../../administration/permissions-and-safety.md)
