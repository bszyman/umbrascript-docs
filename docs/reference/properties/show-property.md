# Show a property

Returns one property value for every selected content item. This command does not modify content.

## Syntax

```text
show property "<property-alias>" of content <selection>
```

## Examples

Show one value:

```text title="UmbraScript"
show property "latitude" of content at "/destinations/chicago/"
```

Show the value for direct children:

```text title="UmbraScript"
show property "region" of content in "/destinations/"
```

## Result

The `properties` array contains one entry per selected content item:

| Field | Meaning |
| --- | --- |
| `key` and `name` | The content item |
| `propertyAlias` | The requested alias |
| `propertyExists` | Whether the content type contains the property |
| `hasValue` | Whether the stored value is non-null |
| `value` | The stored value, or `null` |

## Common failures

- The content reference cannot be resolved.
- The selection's children or descendants cannot be loaded.
- The statement names a resource other than `content`.

A missing property is reported in the result rather than raised as a language error.

## See also

- [Show all properties](show-properties.md)
- [Set a property](set.md)
