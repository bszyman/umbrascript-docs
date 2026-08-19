# Update property values safely

Inspect a property's current values, make the change, and review every item result.

## Inspect the current values

Use the property alias and the intended selection:

```text title="UmbraScript"
show property "region" of content in "/destinations/"
```

The result tells you whether each content type contains the property and whether it currently has a value.

## Set the value

After checking the selection, run:

```text title="UmbraScript"
set property "region" of content in "/destinations/" to "Midwest"
```

Property values are supplied as strings. Confirm that the property's editor accepts the value format.

## Check the result

Review `attempted`, `succeeded`, and `failed`. Each content result includes `propertyExists`, `oldValue`, `newValue`, `success`, and `outcome`.

Setting a property saves the content item; it does not publish it. Publish separately when that is your intended workflow.

## Clear a value

Preview again, then use `clear property`:

```text title="UmbraScript"
clear property "legacyCode" of content below "/destinations/"
```

!!! warning
    `clear property` removes the stored value from every selected item that has the property. UmbraScript 1.0 does not select a culture or segment, so test set and clear operations carefully on variant content.
