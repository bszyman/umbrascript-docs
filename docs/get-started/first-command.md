# Run your first command

Use `show content` to read one item from the content tree. This tutorial does not modify the item.

## Choose a content item

Find a content item with a route you know. This tutorial uses:

```text
/destinations/pensacola-florida/
```

Content paths begin with `/` and are written inside double quotation marks.

## Run the command

Open the UmbraScript console, enter the following statement, and run it:

```text title="UmbraScript"
show content at "/destinations/pensacola-florida/"
```

Replace the example path if it does not exist on your website.

## Read the result

A successful result contains one content summary:

```json
{
  "content": [
    {
      "key": "b01b9237-ca8d-499a-aa97-de894cab5e3b",
      "id": 1138,
      "name": "Pensacola, Florida",
      "contentTypeAlias": "destination",
      "created": "2026-07-07T07:13:44.29618Z",
      "lastModified": "2026-08-05T08:51:24.248402Z"
    }
  ]
}
```

The fields identify the item and its Document Type. Keep the `key` when you need a stable reference that does not depend on the item's route.

## Explore the children

Change `at` to `in` and use a parent path:

```text title="UmbraScript"
show content in "/destinations/"
```

`in` selects the direct children of the referenced item. It does not include the parent itself.

You now know how to run a statement, reference an item by path, and inspect a selection. Continue with [References and selections](../language/references-and-selections.md), or browse the [content command reference](../reference/content/index.md).
