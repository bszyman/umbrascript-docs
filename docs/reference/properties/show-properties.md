# Show all properties

Returns every property and current value for each selected content item. This command does not modify content.

## Syntax

```text
show properties of content <selection>
```

## Examples

Show every property on one item:

```text title="UmbraScript"
show properties of content at "/destinations/chicago/"
```

Show every property on direct children:

```text title="UmbraScript"
show properties of content in "/destinations/"
```

## Result

The result contains `summary`, `count`, and a `content` array. Each content entry includes `key`, `id`, `name`, `contentTypeAlias`, and a `properties` object keyed by property alias.

The returned values are the stored property values. Their JSON shapes depend on the Umbraco property editors in use.

## Common failures

- The content reference cannot be resolved.
- The selection's children or descendants cannot be loaded.
- The statement names a resource other than `content`.

## See also

- [Show a property](show-property.md)
- [Update property values safely](../../how-to/update-properties.md)
